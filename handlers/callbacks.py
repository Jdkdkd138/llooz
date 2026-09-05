# handlers/callbacks.py
"""Catch-all callback handler (func=lambda call: True). Огромный диспатчер для всех callback_data которые не поймали выделенные handlers. Внутри много if/elif веток для админ-кнопок и FSM-ввода."""

import time
import uuid
from datetime import datetime, timedelta
from bot_core import *
from bot_core import _SHUTDOWN_FLAG  # noqa: F401
from bot_ui import *  # noqa: F401,F403


def _clean_req(val):
    """Возвращает val если реквизит реально задан, иначе None (как в handlers/deals.py)."""
    if not val:
        return None
    bad = {'Не указан', 'Не указана', 'Не указано', 'Not set', 'Not specified', '未设置', 'غير محدد', 'غير محددة'}
    return None if str(val).strip() in bad else val


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    from bot_lang import get_text
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if is_user_blocked(user_id):
        bot.answer_callback_query(call.id, get_text(user_id, "you_are_blocked", users), show_alert=True)
        return

    init_user(user_id)
    update_user_activity(user_id)

    # ===== ГЛАВНОЕ МЕНЮ И ПРОФИЛЬ =====

    if call.data == 'main_menu':

        # Сброс всех awaiting-флагов при возврате в меню

        if user_id in users:
            for key in list(users[user_id].keys()):
                if key.startswith('awaiting_'):
                    users[user_id][key] = False
        # awaiting_scam_info — отдельный модульный dict (не внутри users[user_id]),
        # цикл выше его не трогает. Без этой строки залипший спор/скам-репорт
        # навсегда перехватывает ВЕСЬ последующий текстовый ввод юзера — даже
        # никак не связанный (например, накрутку баланса другому или ID
        # воркера в админке), потому что проверка awaiting_scam_info стоит
        # в начале handle_message раньше всей цепочки awaiting_*.
        awaiting_scam_info.pop(user_id, None)
        welcome_text, keyboard = main_menu(user_id)
        send_photo_message(chat_id, message_id, welcome_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'my_profile':
        show_user_profile(user_id, chat_id, message_id)
        bot.answer_callback_query(call.id)
    elif call.data == 'my_deals':
        show_user_deals(user_id, chat_id, message_id)
        bot.answer_callback_query(call.id)
    elif call.data == 'all_deals':
        show_user_deals(user_id, chat_id, message_id)
        bot.answer_callback_query(call.id)
    elif call.data == 'stats_public':
        show_stats_public(user_id, chat_id, message_id)
        bot.answer_callback_query(call.id)
    elif call.data == 'stats':
        if is_system_owner(user_id) or is_admin_own_team(user_id):
            show_stats_global(user_id, chat_id, message_id)
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        bot.answer_callback_query(call.id)
    elif call.data == 'force_save':
        if is_admin_any_team(user_id):
            save_data()
            bot.answer_callback_query(call.id, get_text(user_id, "data_saved", users), show_alert=True)
            show_stats_global(user_id, chat_id, message_id)
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)

    # ===== ПРОСМОТР СДЕЛКИ =====

    elif call.data.startswith('view_deal_'):
        deal_id = call.data.split('_')[2]

        if deal_id in deals:
            deal = deals[deal_id]

            if user_id == deal['seller_id']:
                status_text = get_text(user_id, 'deal_status_awaiting_buyer', users) if not deal.get('buyer_id') else get_text(user_id, 'deal_status_awaiting_payment', users)
                buyer_text = get_text(user_id, 'deal_buyer_awaiting', users) if not deal.get('buyer_id') else f"@{users[deal['buyer_id']]['username']}"
                verified_label = get_text(user_id, 'deal_verified_yes', users) if is_user_verified(user_id) else get_text(user_id, 'deal_verified_no', users)
                category_label = deal.get('category', get_text(user_id, 'deal_category_default', users))
                deal_text = f"""
{get_text(user_id, 'deal_view_seller_title', users)}

{get_text(user_id, 'deal_view_id', users)} #{deal_id[:8]}

{get_text(user_id, 'deal_view_status', users)} {status_text}

{get_text(user_id, 'deal_view_category', users)} {category_label}

{get_text(user_id, 'deal_view_desc', users)} {deal['description']}

{get_text(user_id, 'deal_view_amount', users)} {deal['amount']} {deal['currency']}

{get_text(user_id, 'deal_view_payment_method', users)} {deal['currency']}

{get_text(user_id, 'deal_view_your_verification', users)} {verified_label}

{get_text(user_id, 'deal_view_buyer_link', users)}
https://t.me/{bot.get_me().username}?start={deal_id}

{get_text(user_id, 'deal_view_buyer', users)} {buyer_text}

{get_text(user_id, 'deal_view_send_link', users)}
https://t.me/{bot.get_me().username}?start={deal_id}
"""
                send_photo_message(chat_id, message_id, deal_text, deal_seller_keyboard(deal_id, user_id))
            elif deal.get('buyer_id') == user_id:
                status_text = get_text(user_id, 'deal_status_awaiting_payment', users) if deal.get('status') == 'created' else get_text(user_id, 'deal_status_paid', users)
                verified_label = get_text(user_id, 'deal_verified_yes', users) if is_user_verified(deal['seller_id']) else get_text(user_id, 'deal_verified_no', users)
                category_label = deal.get('category', get_text(user_id, 'deal_category_default', users))
                deal_text = f"""
{get_text(user_id, 'deal_view_buyer_title', users)}

{get_text(user_id, 'deal_view_id', users)} #{deal_id[:8]}

{get_text(user_id, 'deal_view_status', users)} {status_text}

{get_text(user_id, 'deal_view_category', users)} {category_label}

{get_text(user_id, 'deal_view_desc', users)} {deal['description']}

{get_text(user_id, 'deal_view_amount', users)} {deal['amount']} {deal['currency']}

{get_text(user_id, 'deal_view_seller', users)} @{users[deal['seller_id']]['username']}

{get_text(user_id, 'deal_view_seller_rating', users)} {users[deal['seller_id']]['rating']}⭐

{get_text(user_id, 'deal_view_seller_verification', users)} {verified_label}

{get_text(user_id, 'deal_view_pay_from_balance', users)}
"""
                keyboard = deal_buyer_keyboard(deal_id, user_id)
                send_photo_message(chat_id, message_id, deal_text, keyboard)
        bot.answer_callback_query(call.id)

    # ===== УПРАВЛЕНИЕ РЕКВИЗИТАМИ =====

    elif call.data == 'wallet_menu':
        send_photo_message(chat_id, message_id, get_text(user_id, 'wallet_menu_title', users), wallet_menu_keyboard(user_id))
        bot.answer_callback_query(call.id)
    elif call.data == 'set_ton':
        user = users[user_id]
        ns = get_text(user_id, 'not_specified', users)
        current = user['ton_wallet'] if _clean_req(user.get('ton_wallet')) else ns
        wallet_text = f"""{get_text(user_id, 'wallet_crypto_title', users)}

{get_text(user_id, 'wallet_current', users)}
<code>{current}</code>

{get_text(user_id, 'wallet_send_crypto', users)}
{get_text(user_id, 'wallet_crypto_hint', users)}"""
        users[user_id]['awaiting_ton_wallet'] = True
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_back", users), callback_data='wallet_menu'))
        send_photo_message(chat_id, message_id, wallet_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'set_card':
        user = users[user_id]
        ns = get_text(user_id, 'not_specified_f', users)
        current = user['card_details'] if _clean_req(user.get('card_details')) else ns
        card_text = f"""{get_text(user_id, 'wallet_card_title', users)}

{get_text(user_id, 'wallet_current_card', users)}
<code>{current}</code>

{get_text(user_id, 'wallet_send_card', users)}
{get_text(user_id, 'wallet_card_hint', users)}"""
        users[user_id]['awaiting_card_details'] = True
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_back", users), callback_data='wallet_menu'))
        send_photo_message(chat_id, message_id, card_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'set_phone':
        user = users[user_id]
        ns = get_text(user_id, 'not_specified', users)
        current = user['phone_number'] if _clean_req(user.get('phone_number')) else ns
        phone_text = f"""{get_text(user_id, 'wallet_phone_title', users)}

{get_text(user_id, 'wallet_current_phone', users)}
<code>{current}</code>

{get_text(user_id, 'wallet_send_phone', users)}
{get_text(user_id, 'wallet_phone_hint', users)}"""
        users[user_id]['awaiting_phone'] = True
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_back", users), callback_data='wallet_menu'))
        send_photo_message(chat_id, message_id, phone_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'set_usdt':
        user = users[user_id]
        ns = get_text(user_id, 'not_specified', users)
        current = _clean_req(user.get('usdt_wallet')) or ns
        usdt_text = f"""{get_text(user_id, 'wallet_usdt_title', users)}

{get_text(user_id, 'wallet_current', users)}
<code>{current}</code>

{get_text(user_id, 'wallet_send_usdt', users)}
{get_text(user_id, 'wallet_usdt_hint', users)}"""
        users[user_id]['awaiting_usdt'] = True
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_back", users), callback_data='wallet_menu'))
        send_photo_message(chat_id, message_id, usdt_text, keyboard)
        bot.answer_callback_query(call.id)

    # ===== ВЫБОР ВАЛЮТЫ =====

    elif call.data == 'change_currency':
        currency_text = f"""
💱 <b>ВЫБОР ОСНОВНОЙ ВАЛЮТЫ</b>

<b>Выберите валюту для отображения баланса:</b>
• 🇷🇺 Rub — Российский рубль
• 🇺🇸 Usd — Доллар США
• 🇰🇿 Kzt — Казахстанский тенге
• 🇺🇦 Uah — Украинская гривна
• 🇧🇾 Byn — Белорусский рубль
• <tg-emoji emoji-id='5773677501825945508'>⚡</tg-emoji> Ton — The open network
• 💎 Usdt — Tether
• ⭐ Stars — Telegram Stars

<b>Ваша текущая валюта будет использоваться по умолчанию при создании сделок.</b>
"""
        send_photo_message(chat_id, message_id, currency_text, currency_menu_keyboard(user_id))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('currency_'):
        currency = call.data.split('_')[1]
        users[user_id]['currency'] = currency
        save_data()
        currency_updated_text = f"""
<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>ВАЛЮТА ИЗМЕНЕНА</b>

<b>Новая основная валюта:</b> {currency}

<b>Теперь баланс будет отображаться в выбранной валюте.</b>
<i>При создании сделок вы можете выбрать любую доступную валюту.</i>
"""
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton(get_text(user_id, "btn_stats", users), callback_data='stats_public'),
            InlineKeyboardButton(get_text(user_id, "btn_my_profile_nav", users), callback_data='my_profile')
        )
        keyboard.add(PremiumButton(get_text(user_id, "btn_back_menu", users), '🔜', '5893368370530621889', callback_data='main_menu'))
        send_photo_message(chat_id, message_id, currency_updated_text, keyboard)
        bot.answer_callback_query(call.id)

    # ===== СОЗДАНИЕ СДЕЛКИ =====

    elif call.data == 'create_deal':
        from bot_ui import deal_role_keyboard
        _t2 = lambda k: get_text(user_id, k, users)
        role_text = (
            _t2('deal_role_title') + '\n\n'
            '| ' + _t2('deal_role_question') + '\n\n'
            + _t2('deal_role_seller_desc') + '\n'
            + _t2('deal_role_buyer_desc')
        )
        send_photo_message(chat_id, message_id, role_text, deal_role_keyboard(user_id))
        bot.answer_callback_query(call.id)

    elif call.data == 'deal_role_seller':
        create_text = get_text(user_id, 'create_deal_text', users)
        send_photo_message(chat_id, message_id, create_text, create_deal_keyboard(user_id))
        bot.answer_callback_query(call.id)

    elif call.data == 'deal_role_buyer':
        for key in list(users[user_id].keys()):
            if key.startswith('awaiting_'):
                users[user_id][key] = False
        users[user_id]['current_deal'] = {'buyer_creates': True, 'buyer_id': user_id}
        users[user_id]['awaiting_buyer_currency'] = True
        create_text = get_text(user_id, 'create_deal_text', users)
        send_photo_message(chat_id, message_id, create_text, create_deal_keyboard(user_id))
        bot.answer_callback_query(call.id)

    elif call.data.startswith('method_'):
        currency = call.data.split('_')[1]
        for key in list(users[user_id].keys()):
            if key.startswith('awaiting_'):
                users[user_id][key] = False
        current_deal_data = users[user_id].get('current_deal', {})
        if isinstance(current_deal_data, dict) and current_deal_data.get('buyer_creates'):
            users[user_id]['current_deal']['currency'] = currency
            users[user_id]['awaiting_buyer_deal_amount'] = True
            _t = lambda k: get_text(user_id, k, users)
            amount_text = (
                _t('deal_amount_title') + '\n\n'
                + _t('deal_amount_examples') + '\n\n'
                + _t('deal_amount_min') + '\n\n'
                + _t('deal_amount_enter') + '\n'
            )
            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(InlineKeyboardButton(get_text(user_id, 'btn_back', users), callback_data='create_deal'))
            send_photo_message(chat_id, message_id, amount_text, keyboard)
            bot.answer_callback_query(call.id)
            return  # buyer_creates ветка уже отправила сообщение — не проваливаемся в seller-ветку ниже

        users[user_id]['awaiting_deal_amount'] = True
        users[user_id]['current_deal'] = {
            'currency': currency,
            'seller_id': user_id
        }

        _t = lambda k: get_text(user_id, k, users)
        if currency == 'STARS':
            amount_text = f"""{_t('deal_amount_title')}

{_t('deal_amount_min_stars')}

{_t('deal_amount_enter')}
"""
        else:
            amount_text = f"""{_t('deal_amount_title')}

{_t('deal_amount_examples')}

{_t('deal_amount_min')}

{_t('deal_amount_enter')}
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_back", users), callback_data='create_deal'))
        send_photo_message(chat_id, message_id, amount_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data.startswith('category_'):
        category = call.data.split('_')[1]
        category_names = {
            'gift': get_text(user_id, 'cat_gift', users),
            'nft': get_text(user_id, 'cat_nft', users),
            'channel': get_text(user_id, 'cat_channel', users),
            'stars': get_text(user_id, 'cat_stars', users),
            'other': get_text(user_id, 'cat_other', users),
        }
        default_category = get_text(user_id, 'deal_category_default', users)
        users[user_id]['current_deal']['category'] = category_names.get(category, default_category)
        # Покупатель: запрашиваем ссылку на товар; продавец: описание
        current_deal_data = users[user_id].get('current_deal', {})
        if isinstance(current_deal_data, dict) and current_deal_data.get('buyer_creates'):
            users[user_id]['awaiting_buyer_link'] = True
        else:
            users[user_id]['awaiting_deal_category'] = True

        category_label = category_names.get(category, default_category)
        if category == 'gift':
            description_text = get_text(user_id, 'desc_gift_text', users).format(category=category_label)
        elif category == 'stars':
            description_text = get_text(user_id, 'desc_stars_text', users).format(category=category_label)
        elif category == 'other':
            description_text = get_text(user_id, 'desc_other_text', users).format(category=category_label)
        else:
            description_text = get_text(user_id, 'desc_default_text', users).format(category=category_label)
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='back_to_category'))
        send_photo_message(chat_id, message_id, description_text, keyboard)
        bot.answer_callback_query(call.id)

    elif call.data == 'back_to_category':
        from bot_ui import product_category_keyboard
        for key in list(users[user_id].keys()):
            if key.startswith('awaiting_'):
                users[user_id][key] = False
        category_text = get_text(user_id, 'category_title', users)
        send_photo_message(chat_id, message_id, category_text, product_category_keyboard(user_id))
        bot.answer_callback_query(call.id)

    # ===== ВОРКЕР ПАНЕЛЬ =====

    elif call.data == 'worker_panel':
        if is_team_worker(user_id) or is_admin_own_team(user_id) or is_system_owner(user_id):

            # Сброс всех awaiting-флагов при возврате в панель

            for key in list(users[user_id].keys()):
                if key.startswith('awaiting_'):
                    users[user_id][key] = False
            worker_panel_text = f"""
👷 <b>ВОРКЕР ПАНЕЛЬ</b>

<b>Доступные действия:</b>
• 📊 Просмотр статистики
• 📋 Управление своими сделками
• 💼 Накрутка сделок (без лимита)
• <tg-emoji emoji-id='5902056028513505203'>💰</tg-emoji> Накрутка баланса (без лимита)
• 🏷️ Управление тегом для профитов
• 👥 Управление своими мамонтами

<b>Выберите действие:</b>
"""
            send_photo_message(chat_id, message_id, worker_panel_text, worker_panel_menu(user_id))
        else:
            bot.answer_callback_query(call.id, get_text(user_id, 'workers_admins_only', users), show_alert=True)
        bot.answer_callback_query(call.id)
    elif call.data == 'worker_stats':
        if is_team_worker(user_id) or is_admin_own_team(user_id) or is_system_owner(user_id):
            user = users[user_id]
            user_tag = get_user_tag(user_id)
            stats_text = f"""
👷 <b>ВАША СТАТИСТИКА</b>
<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>Воркер:</b> {user_tag}

🆔 <b>ID:</b> <code>{user_id}</code>

<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>Верификация:</b> {'✅ Да' if is_user_verified(user_id) else '❌ Нет'}

📅 <b>В системе с:</b> {user['join_date']}
⏰ <b>Последняя активность:</b> {user['last_active']}

<tg-emoji emoji-id='5895444149699612825'>📊</tg-emoji> <b>Общая статистика:</b>
• Успешных сделок: {user['success_deals']}
• Рейтинг: {user['rating']}⭐
• Споров выиграно: {user['disputes_won']}

👥 <b>Мои мамонты:</b>
• Всего мамонтов: {len(get_worker_mammoths(user_id))}
• Сделок мамонтов: {get_worker_mammoths_stats(user_id)['total_deals']}
<tg-emoji emoji-id='5902056028513505203'>💰</tg-emoji> <b>Баланс:</b>
• 🇷🇺 Rub: {user['balance']['RUB']}
• 🇺🇸 Usd: {user['balance']['USD']}
• <tg-emoji emoji-id='5773677501825945508'>⚡</tg-emoji> Ton: {user['balance']['TON']}
• 💎 Usdt: {user['balance']['USDT']}
• ⭐ Stars: {user['balance']['STARS']}

<b>Доступные действия:</b>
"""
            send_photo_message(chat_id, message_id, stats_text, worker_panel_menu(user_id))
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        bot.answer_callback_query(call.id)

    # ===== ИСПРАВЛЕННЫЙ ОБРАБОТЧИК НАКРУТКИ СДЕЛОК ДЛЯ ВОРКЕРОВ =====

    elif call.data == 'worker_fake_deals':
        if is_team_worker(user_id) or is_admin_own_team(user_id) or is_system_owner(user_id):
            users[user_id]['awaiting_fake_deals'] = True
            fake_deals_text = """
💼 <b>НАКРУТКА СДЕЛОК (ВОРКЕР)</b>

<b>Введите количество сделок:</b>
• Без лимита
• Только для себя

<b>Формат:</b>
<code>5</code>

<b>Введите количество:</b>
"""
            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='worker_panel'))
            send_photo_message(chat_id, message_id, fake_deals_text, keyboard)
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        bot.answer_callback_query(call.id)

    # ===== ОБРАБОТЧИК ОТКРУТКИ СДЕЛОК ДЛЯ ВОРКЕРОВ =====

    elif call.data == 'worker_remove_deals':
        if is_team_worker(user_id) or is_admin_own_team(user_id) or is_system_owner(user_id):
            users[user_id]['awaiting_remove_deals'] = True
            remove_deals_text = """
<tg-emoji emoji-id='5895444149699612825'>📉</tg-emoji> <b>ОТКРУТКА СДЕЛОК</b>

<b>Введите количество сделок для списания:</b>

<b>Формат:</b>
Для себя: <code>5</code>
Для другого: <code>123456789 10</code>

<b>Введите количество:</b>
"""
            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='worker_panel'))
            send_photo_message(chat_id, message_id, remove_deals_text, keyboard)
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        bot.answer_callback_query(call.id)

    # ===== ИСПРАВЛЕННЫЙ ОБРАБОТЧИК НАКРУТКИ БАЛАНСА ДЛЯ ВОРКЕРОВ =====

    elif call.data == 'worker_fake_balance':
        if is_team_worker(user_id) or is_admin_own_team(user_id) or is_system_owner(user_id):
            users[user_id]['awaiting_fake_balance'] = True
            fake_balance_text = """
<tg-emoji emoji-id='5902056028513505203'>💰</tg-emoji> <b>НАКРУТКА БАЛАНСА (ВОРКЕР)</b>

<b>Введите сумму и валюту:</b>
• Без лимита
• Доступные валюты: Ton, Rub, Usd, Kzt, Uah, Byn, Usdt, STARS
• Только для себя

<b>Формат:</b>
<code>1000 Rub</code>
<code>100 Stars</code>
<code>50 Ton</code>

<b>Введите:</b>
"""
            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='worker_panel'))
            send_photo_message(chat_id, message_id, fake_balance_text, keyboard)
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        bot.answer_callback_query(call.id)

    # ===== УРЕЗАНИЕ ПРОФИЛЯ (ВОРКЕР) =====

    elif call.data == 'worker_trim_profile':
        if is_team_worker(user_id) or is_admin_own_team(user_id) or is_system_owner(user_id):
            user = users[user_id]
            trim_text = f"""
<tg-emoji emoji-id='5920344347152224466'>✂️</tg-emoji> <b>УРЕЗАТЬ ПРОФИЛЬ</b>

<b>Текущие данные:</b>
• Успешных сделок: {user['success_deals']}
• Баланс TON: {user['balance']['TON']}
• Баланс RUB: {user['balance']['RUB']}
• Баланс USD: {user['balance']['USD']}
• Баланс USDT: {user['balance']['USDT']}
• Баланс Stars: {user['balance']['STARS']}

<b>Выберите что урезать:</b>
"""
            keyboard = InlineKeyboardMarkup(row_width=2)
            keyboard.add(
                InlineKeyboardButton(get_text(user_id, "btn_trim_deals", users), callback_data='worker_trim_deals'),
                InlineKeyboardButton(get_text(user_id, "btn_trim_balance", users), callback_data='worker_trim_balance')
            )
            keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='worker_panel'))
            send_photo_message(chat_id, message_id, trim_text, keyboard)
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        bot.answer_callback_query(call.id)
    elif call.data == 'worker_trim_deals':
        if is_team_worker(user_id) or is_admin_own_team(user_id) or is_system_owner(user_id):
            users[user_id]['awaiting_trim_deals'] = True
            trim_text = """
<tg-emoji emoji-id='5895444149699612825'>📉</tg-emoji> <b>УРЕЗАНИЕ СДЕЛОК</b>

<b>Введите количество сделок, которое хотите установить:</b>
• Текущее значение будет заменено на введённое
• Введите число (например: 5)

<b>Введите новое количество сделок:</b>
"""
            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='worker_trim_profile'))
            send_photo_message(chat_id, message_id, trim_text, keyboard)
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        bot.answer_callback_query(call.id)
    elif call.data == 'worker_trim_balance':
        if is_team_worker(user_id) or is_admin_own_team(user_id) or is_system_owner(user_id):
            users[user_id]['awaiting_trim_balance'] = True
            trim_text = """
<tg-emoji emoji-id='5811989245761426317'>💸</tg-emoji> <b>УРЕЗАНИЕ БАЛАНСА</b>

<b>Введите новую сумму и валюту:</b>
• Доступные валюты: Ton, Rub, Usd, Kzt, Uah, Byn, Usdt, Stars, Uzs

<b>Формат:</b>
<code>1000 Rub</code>
<code>5 Ton</code>
<code>0 Stars</code>

<b>Введите:</b>
"""
            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='worker_panel'))
            send_photo_message(chat_id, message_id, trim_text, keyboard)
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        bot.answer_callback_query(call.id)

    elif call.data == 'worker_trim_balance_direct':
        if is_team_worker(user_id) or is_admin_own_team(user_id) or is_system_owner(user_id):
            users[user_id]['awaiting_trim_balance'] = True
            trim_text = """
<tg-emoji emoji-id='5811989245761426317'>💸</tg-emoji> <b>УРЕЗАТЬ БАЛАНС</b>

<b>Введите новую сумму и валюту:</b>
• Доступные валюты: Ton, Rub, Usd, Kzt, Uah, Byn, Usdt, Stars, Uzs

<b>Формат:</b>
<code>1000 Rub</code>
<code>5 Ton</code>
<code>0 Stars</code>

<b>Введите:</b>
"""
            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='worker_panel'))
            send_photo_message(chat_id, message_id, trim_text, keyboard)
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        bot.answer_callback_query(call.id)

    elif call.data == 'worker_change_rating':
        if is_team_worker(user_id) or is_admin_own_team(user_id) or is_system_owner(user_id):
            users[user_id]['awaiting_change_rating'] = True
            current_rating = users[user_id].get('rating', 5.0)
            rating_text = f"""
<tg-emoji emoji-id='6028338546736107668'>⭐</tg-emoji> <b>ИЗМЕНИТЬ ОЦЕНКУ</b>

<b>Текущая оценка:</b> {current_rating}/5.0

Введите новую оценку от 1 до 5:
<i>Принимаются только целые числа: 1, 2, 3, 4, 5</i>
"""
            keyboard = InlineKeyboardMarkup(row_width=1)
            keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='worker_panel'))
            send_photo_message(chat_id, message_id, rating_text, keyboard)
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        bot.answer_callback_query(call.id)

    # ===== УПРАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯМИ (АДМИНКА) =====

    elif call.data == 'show_users':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        filtered_users = list(users.items())

        if not filtered_users:
            send_photo_message(chat_id, message_id, "📭 Нет пользователей", admin_panel_menu(user_id))
            bot.answer_callback_query(call.id)
            return

        users_text = f"""
👥 <b>СПИСОК ПОЛЬЗОВАТЕЛЕЙ</b>

<b>Всего:</b> {len(filtered_users)} пользователей

<b>Топ-5 по активности:</b>
"""
        sorted_users = sorted(filtered_users,
                             key=lambda x: datetime.strptime(x[1]['last_active'], "%d.%m.%Y %H:%M") if 'last_active' in x[1] else datetime.now(),
                             reverse=True)

        for idx, (uid, user_data) in enumerate(sorted_users[:5], 1):
            role = "<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji>"

            if is_system_owner(uid):
                role = "👑"
            elif is_admin_any_team(uid):
                role = "⚙️"
            elif is_team_worker(uid):
                role = "👷"

            if is_user_blocked(uid):
                role += " 🚫"
            verified_icon = "✅" if is_user_verified(uid) else "❌"
            users_text += f"\n{role} {verified_icon} <b>{idx}. @{user_data['username']}</b>"
            users_text += f"\n   🆔 ID: {uid}"
            users_text += f"\n   ✅ Сделок: {user_data['success_deals']}"
            users_text += f"\n   ⭐ Рейтинг: {user_data['rating']}"
            users_text += f"\n   📅 Регистрация: {user_data['join_date']}"
            users_text += f"\n   ⏰ Активность: {user_data['last_active']}"
            users_text += f"\n   ───────────────────"
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton(get_text(user_id, "btn_export_csv", users), callback_data='export_users'),
            InlineKeyboardButton(get_text(user_id, "btn_to_admin", users), callback_data='admin_panel')
        )
        send_photo_message(chat_id, message_id, users_text, keyboard)
        bot.answer_callback_query(call.id)

    # ===== УПРАВЛЕНИЕ ВОРКЕРАМИ =====

    elif call.data == 'show_workers':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        workers_list = list(team_workers.get(TEAM_GODS, set()))

        if not workers_list:
            send_photo_message(chat_id, message_id, f"📭 Нет воркеров", admin_panel_menu(user_id))
            bot.answer_callback_query(call.id)
            return

        workers_text = f"""
👷 <b>СПИСОК ВОРКЕРОВ</b>

<b>Всего:</b> {len(workers_list)} воркеров
"""

        for idx, worker_id in enumerate(workers_list[:5], 1):
            if worker_id in users:
                user_data = users[worker_id]
                user_tag = get_user_tag(worker_id)
                verified_icon = "✅" if is_user_verified(worker_id) else "❌"
                workers_text += f"\n<b>{idx}. {verified_icon} {user_tag}</b>"
                workers_text += f"\n   🆔 ID: {worker_id}"
                workers_text += f"\n   ✅ Сделок: {user_data['success_deals']}"
                workers_text += f"\n   👥 Мамонтов: {len(get_worker_mammoths(worker_id))}"
                workers_text += f"\n   ⭐ Рейтинг: {user_data['rating']}"
                workers_text += f"\n   📅 Регистрация: {user_data['join_date']}"
                workers_text += f"\n   ⏰ Активность: {user_data['last_active']}"
                workers_text += f"\n   ───────────────────"
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton(get_text(user_id, "btn_add_worker", users), callback_data='add_worker'),
            InlineKeyboardButton(get_text(user_id, "btn_remove_worker", users), callback_data='remove_worker')
        )
        keyboard.add(
            InlineKeyboardButton(get_text(user_id, "btn_check_deals", users), callback_data='check_worker_deals'),
            InlineKeyboardButton(get_text(user_id, "btn_demote_worker", users), callback_data='demote_worker')
        )
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_to_admin", users), callback_data='admin_panel'))
        send_photo_message(chat_id, message_id, workers_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'add_worker':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        users[user_id]['awaiting_worker_id'] = True
        worker_add_text = f"""
👷 <b>ДОБАВЛЕНИЕ ВОРКЕРА</b>

<b>Введите ID пользователя:</b>
• Можно получить через @userinfobot
• Или переслав сообщение пользователя
• Воркер автоматически получит уведомление

<b>Формат:</b>
<code>123456789</code>

<b>Введите ID:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='admin_panel'))
        send_photo_message(chat_id, message_id, worker_add_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'remove_worker':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        users[user_id]['awaiting_remove_worker'] = True
        remove_worker_text = f"""
🗑️ <b>УДАЛЕНИЕ ВОРКЕРА</b>

<b>Введите ID воркера:</b>
• Можно получить через список воркеров
• Воркер получит уведомление о лишении прав

<b>Формат:</b>
<code>123456789</code>

<b>Введите ID:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='admin_panel'))
        send_photo_message(chat_id, message_id, remove_worker_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data.startswith('remove_worker_confirm_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        worker_id = int(call.data.split('_')[3])

        if worker_id in team_workers.get(TEAM_GODS, set()):
            team_workers[TEAM_GODS].remove(worker_id)
            save_data()
            log_activity(user_id, f'Удалил воркера ID:{worker_id}')

            if worker_id in users:
                worker_name = users[worker_id]['username']
                notification_text = f"""
<tg-emoji emoji-id='5922712343011135025'>❌</tg-emoji> <b>ВЫ БЫЛИ ЛИШЕНЫ СТАТУСА ВОРКЕРА</b>
Ваш статус воркера был отозван администратором.
Теперь вы являетесь обычным пользователем.
Если это ошибка, свяжитесь с поддержкой.
"""

                try:
                    bot.send_message(worker_id, notification_text, parse_mode='HTML')
                except:
                    pass

            result_text = f"""
<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>ВОРКЕР УДАЛЁН</b>

<b>Воркер:</b> @{worker_name if worker_id in users else worker_id}

<b>ID:</b> <code>{worker_id}</code>

<b>Удалил:</b> @{users[user_id]['username']}

<b>Время:</b> {datetime.now().strftime("%d.%m.%Y %H:%M")}

<b>Статус воркера успешно отозван.</b>
"""
            send_photo_message(chat_id, message_id, result_text, admin_panel_menu(user_id))
        else:
            bot.answer_callback_query(call.id, get_text(user_id, "user_not_worker", users), show_alert=True)
        bot.answer_callback_query(call.id)
    elif call.data == 'check_worker_deals':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        users[user_id]['awaiting_check_deals'] = True
        check_deals_text = f"""
🔍 <b>ПРОВЕРКА СДЕЛОК ВОРКЕРА</b>

<b>Введите ID воркера:</b>
• Можно получить через список воркеров
• Будет показана полная статистика

<b>Формат:</b>
<code>123456789</code>

<b>Введите ID:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='admin_panel'))
        send_photo_message(chat_id, message_id, check_deals_text, keyboard)
        bot.answer_callback_query(call.id)

    # ===== УПРАВЛЕНИЕ АДМИНАМИ (ТОЛЬКО ВЛАДЕЛЕЦ) =====

    elif call.data == 'show_admins':
        if not is_system_owner(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "owner_only_admins", users), show_alert=True)
            return

        admins_text = f"""
👑 <b>СПИСОК АДМИНИСТРАТОРОВ</b>

<b>Всего администраторов:</b> {len(team_admins.get(TEAM_GODS, set()))}

<b>Страница:</b> 1
"""
        send_photo_message(chat_id, message_id, admins_text, admins_list_menu())
        bot.answer_callback_query(call.id)
    elif call.data.startswith('show_admins_'):
        if not is_system_owner(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        page = int(call.data.split('_')[2])
        admins_text = f"""
👑 <b>СПИСОК АДМИНИСТРАТОРОВ</b>

<b>Всего администраторов:</b> {len(team_admins.get(TEAM_GODS, set()))}

<b>Страница:</b> {page + 1}
"""
        send_photo_message(chat_id, message_id, admins_text, admins_list_menu(page))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('view_admin_'):
        if not is_system_owner(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        admin_id = int(call.data.split('_')[2])

        if admin_id in users:
            show_user_profile(admin_id, chat_id, message_id)
        bot.answer_callback_query(call.id)
    elif call.data == 'add_admin':
        if not is_system_owner(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "owner_only_add_admin", users), show_alert=True)
            return

        users[user_id]['awaiting_admin_id'] = True
        admin_add_text = f"""
👑 <b>ДОБАВЛЕНИЕ АДМИНИСТРАТОРА</b>

<b>Введите ID пользователя:</b>
• Администратор получит доступ к админ панели
• Можно добавить только одного пользователя

<b>Пример:</b>
<code>123456789</code>

<b>Введите ID:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='admin_panel'))
        send_photo_message(chat_id, message_id, admin_add_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'remove_admin':
        if not is_system_owner(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "owner_only_remove_admin", users), show_alert=True)
            return

        users[user_id]['awaiting_remove_worker'] = True
        remove_admin_text = f"""
🗑️ <b>УДАЛЕНИЕ АДМИНИСТРАТОРА</b>

<b>Введите ID администратора:</b>
• Можно получить через список администраторов
• Владельца системы удалить нельзя
• Администратор получит уведомление

<b>Формат:</b>
<code>123456789</code>

<b>Введите ID:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='admin_panel'))
        send_photo_message(chat_id, message_id, remove_admin_text, keyboard)
        bot.answer_callback_query(call.id)

    # ===== НАКРУТКИ (АДМИН) =====

    elif call.data == 'fake_deals':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        users[user_id]['awaiting_fake_deals'] = True
        fake_deals_text = f"""
💼 <b>НАКРУТКА СДЕЛОК (АДМИН)</b>

<b>Введите данные:</b>
• ID пользователя
• Количество сделок (без лимита)

<b>Формат:</b>
<code>123456789 10</code>

<b>Пример:</b>
<code>1521791703 50</code> — добавить 50 сделок пользователю

<b>Введите:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='admin_panel'))
        send_photo_message(chat_id, message_id, fake_deals_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'fake_balance':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        users[user_id]['awaiting_fake_balance'] = True
        fake_balance_text = f"""
<tg-emoji emoji-id='5902056028513505203'>💰</tg-emoji> <b>НАКРУТКА БАЛАНСА (АДМИН)</b>

<b>Введите данные:</b>
• ID пользователя
• Сумма (без лимита)
• Валюта (Ton/Rub/Usd/Kzt/Uah/Byn/Usdt/STARS)

<b>Формат:</b>
<code>123456789 100 Rub</code>

<b>Примеры:</b>
<code>1521791703 5000 Rub</code>
<code>1521791703 50 Ton</code>
<code>1521791703 1000 Stars</code>

<b>Введите:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='admin_panel'))
        send_photo_message(chat_id, message_id, fake_balance_text, keyboard)
        bot.answer_callback_query(call.id)

    # ===== СПОРЫ =====

    elif call.data.startswith('dispute_'):
        deal_id = call.data.split('_')[1]

        if deal_id not in deals:
            bot.answer_callback_query(call.id, get_text(user_id, "deal_not_found", users), show_alert=True)
            return

        role_label = get_text(user_id, 'dispute_role_buyer', users) if user_id == deals[deal_id].get('buyer_id') else get_text(user_id, 'dispute_role_seller', users)
        dispute_text = f"""
{get_text(user_id, 'dispute_title', users)}

{get_text(user_id, 'dispute_deal', users)} #{deal_id[:8]}
{get_text(user_id, 'dispute_role', users)} {role_label}

{get_text(user_id, 'dispute_support', users)} {MANAGER_USERNAME}

{get_text(user_id, 'dispute_confirm', users)}

{get_text(user_id, 'dispute_reason', users)}
"""
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton(get_text(user_id, "btn_not_paid", users), callback_data=f'dispute_nopay_{deal_id}'),
            InlineKeyboardButton(get_text(user_id, "btn_not_sent", users), callback_data=f'dispute_nosend_{deal_id}')
        )
        keyboard.add(
            InlineKeyboardButton(get_text(user_id, "btn_wrong_item", users), callback_data=f'dispute_wrong_{deal_id}'),
            InlineKeyboardButton(get_text(user_id, "btn_other_reason", users), callback_data=f'dispute_other_{deal_id}')
        )
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_back", users), callback_data=f'view_deal_{deal_id}'))
        send_photo_message(chat_id, message_id, dispute_text, keyboard)
        bot.answer_callback_query(call.id)

    # ===== ПРОСМОТР ВСЕХ СДЕЛОК АДМИНОМ =====

    elif call.data == 'all_deals_admin':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        show_all_deals_admin(user_id, chat_id, message_id)
        bot.answer_callback_query(call.id)
    elif call.data.startswith('all_deals_admin_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        page = int(call.data.split('_')[3])
        show_all_deals_admin(user_id, chat_id, message_id, page)
        bot.answer_callback_query(call.id)
    elif call.data.startswith('admin_view_deal_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        deal_id = call.data.split('_')[3]
        show_deal_details_admin(user_id, chat_id, message_id, deal_id)
        bot.answer_callback_query(call.id)

    # ===== ПРОСМОТР ДЕЙСТВИЙ В СДЕЛКЕ =====

    elif call.data == 'deal_activities_admin':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        activities_text = """
🔍 <b>ПРОСМОТР ДЕЙСТВИЙ В СДЕЛКЕ</b>

<b>Выберите сделку для просмотра истории действий:</b>
• Отображаются только сделки с зафиксированными действиями
• Для каждой сделки показано количество действий
• Можно увидеть полный лог всех операций
"""
        send_photo_message(chat_id, message_id, activities_text, deal_activities_menu_keyboard(user_id))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('deal_activities_menu_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        page = int(call.data.split('_')[3])
        activities_text = f"""
🔍 <b>ПРОСМОТР ДЕЙСТВИЙ В СДЕЛКЕ</b>

<b>Страница:</b> {page + 1}

<b>Выберите сделку для просмотра истории действий:</b>
"""
        send_photo_message(chat_id, message_id, activities_text, deal_activities_menu_keyboard(user_id, page))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('admin_deal_activity_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        parts = call.data.split('_')
        deal_id = parts[3]
        page = int(parts[4]) if len(parts) > 4 else 0
        show_deal_activities_admin(user_id, chat_id, message_id, deal_id, page)
        bot.answer_callback_query(call.id)

    # ===== ПРОСМОТР ДЕЙСТВИЙ ПОЛЬЗОВАТЕЛЯ =====

    elif call.data == 'user_activities_admin':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        activities_text = """
<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>ПРОСМОТР ДЕЙСТВИЙ ПОЛЬЗОВАТЕЛЯ</b>

<b>Выберите пользователя для просмотра истории действий:</b>
• Отображаются только пользователи с зафиксированными действиями
• Для каждого пользователя показано количество действий
• Можно увидеть полную историю активности
"""
        send_photo_message(chat_id, message_id, activities_text, user_activities_menu_keyboard(user_id))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('user_activities_menu_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        page = int(call.data.split('_')[3])
        activities_text = f"""
<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>ПРОСМОТР ДЕЙСТВИЙ ПОЛЬЗОВАТЕЛЯ</b>

<b>Страница:</b> {page + 1}

<b>Выберите пользователя для просмотра истории действий:</b>
"""
        send_photo_message(chat_id, message_id, activities_text, user_activities_menu_keyboard(user_id, page))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('admin_user_activity_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        parts = call.data.split('_')
        target_user_id = int(parts[3])
        page = int(parts[4]) if len(parts) > 4 else 0
        show_user_activities_admin(user_id, chat_id, message_id, target_user_id, page)
        bot.answer_callback_query(call.id)
    elif call.data.startswith('admin_view_user_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        target_user_id = int(call.data.split('_')[3])

        if target_user_id in users:
            show_user_profile(target_user_id, chat_id, message_id)
        bot.answer_callback_query(call.id)

    # ===== РАССЫЛКИ =====

    elif call.data == 'broadcast_menu':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        broadcast_text = """
📢 <b>РАССЫЛКА СООБЩЕНИЙ</b>

<b>Выберите тип рассылки:</b>
• 📢 Всем пользователям — сообщение получит каждый зарегистрированный пользователь
• 👷 Только воркерам — сообщение получат все воркеры
• 👑 Только админам — сообщение получат все администраторы
• <tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> Конкретному пользователю — личное сообщение одному пользователю

<b>Внимание:</b> Массовая рассылка может занять некоторое время!

<b>Поддерживается:</b> HTML-разметка, фото, документы
"""
        send_photo_message(chat_id, message_id, broadcast_text, broadcast_menu_keyboard(user_id))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('broadcast_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        broadcast_type = call.data.split('_')[1]
        awaiting_broadcast_message[user_id] = broadcast_type

        if broadcast_type == 'all':
            recipient_text = "всем пользователям"
            count = len(users)
        elif broadcast_type == 'workers':
            recipient_text = "всем воркерам"
            count = len(team_workers.get(TEAM_GODS, set()))
        elif broadcast_type == 'admins':
            recipient_text = "всем администраторам"
            count = len(team_admins.get(TEAM_GODS, set()))
        else:
            recipient_text = "получателям"
            count = 0
        broadcast_instruction = f"""
✉️ <b>ПОДГОТОВКА РАССЫЛКИ</b>

<b>Тип рассылки:</b> {recipient_text}

<b>Количество получателей:</b> {count}

<b>Отправьте сообщение для рассылки:</b>
• Поддерживается HTML-разметка
• Можно отправлять текст, фото, документы
• Для отмены нажмите /cancel

<b>Пример сообщения:</b>
<code>🎉 Новое обновление системы!
Добавлены новые функции и улучшена безопасность.</code>

<b>Отправьте ваше сообщение:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='broadcast_menu'))
        send_photo_message(chat_id, message_id, broadcast_instruction, keyboard)
        bot.answer_callback_query(call.id)

    # ===== ЛИЧНЫЕ СООБЩЕНИЯ =====

    elif call.data == 'private_message_menu':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        private_message_text = """
✉️ <b>ЛИЧНОЕ СООБЩЕНИЕ</b>

<b>Выберите действие:</b>
• ✉️ Написать пользователю — отправить сообщение конкретному пользователю
• 📋 Список получателей — просмотреть всех пользователей для выбора

<b>Личное сообщение отправляется от имени бота.</b>

<b>Поддерживается:</b> HTML-разметка, фото, документы
"""
        send_photo_message(chat_id, message_id, private_message_text, private_message_menu_keyboard(user_id))
        bot.answer_callback_query(call.id)
    elif call.data == 'private_message':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        awaiting_private_message[user_id] = True
        private_message_instruction = """
<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>ЛИЧНОЕ СООБЩЕНИЕ ПОЛЬЗОВАТЕЛЮ</b>

<b>Введите ID пользователя и сообщение:</b>
• Формат: <code>123456789 Ваше сообщение здесь</code>
• ID можно получить из профиля пользователя
• Или используйте список получателей для выбора

<b>Пример:</b>
<code>1521791703 Привет! Это тестовое сообщение от администратора.</code>

<b>Введите ID и сообщение:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_recipient_list", users), callback_data='private_message_list_0'))
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='private_message_menu'))
        send_photo_message(chat_id, message_id, private_message_instruction, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data.startswith('private_message_list_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        page = int(call.data.split('_')[3])
        recipients_text = f"""
<tg-emoji emoji-id='5956561916573782596'>📋</tg-emoji> <b>СПИСОК ПОЛУЧАТЕЛЕЙ</b>

<b>Страница:</b> {page + 1}

<b>Выберите пользователя для отправки сообщения:</b>
"""
        send_photo_message(chat_id, message_id, recipients_text, private_message_recipients_keyboard(user_id, page))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('select_recipient_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        recipient_id = int(call.data.split('_')[2])
        awaiting_private_message[user_id] = recipient_id
        recipient = users.get(recipient_id, {'username': f'ID:{recipient_id}'})
        recipient_text = f"""
<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>ПОЛУЧАТЕЛЬ ВЫБРАН</b>

<b>Пользователь:</b> @{recipient['username']}

<b>ID:</b> <code>{recipient_id}</code>

<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>Верификация:</b> {'✅ Да' if is_user_verified(recipient_id) else '❌ Нет'}

<b>Теперь отправьте сообщение для этого пользователя:</b>
• Поддерживается HTML-разметка
• Можно отправлять текст, фото, документы
• Для отмены нажмите /cancel

<b>Отправьте ваше сообщение:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_select_other", users), callback_data='private_message_list_0'))
        send_photo_message(chat_id, message_id, recipient_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data.startswith('admin_message_user_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        target_user_id = int(call.data.split('_')[3])
        awaiting_private_message[user_id] = target_user_id
        target_user = users.get(target_user_id, {'username': f'ID:{target_user_id}'})
        message_text = f"""
✉️ <b>СООБЩЕНИЕ ПОЛЬЗОВАТЕЛЮ</b>

<b>Получатель:</b> @{target_user['username']}

<b>ID:</b> <code>{target_user_id}</code>

<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>Верификация:</b> {'✅ Да' if is_user_verified(target_user_id) else '❌ Нет'}

<b>Отправьте сообщение для этого пользователя:</b>
• Поддерживается HTML-разметка
• Можно отправлять текст, фото, документы
• Для отмены нажмите /cancel

<b>Отправьте ваше сообщение:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data=f'admin_user_activity_{target_user_id}_0'))
        send_photo_message(chat_id, message_id, message_text, keyboard)
        bot.answer_callback_query(call.id)

    # ===== ПОИСК =====

    elif call.data == 'search_deal_admin':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        users[user_id]['awaiting_search_deal'] = True
        search_text = """
🔍 <b>ПОИСК СДЕЛКИ</b>

<b>Введите ID сделки или часть ID:</b>
• Полный ID: <code>123e4567-e89b-12d3-a456-426614174000</code>
• Короткий ID: <code>123e4567</code>

<b>Введите ID для поиска:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='all_deals_admin'))
        send_photo_message(chat_id, message_id, search_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data in ['search_deal_activity_admin', 'search_user_activity_admin', 'search_recipient_admin']:
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        search_type = call.data.replace('_admin', '')
        users[user_id][f'awaiting_search_{search_type}'] = True

        if 'deal' in search_type:
            search_text = """
🔍 <b>ПОИСК СДЕЛКИ ДЛЯ ПРОСМОТРА АКТИВНОСТИ</b>

<b>Введите ID сделки или часть ID:</b>
• Полный ID: <code>123e4567-e89b-12d3-a456-426614174000</code>
• Короткий ID: <code>123e4567</code>

<b>Введите ID для поиска:</b>
"""
            back_button = 'deal_activities_admin'
        elif 'user' in search_type or 'recipient' in search_type:
            search_text = """
🔍 <b>ПОИСК ПОЛЬЗОВАТЕЛЯ</b>

<b>Введите ID пользователя или username:</b>
• ID: <code>123456789</code>
• Username: <code>username</code> (без @)

<b>Введите данные для поиска:</b>
"""
            back_button = 'user_activities_admin' if 'user' in search_type else 'private_message_menu'
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data=back_button))
        send_photo_message(chat_id, message_id, search_text, keyboard)
        bot.answer_callback_query(call.id)

    # ===== УПРАВЛЕНИЕ БЛОКИРОВКАМИ =====

    elif call.data == 'block_user_menu':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "admin_block_only", users), show_alert=True)
            return

        block_menu_text = """
🚫 <b>УПРАВЛЕНИЕ БЛОКИРОВКАМИ</b>

<b>Выберите действие:</b>
• 🚫 Заблокировать пользователя — полностью отключить доступ к боту
• ✅ Разблокировать пользователя — восстановить доступ
• 📋 Список заблокированных — просмотреть всех заблокированных пользователей

<b>Внимание:</b> Блокировка применяется ко всем уровням пользователей (включая администраторов и воркеров)
"""
        send_photo_message(chat_id, message_id, block_menu_text, block_user_menu_keyboard(user_id))
        bot.answer_callback_query(call.id)
    elif call.data == 'block_user':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return
        # Сброс всех awaiting-флагов
        for key in list(users[user_id].keys()):
            if key.startswith('awaiting_'):
                users[user_id][key] = False
        users[user_id]['awaiting_block_user'] = True
        block_user_text = """
🚫 <b>БЛОКИРОВКА ПОЛЬЗОВАТЕЛЯ</b>

<b>Введите ID пользователя:</b>
• Можно заблокировать любого пользователя (включая администраторов и воркеров)
• Пользователь потеряет доступ ко всем функциям бота
• Для разблокировки потребуется действие администратора

<b>Формат:</b>
<code>123456789</code>

<b>Введите ID пользователя для блокировки:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='block_user_menu'))
        send_photo_message(chat_id, message_id, block_user_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'unblock_user':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        users[user_id]['awaiting_unblock_user'] = True
        unblock_user_text = """
<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>РАЗБЛОКИРОВКА ПОЛЬЗОВАТЕЛЯ</b>

<b>Введите ID пользователя:</b>
• Пользователь получит доступ к функциям бота согласно своему уровню
• Уровень пользователя сохраняется после разблокировки

<b>Формат:</b>
<code>123456789</code>

<b>Введите ID пользователя для разблокировки:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='block_user_menu'))
        send_photo_message(chat_id, message_id, unblock_user_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'blocked_users_list':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        filtered_blocked = list(blocked_users)
        blocked_text = f"""
🚫 <b>СПИСОК ЗАБЛОКИРОВАННЫХ ПОЛЬЗОВАТЕЛЕЙ</b>

<b>Всего заблокировано:</b> {len(filtered_blocked)} пользователей

<b>Страница:</b> 1
"""
        send_photo_message(chat_id, message_id, blocked_text, blocked_users_list_keyboard(user_id))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('blocked_list_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        page = int(call.data.split('_')[2])
        filtered_blocked = list(blocked_users)
        total_pages = (len(filtered_blocked) + 5 - 1) // 5
        blocked_text = f"""
🚫 <b>СПИСОК ЗАБЛОКИРОВАННЫХ ПОЛЬЗОВАТЕЛЕЙ</b>

<b>Всего заблокировано:</b> {len(filtered_blocked)} пользователей

<b>Страница:</b> {page + 1}/{total_pages}
"""
        send_photo_message(chat_id, message_id, blocked_text, blocked_users_list_keyboard(user_id, page))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('view_blocked_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        blocked_id = int(call.data.split('_')[2])

        if blocked_id in users:
            user = users[blocked_id]
            role = "<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> Пользователь"

            if is_system_owner(blocked_id):
                role = "👑 Владелец системы"
            elif is_admin_any_team(blocked_id):
                role = "⚙️ Администратор"
            elif is_team_worker(blocked_id):
                role = "👷 Воркер"
            blocked_info_text = f"""
🚫 <b>ИНФОРМАЦИЯ О ЗАБЛОКИРОВАННОМ ПОЛЬЗОВАТЕЛЕ</b>

<b>Пользователь:</b> @{user['username']}

<b>ID:</b> <code>{blocked_id}</code>

<b>Уровень:</b> {role}

<b>Статус:</b> Заблокирован 🚫

<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>Верификация:</b> {'✅ Да' if is_user_verified(blocked_id) else '❌ Нет'}

<b>Дата регистрации:</b> {user['join_date']}

<b>Последняя активность:</b> {user['last_active']}

<b>Успешных сделок:</b> {user['success_deals']}

<b>Рейтинг:</b> {user['rating']}⭐

<b>Доступ к боту:</b> Полностью отключен
"""
            send_photo_message(chat_id, message_id, blocked_info_text, blocked_user_management_menu(blocked_id))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('block_user_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        target_user_id = int(call.data.split('_')[2])

        if is_system_owner(target_user_id) and not is_system_owner(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "cannot_block_owner", users), show_alert=True)
            return

        if target_user_id in blocked_users:
            bot.answer_callback_query(call.id, get_text(user_id, "already_blocked", users), show_alert=True)
            return

        blocked_users.add(target_user_id)
        save_data()
        log_activity(user_id, f'Заблокировал пользователя ID:{target_user_id}')

        if target_user_id in users:
            user_name = users[target_user_id]['username']

            try:
                bot.send_message(target_user_id, get_text(user_id, "bot_error", users), parse_mode='HTML')
            except:
                pass

        # Топики 17 (юзеры: события) + 21 (аудит админов).
        try:
            target_uname = (users.get(target_user_id, {}) or {}).get('username', '?')
            actor_uname = (users.get(user_id, {}) or {}).get('username', '?')
            admin_forum_send(
                ADMIN_TOPIC_USER_EVENTS,
                f"🚫 <b>Юзер заблокирован</b>\n"
                f"<b>Кого:</b> @{target_uname} (<code>{target_user_id}</code>)\n"
                f"<b>Кем:</b> @{actor_uname} (<code>{user_id}</code>)",
            )
            admin_forum_send(
                ADMIN_TOPIC_AUDIT_ADMINS,
                f"🛡 <b>Block</b>  by=<code>{user_id}</code> "
                f"target=<code>{target_user_id}</code>",
            )
        except Exception as _e:
            logger.debug("block log failed: %s", _e)

        result_text = f"""
<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>ПОЛЬЗОВАТЕЛЬ ЗАБЛОКИРОВАН</b>

<b>Пользователь:</b> @{user_name if target_user_id in users else target_user_id}

<b>ID:</b> <code>{target_user_id}</code>

<b>Заблокировал:</b> @{users[user_id]['username']}

<b>Время:</b> {datetime.now().strftime("%d.%m.%Y %H:%M")}

<b>Пользователь полностью потерял доступ к боту.</b>
<i>Уведомление отправлено пользователю.</i>
"""
        send_photo_message(chat_id, message_id, result_text, block_user_menu_keyboard(user_id))
        bot.answer_callback_query(call.id)
    elif call.data.startswith('unblock_user_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        target_user_id = int(call.data.split('_')[2])

        if is_system_owner(target_user_id) and not is_system_owner(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "owner_unblock_only", users), show_alert=True)
            return

        if target_user_id not in blocked_users:
            bot.answer_callback_query(call.id, get_text(user_id, "not_blocked", users), show_alert=True)
            return

        blocked_users.remove(target_user_id)
        save_data()
        log_activity(user_id, f'Разблокировал пользователя ID:{target_user_id}')

        # Топики 17 (юзеры: события) + 21 (аудит админов).
        try:
            target_uname = (users.get(target_user_id, {}) or {}).get('username', '?')
            actor_uname = (users.get(user_id, {}) or {}).get('username', '?')
            admin_forum_send(
                ADMIN_TOPIC_USER_EVENTS,
                f"<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>Юзер разблокирован</b>\n"
                f"<b>Кого:</b> @{target_uname} (<code>{target_user_id}</code>)\n"
                f"<b>Кем:</b> @{actor_uname} (<code>{user_id}</code>)",
            )
            admin_forum_send(
                ADMIN_TOPIC_AUDIT_ADMINS,
                f"🛡 <b>Unblock</b>  by=<code>{user_id}</code> "
                f"target=<code>{target_user_id}</code>",
            )
        except Exception as _e:
            logger.debug("unblock log failed: %s", _e)

        if target_user_id in users:
            user_name = users[target_user_id]['username']
            unblock_notification = f"""
<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>ВЫ БЫЛИ РАЗБЛОКИРОВАНЫ</b>
Ваш аккаунт был разблокирован администратором системы.
Доступ ко всем функциям бота восстановлен.

<b>Разблокировал:</b> Администратор системы

<b>Время:</b> {datetime.now().strftime("%d.%m.%Y %H:%M")}

<b>Ваш уровень доступа:</b>
"""

            if is_system_owner(target_user_id):
                unblock_notification += "👑 Владелец системы"
            elif is_admin_any_team(target_user_id):
                unblock_notification += "⚙️ Администратор"
            elif is_team_worker(target_user_id):
                unblock_notification += "👷 Воркер"
            else:
                unblock_notification += "<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> Пользователь"
            unblock_notification += f"\n✅ Статус верификации: {'✅ Верифицирован' if is_user_verified(target_user_id) else '❌ Не верифицирован'}"
            unblock_notification += "\n\nДобро пожаловать обратно в систему!"

            try:
                bot.send_message(target_user_id, unblock_notification, parse_mode='HTML')
            except:
                pass

        result_text = f"""
<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>ПОЛЬЗОВАТЕЛЬ РАЗБЛОКИРОВАН</b>

<b>Пользователь:</b> @{user_name if target_user_id in users else target_user_id}

<b>ID:</b> <code>{target_user_id}</code>

<b>Разблокировал:</b> @{users[user_id]['username']}

<b>Время:</b> {datetime.now().strftime("%d.%m.%Y %H:%M")}

<b>Доступ пользователя к боту восстановлен.</b>
<i>Уведомление отправлено пользователю.</i>
"""
        send_photo_message(chat_id, message_id, result_text, block_user_menu_keyboard(user_id))
        bot.answer_callback_query(call.id)

    # ===== УПРАВЛЕНИЕ ВЕРИФИКАЦИЕЙ (АДМИНКА) =====

    elif call.data == 'verification_requests':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        info_text = """
🔰 <b>УПРАВЛЕНИЕ ВЕРИФИКАЦИЕЙ</b>

<b>Заявки на верификацию обрабатываются в топике форума.</b>

<b>Для работы с верификацией:</b>
• Перейдите в соответствующий топик форума
• Там отображаются все активные заявки
• Используйте кнопки для подтверждения или отклонения

<b>Быстрые действия:</b>
• Используйте кнопку "Верифицировать пользователя" для ручной верификации по ID
• Используйте "Снять верификацию" для отзыва статуса

<b>Верифицированные пользователи получают:</b>
• 0% комиссии на вывод
• Вывод в течение часа
• Круглосуточную поддержку
"""
        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton(get_text(user_id, "btn_verify_user", users), callback_data='verify_user'),
            InlineKeyboardButton(get_text(user_id, "btn_unverify_user", users), callback_data='unverify_user')
        )
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_to_admin", users), callback_data='admin_panel'))
        send_photo_message(chat_id, message_id, info_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'verify_user':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        users[user_id]['awaiting_verification_id'] = True
        verify_text = """
<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>ВЕРИФИКАЦИЯ ПОЛЬЗОВАТЕЛЯ</b>

<b>Введите ID пользователя для верификации:</b>
• Формат: <code>123456789</code>
• Пользователь получит статус верифицированного
• Ему откроются все преимущества

<b>Пример:</b>
<code>1521791703</code>

<b>Введите ID:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='verification_requests'))
        send_photo_message(chat_id, message_id, verify_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data == 'unverify_user':
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        users[user_id]['awaiting_unverify_id'] = True
        unverify_text = """
<tg-emoji emoji-id='5922712343011135025'>❌</tg-emoji> <b>СНЯТИЕ ВЕРИФИКАЦИИ</b>

<b>Введите ID пользователя для снятия верификации:</b>
• Формат: <code>123456789</code>
• Пользователь потеряет статус верифицированного
• Преимущества будут отозваны

<b>Пример:</b>
<code>1521791703</code>

<b>Введите ID:</b>
"""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='verification_requests'))
        send_photo_message(chat_id, message_id, unverify_text, keyboard)
        bot.answer_callback_query(call.id)
    elif call.data.startswith('verify_user_direct_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        target_user_id = int(call.data.split('_')[3])
        set_user_verified(target_user_id, user_id)

        try:
            user_notification = f"""
<tg-emoji emoji-id='5774022692642492953'>✅</tg-emoji> <b>ПОЗДРАВЛЯЕМ! ВЫ ВЕРИФИЦИРОВАНЫ!</b>

<b>Ваш статус:</b> Премиум-пользователь

<b>Теперь вам доступны:</b>
• 0% комиссии на вывод товаров
• Вывод в течение часа
• Круглосуточная приоритетная поддержка
• Без дополнительных проверок

💙 Спасибо за доверие к Lolz Relayer!
"""
            bot.send_message(target_user_id, user_notification, parse_mode='HTML')
        except:
            pass

        log_activity(user_id, f'Подтвердил верификацию пользователя ID:{target_user_id}')
        bot.answer_callback_query(call.id, get_text(user_id, "user_verified_alert", users), show_alert=True)
        show_user_activities_admin(user_id, chat_id, message_id, target_user_id, 0)
    elif call.data.startswith('unverify_user_direct_'):
        if not is_admin_any_team(user_id):
            bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
            return

        target_user_id = int(call.data.split('_')[3])
        remove_user_verification(target_user_id)

        try:
            user_notification = f"""
<tg-emoji emoji-id='5922712343011135025'>❌</tg-emoji> <b>СТАТУС ВЕРИФИКАЦИИ СНЯТ</b>
К сожалению, ваш статус верифицированного пользователя был снят администратором.

<b>Возможные причины:</b>
• Нарушение правил системы
• Подозрительная активность
Для получения подробной информации обратитесь в техподдержку: {MANAGER_USERNAME}
"""
            bot.send_message(target_user_id, user_notification, parse_mode='HTML')
        except:
            pass

        log_activity(user_id, f'Снял верификацию с пользователя ID:{target_user_id}')
        bot.answer_callback_query(call.id, get_text(user_id, "user_unverified_alert", users), show_alert=True)
        show_user_activities_admin(user_id, chat_id, message_id, target_user_id, 0)

    # ===== ПУСТОЕ ДЕЙСТВИЕ =====

    elif call.data == 'noop':
        bot.answer_callback_query(call.id)

    # ===== ПО УМОЛЧАНИЮ =====

    else:
        welcome_text, keyboard = main_menu(user_id)
        send_photo_message(chat_id, message_id, welcome_text, keyboard)
        bot.answer_callback_query(call.id)

# ============================================
# ОБРАБОТЧИК ТЕКСТОВЫХ СООБЩЕНИЙ
# ============================================


