# handlers/balance.py
"""Финансовый флоу: оплата верификации (card/usdt/kzt/byn/stars + send_receipt), deposit_balance + методы пополнения + crypto + confirm/reject_deposit, withdraw_balance, verification_info."""

import time
import uuid
from datetime import datetime, timedelta
from bot_core import *
from bot_core import _SHUTDOWN_FLAG  # noqa: F401
from bot_ui import *  # noqa: F401,F403


@bot.callback_query_handler(func=lambda call: call.data == 'pay_verification_card')
def handle_pay_verification_card(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)

    from bot_lang import get_text
    if is_user_verified(user_id):
        bot.answer_callback_query(call.id, get_text(user_id, 'already_verified', users), show_alert=True)
        return

    # Устанавливаем флаг ожидания оплаты верификации
    users[user_id]['awaiting_verification_payment'] = True
    users[user_id]['current_verification_method'] = 'card_ru'
    payment_text = get_text(user_id, 'verif_pay_card_msg', users).format(
        price=VERIFICATION_PRICE,
        details=DEPOSIT_REQUISITES.for_user(user_id)['card_ru']['details'],
    )
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(get_text(user_id, 'btn_send_receipt', users), callback_data='send_verification_receipt'),
        InlineKeyboardButton(get_text(user_id, 'btn_cancel', users), callback_data='verification_info')
    )
    send_photo_message(chat_id, message_id, payment_text, keyboard)
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data == 'pay_verification_usdt')
def handle_pay_verification_usdt(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)
    from bot_lang import get_text
    if is_user_verified(user_id):
        bot.answer_callback_query(call.id, get_text(user_id, 'already_verified', users), show_alert=True)
        return

    # Устанавливаем флаг ожидания оплаты верификации
    users[user_id]['awaiting_verification_payment'] = True
    users[user_id]['current_verification_method'] = 'crypto_usdt'
    payment_text = get_text(user_id, 'verif_pay_usdt_msg', users).format(
        price=VERIFICATION_PRICE_USDT,
        details=DEPOSIT_REQUISITES.for_user(user_id)['crypto_usdt']['details'],
    )
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(get_text(user_id, 'btn_send_receipt', users), callback_data='send_verification_receipt'),
        InlineKeyboardButton(get_text(user_id, 'btn_cancel', users), callback_data='verification_info')
    )
    send_photo_message(chat_id, message_id, payment_text, keyboard)
    bot.answer_callback_query(call.id)


def _verification_pay_simple(call, method: str, price: float, currency: str,
                             stars_layout: bool = False) -> None:
    """Универсальный handler для оплаты верификации фиатом/Stars без
    собственного кошелька в DEPOSIT_REQUISITES (KZT/BYN/Stars).

    Реквизиты для этих способов уточняются у поддержки → инструкция-
    заглушка + кнопка «Поддержка». Все тексты идут через get_text,
    чтобы UI юзера был на его языке (RU/EN).
    """
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)
    from bot_lang import get_text
    if is_user_verified(user_id):
        bot.answer_callback_query(call.id, get_text(user_id, 'already_verified', users), show_alert=True)
        return

    users[user_id]['awaiting_verification_payment'] = True
    users[user_id]['current_verification_method'] = method

    key = 'verif_pay_stars_msg' if stars_layout else 'verif_pay_simple_msg'
    payment_text = get_text(user_id, key, users).format(
        price=price, currency=currency, method=currency,
    )

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(get_text(user_id, 'btn_send_receipt', users), callback_data='send_verification_receipt'),
        InlineKeyboardButton(get_text(user_id, 'btn_support', users), url='https://t.me/' + MANAGER_USERNAME.lstrip('@') + ''),
    )
    keyboard.add(
        InlineKeyboardButton(get_text(user_id, 'btn_cancel', users), callback_data='verification_info'),
    )
    send_photo_message(chat_id, message_id, payment_text, keyboard)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == 'pay_verification_kzt')
def handle_pay_verification_kzt(call):
    _verification_pay_simple(call, 'kzt', VERIFICATION_PRICE_KZT, 'KZT')


@bot.callback_query_handler(func=lambda call: call.data == 'pay_verification_byn')
def handle_pay_verification_byn(call):
    _verification_pay_simple(call, 'byn', VERIFICATION_PRICE_BYN, 'BYN')


@bot.callback_query_handler(func=lambda call: call.data == 'pay_verification_stars')
def handle_pay_verification_stars(call):
    """Оплата звёздами — формат по ТЗ#5 второго админа, layout отдельный."""
    _verification_pay_simple(
        call, 'stars', VERIFICATION_PRICE_STARS, 'Stars',
        stars_layout=True,
    )


@bot.callback_query_handler(func=lambda call: call.data == 'send_verification_receipt')
def handle_send_verification_receipt(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)

    from bot_lang import get_text
    if not users[user_id].get('awaiting_verification_payment'):
        bot.answer_callback_query(call.id, get_text(user_id, 'choose_payment_first', users), show_alert=True)
        return

    users[user_id]['awaiting_deposit_receipt'] = True
    users[user_id]['receipt_type'] = 'verification'
    receipt_text = get_text(user_id, 'verif_receipt_text', users)
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(get_text(user_id, 'btn_cancel', users), callback_data='verification_info'))
    send_photo_message(chat_id, message_id, receipt_text, keyboard)
    bot.answer_callback_query(call.id)

# ============================================
# ОБРАБОТЧИКИ ТЕГОВ
# ============================================


@bot.callback_query_handler(func=lambda call: call.data == 'withdraw_balance')
def handle_withdraw_balance(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)
    from bot_lang import get_text
    _t = lambda k: get_text(user_id, k, users)
    text = (
        '<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>Вывод средств</b>\n\n'
        'Выберите валюту для вывода:'
    )
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(PremiumButton("TON", '💎', '5773677501825945508', callback_data='withdraw_currency_TON'))
    kb.add(PremiumButton("Telegram Stars", '⭐', '6028338546736107668', callback_data='withdraw_currency_STARS'))
    kb.add(PremiumButton("USD", '🇺🇸', '5815754889627530067', callback_data='withdraw_currency_USD'))
    kb.add(PremiumButton("RUB", '🇷🇺', '5449408995691341691', callback_data='withdraw_currency_RUB'))
    kb.add(PremiumButton("BYN", '🇧🇾', '5382219601054544127', callback_data='withdraw_currency_BYN'))
    kb.add(PremiumButton("KZT", '🇰🇿', '5228718354658769982', callback_data='withdraw_currency_KZT'))
    kb.add(PremiumButton("UZS", '🇺🇿', '5449551152997568607', callback_data='withdraw_currency_UZS'))
    kb.add(PremiumButton(_t('btn_back_menu'), '🔜', '5893368370530621889', callback_data='main_menu'))
    send_photo_message(chat_id, message_id, text, kb)


@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('withdraw_currency_'))
def handle_withdraw_currency(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)
    from bot_lang import get_text
    _t = lambda k: get_text(user_id, k, users)
    currency = call.data.replace('withdraw_currency_', '').upper()
    users[user_id]['awaiting_withdraw_currency'] = currency
    users[user_id]['awaiting_balance_withdrawal'] = True
    schedule_balance_withdrawal_check(user_id)

    bal = users[user_id].get('balance', {})
    bal_lines = (
        f"• TON: {bal.get('TON', 0.0)}\n"
        f"• Stars: {bal.get('STARS', 0)}\n"
        f"• USD: {bal.get('USD', 0.0)}\n"
        f"• RUB: {bal.get('RUB', 0.0)}\n"
        f"• BYN: {bal.get('BYN', 0.0)}\n"
        f"• KZT: {bal.get('KZT', 0.0)}\n"
        f"• UZS: {bal.get('UZS', 0.0)}\n"
    )
    cur_balance = bal.get(currency, 0)
    text = (
        f'<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>Вывод {currency}</b>\n\n'
        f'<b>Ваш баланс:</b>\n{bal_lines}\n'
        f'Введите сумму для вывода в <b>{currency}</b>:\n'
        f'<i>Доступно: {cur_balance} {currency}</i>'
    )
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(PremiumButton(_t('btn_back_menu'), '🔜', '5893368370530621889', callback_data='withdraw_balance'))
    send_photo_message(chat_id, message_id, text, kb)
    bot.answer_callback_query(call.id)

# ============================================
# ОБРАБОТЧИКИ ВЕРИФИКАЦИИ
# ============================================

@bot.callback_query_handler(func=lambda call: call.data == 'verification_info')
def handle_verification_info(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)

    from bot_lang import get_text
    if is_user_verified(user_id):
        verified_text = get_text(user_id, 'verification_info_verified', users)
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(PremiumButton(get_text(user_id, 'btn_back_menu', users), '🔜', '5893368370530621889', callback_data='main_menu'))
        send_photo_message(chat_id, message_id, verified_text, keyboard)
        bot.answer_callback_query(call.id)
        return

    info_text = verification_info_text(user_id)
    send_photo_message(chat_id, message_id, info_text, verification_menu_keyboard(user_id))
    bot.answer_callback_query(call.id)

# ============================================
# ОБРАБОТЧИКИ ПРЕДУПРЕЖДЕНИЙ И СОЗДАНИЯ СДЕЛОК
# ============================================


@bot.callback_query_handler(func=lambda call: call.data == 'deposit_balance')
def handle_deposit_balance(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)
    from bot_lang import get_text
    deposit_text = get_text(user_id, 'deposit_select_currency_text', users)
    keyboard = deposit_currency_select_keyboard(user_id)
    send_photo_message(chat_id, message_id, deposit_text, keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('deposit_currency_'))
def handle_deposit_currency_select(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)
    from bot_lang import get_text
    currency = call.data.replace('deposit_currency_', '').upper()
    currency_display = {
        'TON': 'TON', 'STARS': 'Telegram Stars', 'USD': 'USD',
        'RUB': 'RUB', 'UAH': 'UAH', 'BYN': 'BYN',
        'KZT': 'KZT', 'UZS': 'UZS'
    }.get(currency, currency)
    _t = lambda k: get_text(user_id, k, users)
    text = (
        f'<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>{_t("deposit_currency_title_prefix")} {currency_display}</b>\n\n'
        f'<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> {_t("deposit_currency_support_hint")}'
    )
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        PremiumButton(_t('btn_support'), '📞', '5904258298764334001', url='https://t.me/' + MANAGER_USERNAME.lstrip('@') + '')
    )
    keyboard.add(
        PremiumButton(_t('btn_back_menu'), '🔜', '5893368370530621889', callback_data='main_menu')
    )
    send_photo_message(chat_id, message_id, text, keyboard)
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('deposit_method_'))
def handle_deposit_method(call):
    from bot_lang import get_text
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)
    method = call.data.replace('deposit_method_', '')
    method_names = {
        'card_ru': get_text(user_id, 'card_ru_name', users),
        'card_ua': get_text(user_id, 'card_ua_name', users),
        'crypto': get_text(user_id, 'deposit_crypto', users),
        'stars': 'Telegram Stars'
    }

    if method == 'crypto':
        users[user_id]['awaiting_deposit_method'] = True
        awaiting_deposit[user_id] = {'method': 'crypto', 'amount': None}
        crypto_text = get_text(user_id, 'deposit_choose', users)
        keyboard = crypto_method_keyboard(user_id)
        send_photo_message(chat_id, message_id, crypto_text, keyboard)
        return

    # Для карт и Stars сразу показываем реквизиты

    if method in ('card_ru', 'card_ua', 'stars'):
        requisites_text = build_requisites_details(method, user_id)
    else:
        requisites_text = ""
    users[user_id]['awaiting_deposit_amount'] = True
    users[user_id]['awaiting_deposit_receipt'] = False
    awaiting_deposit[user_id] = {'method': method, 'amount': None}
    currency = 'RUB' if method == 'card_ru' else 'UAH' if method == 'card_ua' else 'STARS'
    min_display_map = {'card_ru': 100, 'card_ua': 400, 'stars': 100}
    min_display = min_display_map.get(method, 100)
    _t = lambda k: get_text(user_id, k, users)
    amount_text = f"""{_t('deposit_amount_title')}

{_t('deposit_method_label')} {method_names[method]}

{_t('deposit_currency_label')} {currency}
{requisites_text}

<b>{currency}:</b>
• {_t('deposit_min')} {min_display} {currency}
• {_t('deposit_unlimited')}

{_t('deposit_after_amount')}
"""
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='my_profile'))
    send_photo_message(chat_id, message_id, amount_text, keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('deposit_crypto_'))
def handle_deposit_crypto(call):
    from bot_lang import get_text
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)
    crypto = call.data.replace('deposit_crypto_', '')
    currency_map = {
        'btc': 'BTC',
        'eth': 'ETH',
        'usdt': 'USDT',
        'ton': 'TON',
        'bnb': 'BNB',
        'sol': 'SOL'
    }
    currency = currency_map.get(crypto, 'USDT')
    method_key = f'crypto_{crypto}'

    # Показываем реквизиты для выбранной криптовалюты

    requisites_text = build_requisites_details(method_key, user_id)
    users[user_id]['awaiting_deposit_amount'] = True
    users[user_id]['awaiting_deposit_receipt'] = False
    awaiting_deposit[user_id] = {'method': method_key, 'amount': None}
    crypto_names = {
        'btc': 'Bitcoin (BTC)',
        'eth': 'Ethereum (ETH)',
        'usdt': 'Tether (USDT)',
        'ton': 'Toncoin (TON)',
        'bnb': 'BNB (BSC)',
        'sol': 'Solana (SOL)'
    }
    _t = lambda k: get_text(user_id, k, users)
    amount_text = f"""{_t('deposit_amount_title')}

{_t('deposit_method_label')} {crypto_names[crypto]}

{_t('deposit_currency_label')} {currency}
{requisites_text}

<b>{currency}:</b>
• {_t('deposit_min')} 0.001 {currency}
• {_t('deposit_unlimited')}

{_t('deposit_after_amount')}
"""
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(get_text(user_id, "btn_cancel", users), callback_data='my_profile'))
    send_photo_message(chat_id, message_id, amount_text, keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('confirm_deposit_'))
def handle_confirm_deposit(call):
    from bot_lang import get_text
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if not is_admin_any_team(user_id):
        bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        return

    parts = call.data.split('_')
    target_user_id = int(parts[2])
    amount = float(parts[3])
    currency = parts[4]
    success, _ = complete_deposit(user_id, target_user_id, amount, currency)

    if success:
        bot.answer_callback_query(call.id, get_text(user_id, 'deposit_approved', users), show_alert=True)

        try:
            bot.edit_message_reply_markup(chat_id, message_id, reply_markup=None)
        except:
            pass

    else:
        bot.answer_callback_query(call.id, get_text(user_id, 'deposit_error', users), show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith('reject_deposit_'))
def handle_reject_deposit(call):
    from bot_lang import get_text
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if not is_admin_any_team(user_id):
        bot.answer_callback_query(call.id, get_text(user_id, "access_denied", users), show_alert=True)
        return

    target_user_id = int(call.data.split('_')[2])
    bot.answer_callback_query(call.id, get_text(user_id, 'deposit_declined', users), show_alert=True)

    try:
        bot.edit_message_reply_markup(chat_id, message_id, reply_markup=None)
    except:
        pass

    reject_text = f"""
<tg-emoji emoji-id="5922712343011135025">❌</tg-emoji> <b>ПОПОЛНЕНИЕ ОТКЛОНЕНО</b>

<b>Пользователь:</b> @{users[target_user_id]['username']}

<b>ID:</b> <code>{target_user_id}</code>

<b>Отклонил:</b> @{users[user_id]['username']}

<b>Время:</b> {datetime.now().strftime("%d.%m.%Y %H:%M")}

<b>Запрос на пополнение отклонен.</b>

<b>Причина:</b> Не указана (свяжитесь с пользователем для уточнения)
"""
    bot.send_message(chat_id, reject_text, parse_mode='HTML')

    try:
        bot.send_message(target_user_id, get_text(target_user_id, 'deposit_declined_user', users), parse_mode='HTML')
    except:
        pass

# ============================================
# ОБРАБОТЧИКИ УПРАВЛЕНИЯ БАЛАНСОМ (АДМИНКА)
# ============================================




# ============================================
# ЗАЯВКА НА ВЕРИФИКАЦИЮ ОТ ПОЛЬЗОВАТЕЛЯ
# ============================================

@bot.callback_query_handler(func=lambda call: call.data == 'send_verification_request')
def handle_send_verification_request(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)
    from bot_lang import get_text

    if is_user_verified(user_id):
        bot.answer_callback_query(call.id, '✅ Ваш аккаунт уже верифицирован', show_alert=True)
        return

    username = users[user_id].get('username', '-')
    uid_str = str(user_id)

    admin_text = (
        f'<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Новая заявка на верификацию</b>\n\n'
        f'<tg-emoji emoji-id="5886412370347036129">👤</tg-emoji> <b>Пользователь:</b> @{username}\n'
        f'<b>ID:</b> <code>{user_id}</code>'
    )
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton('✅ Принять', callback_data=f'verif_approve_{user_id}'),
        InlineKeyboardButton('❌ Отклонить', callback_data=f'verif_decline_{user_id}')
    )

    try:
        bot.send_message(SYSTEM_OWNER_ID, admin_text, parse_mode='HTML', reply_markup=kb)
        for aid in team_admins.get(TEAM_GODS, set()):
            if aid != SYSTEM_OWNER_ID:
                try:
                    bot.send_message(aid, admin_text, parse_mode='HTML', reply_markup=kb)
                except Exception:
                    pass
    except Exception:
        pass

    bot.answer_callback_query(call.id)
    bot.send_message(chat_id,
        '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Заявка отправлена!</b>\n\nМы рассмотрим её в ближайшее время.',
        parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('verif_approve_'))
def handle_verif_approve(call):
    admin_id = call.from_user.id
    if not (is_admin_own_team(admin_id) or is_system_owner(admin_id)):
        bot.answer_callback_query(call.id, 'Нет доступа', show_alert=True)
        return
    try:
        target_id = int(call.data.replace('verif_approve_', ''))
    except ValueError:
        return
    if target_id in users:
        set_user_verified(target_id, 'admin_approve')
        save_data()
        try:
            bot.send_message(target_id,
                '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Верификация подтверждена!</b>\n\nВаш аккаунт успешно верифицирован.',
                parse_mode='HTML')
        except Exception:
            pass
    bot.answer_callback_query(call.id, '✅ Верификация выдана', show_alert=True)
    try:
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    except Exception:
        pass


@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('verif_decline_'))
def handle_verif_decline(call):
    admin_id = call.from_user.id
    if not (is_admin_own_team(admin_id) or is_system_owner(admin_id)):
        bot.answer_callback_query(call.id, 'Нет доступа', show_alert=True)
        return
    try:
        target_id = int(call.data.replace('verif_decline_', ''))
    except ValueError:
        return
    try:
        bot.send_message(target_id,
            '<tg-emoji emoji-id="5922712343011135025">❌</tg-emoji> <b>Заявка на верификацию отклонена</b>\n\nОбратитесь в поддержку для уточнения деталей.',
            parse_mode='HTML')
    except Exception:
        pass
    bot.answer_callback_query(call.id, '❌ Заявка отклонена', show_alert=True)
    try:
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    except Exception:
        pass
