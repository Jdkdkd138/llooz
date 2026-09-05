# handlers/appeals.py
"""Система обращений: appeals_menu, suggest, complain, admin reply/close, admin appeals list."""

from bot_core import *
from bot_ui import *
from bot_lang import get_text

# ──────────────────────────────────────────────
# ХРАНИЛИЩЕ ОБРАЩЕНИЙ (в памяти, сохраняется в lolz_data через appeals_data)
# ──────────────────────────────────────────────

if 'appeals_data' not in dir():
    appeals_data = {}  # будет загружено из bot_core

def _get_appeals():
    """Возвращает список обращений из глобального хранилища."""
    if not hasattr(save_data, '__self__'):
        pass
    return appeals_storage

# Инициализируем хранилище если нет
def _init_appeals_storage():
    global appeals_storage
    if 'appeals_storage' not in globals():
        appeals_storage = []
    return appeals_storage

_init_appeals_storage()


def _appeals_keyboard(user_id):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(PremiumButton(get_text(user_id, 'btn_appeals_suggest', users), '✍️', '5956561916573782596', callback_data='appeal_suggest'))
    kb.add(PremiumButton(get_text(user_id, 'btn_appeals_complain', users), '🚫', '5922712343011135025', callback_data='appeal_complain'))
    kb.add(PremiumButton(get_text(user_id, 'btn_back_menu', users), '🔜', '5893368370530621889', callback_data='main_menu'))
    return kb


def _appeals_menu_text(user_id):
    from bot_core import BOT_NAME
    return (
        f'<tg-emoji emoji-id="5956561916573782596">📄</tg-emoji> <b>Центр обращений {BOT_NAME}</b>\n\n'
        f'<tg-emoji emoji-id="5931546553868095844">⚙️</tg-emoji> <b>Раздел предложений и идей:</b>\n'
        f'• Предложения по улучшению функционала\n'
        f'• Идеи для новых функций\n'
        f'• Запросы на интеграции\n'
        f'• Отзывы о пользовательском опыте\n\n'
        f'<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>Раздел жалоб и претензий:</b>\n'
        f'• Жалобы на пользователей\n'
        f'• Проблемы со сделками\n'
        f'• Технические проблемы\n'
        f'• Некорректное поведение\n'
        f'• Предполагаемое мошенничество\n\n'
        f'<tg-emoji emoji-id="5904258298764334001">📞</tg-emoji> <b>Важная информация:</b>\n'
        f'• Все обращения рассматриваются в течение 24 часов\n'
        f'• Конфиденциальность гарантируется\n'
        f'• По жалобам на мошенничество — моментальная реакция\n'
        f'• Лучшие предложения внедряются в бота\n\n'
        f'<tg-emoji emoji-id="5811989245761426317">💡</tg-emoji> Выберите раздел для обращения:'
    )


@bot.callback_query_handler(func=lambda call: call.data == 'appeals_menu')
def handle_appeals_menu(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    update_user_activity(user_id)
    send_photo_message(chat_id, message_id, _appeals_menu_text(user_id), _appeals_keyboard(user_id))
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == 'appeal_suggest')
def handle_appeal_suggest(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    users[user_id]['awaiting_appeal_type'] = 'suggest'
    text = (
        '<tg-emoji emoji-id="5934504443772756682">✍️</tg-emoji> <b>Напишите ваше предложение:</b>\n\n'
        '<tg-emoji emoji-id="5893193062850499428">ℹ️</tg-emoji> Опишите подробно вашу идею, как она улучшит работу бота и какие преимущества принесет пользователям.'
    )
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(PremiumButton(get_text(user_id, 'btn_back_menu', users), '🔜', '5893368370530621889', callback_data='main_menu'))
    send_photo_message(chat_id, message_id, text, kb)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == 'appeal_complain')
def handle_appeal_complain(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    init_user(user_id)
    users[user_id]['awaiting_appeal_type'] = 'complain'
    text = (
        '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> <b>Напишите вашу жалобу:</b>\n\n'
        '<tg-emoji emoji-id="5893193062850499428">ℹ️</tg-emoji> Укажите:\n'
        '• ID пользователя/сделки\n'
        '• Суть проблемы\n'
        '• Скриншоты (если есть)\n'
        '• Желаемое решение'
    )
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(PremiumButton(get_text(user_id, 'btn_back_menu', users), '🔜', '5893368370530621889', callback_data='main_menu'))
    send_photo_message(chat_id, message_id, text, kb)
    bot.answer_callback_query(call.id)


# ──────────────────────────────────────────────
# ОБРАБОТКА ОТВЕТА АДМИНА
# ──────────────────────────────────────────────

@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('appeal_reply_'))
def handle_appeal_reply(call):
    user_id = call.from_user.id
    if not (is_admin_own_team(user_id) or is_system_owner(user_id)):
        bot.answer_callback_query(call.id, 'Нет доступа', show_alert=True)
        return
    appeal_id = call.data.replace('appeal_reply_', '')
    users[user_id]['awaiting_appeal_reply'] = appeal_id
    bot.send_message(user_id,
        '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Напишите ответ пользователю:</b>',
        parse_mode='HTML')
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('appeal_close_'))
def handle_appeal_close(call):
    user_id = call.from_user.id
    if not (is_admin_own_team(user_id) or is_system_owner(user_id)):
        bot.answer_callback_query(call.id, 'Нет доступа', show_alert=True)
        return
    appeal_id = call.data.replace('appeal_close_', '')
    for ap in appeals_storage:
        if ap['id'] == appeal_id:
            ap['closed'] = True
            break
    save_data()
    bot.answer_callback_query(call.id, '✅ Обращение закрыто', show_alert=True)
    try:
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    except Exception:
        pass


# ──────────────────────────────────────────────
# ПРОСМОТР ОБРАЩЕНИЙ В АДМИНКЕ
# ──────────────────────────────────────────────

@bot.callback_query_handler(func=lambda call: call.data == 'admin_appeals')
def handle_admin_appeals(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if not (is_admin_own_team(user_id) or is_system_owner(user_id)):
        bot.answer_callback_query(call.id, 'Нет доступа', show_alert=True)
        return
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(PremiumButton(get_text(user_id, 'btn_appeals_suggestions', users), '💡', '5811989245761426317', callback_data='admin_appeals_type_suggest_0'))
    kb.add(PremiumButton(get_text(user_id, 'btn_appeals_complaints', users), '🚫', '5922712343011135025', callback_data='admin_appeals_type_complain_0'))
    kb.add(PremiumButton(get_text(user_id, 'btn_admin_panel', users), '🔙', '5904258298764334001', callback_data='admin_panel'))
    send_photo_message(chat_id, message_id,
        '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Жалобы и предложения</b>\n\nВыберите тип:', kb)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data and call.data.startswith('admin_appeals_type_'))
def handle_admin_appeals_list(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if not (is_admin_own_team(user_id) or is_system_owner(user_id)):
        bot.answer_callback_query(call.id)
        return

    # format: admin_appeals_type_{type}_{index}
    parts = call.data.split('_')
    ap_type = parts[3]   # suggest or complain
    try:
        idx = int(parts[4])
    except (IndexError, ValueError):
        idx = 0

    filtered = [a for a in appeals_storage if a['type'] == ap_type and not a.get('closed')]
    total = len(filtered)

    if total == 0:
        bot.answer_callback_query(call.id, '📭 Обращений нет', show_alert=True)
        return

    idx = max(0, min(idx, total - 1))
    ap = filtered[idx]
    username = ap.get('username', '-')
    type_label = 'Предложение' if ap_type == 'suggest' else 'Жалоба'
    text = (
        f'<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Тип:</b> {type_label}\n'
        f'<tg-emoji emoji-id="5886412370347036129">👤</tg-emoji> <b>Пользователь:</b> @{username}\n\n'
        f'{ap["text"]}'
    )

    kb = InlineKeyboardMarkup(row_width=3)
    prev_idx = max(0, idx - 1)
    next_idx = min(total - 1, idx + 1)
    kb.row(
        InlineKeyboardButton('◀️', callback_data=f'admin_appeals_type_{ap_type}_{prev_idx}'),
        InlineKeyboardButton(f'{idx+1}/{total}', callback_data='noop'),
        InlineKeyboardButton('▶️', callback_data=f'admin_appeals_type_{ap_type}_{next_idx}')
    )
    kb.row(
        PremiumButton(get_text(user_id, 'btn_appeal_reply', users), '✍️', '5956561916573782596', callback_data=f'appeal_reply_{ap["id"]}'),
        PremiumButton(get_text(user_id, 'btn_appeal_close', users), '✅', '5920052658743283381', callback_data=f'appeal_close_{ap["id"]}')
    )
    kb.add(PremiumButton(get_text(user_id, 'btn_admin_panel', users), '🔙', '5904258298764334001', callback_data='admin_panel'))

    send_photo_message(chat_id, message_id, text, kb)
    bot.answer_callback_query(call.id)
