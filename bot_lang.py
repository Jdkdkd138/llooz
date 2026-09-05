# bot_lang.py - Система локализации

TEXTS = {
    'ru': {
        'welcome': """<b><tg-emoji emoji-id="5893255507380014983">💼</tg-emoji> Добро пожаловать в {BOT_NAME} Relayer <tg-emoji emoji-id="5357080225463149588">🤝</tg-emoji></b>

<blockquote><i><tg-emoji emoji-id="5456140674028019486">⚡️</tg-emoji> Ваш надёжный P2P-гарант:</i>
	<tg-emoji emoji-id="5794182096603847292">1⃣</tg-emoji> <tg-emoji emoji-id="5967389567781703494">💼</tg-emoji> Автоматические сделки с NFT и подарками
	<tg-emoji emoji-id="5794303034292968945">2⃣</tg-emoji> <tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Полная защита обеих сторон
	<tg-emoji emoji-id="5794031944547178894">3⃣</tg-emoji> <tg-emoji emoji-id="6039802097916974085">🪙</tg-emoji> Огромный функционал бота и сайта
	<tg-emoji emoji-id="5793901252987330401">4⃣</tg-emoji> <tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> Передача товаров через менеджера: {MANAGER_USERNAME}</blockquote>
    
<tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji> Выберите действие ниже <tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji>""",

        'verified_status': '\n<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Статус:</b> Верифицированный пользователь',

        # Кнопки главного меню
        'btn_create_deal': 'Создать сделку',
        'btn_my_profile': 'Мой профиль',
        'btn_balance_req': 'Баланс и реквизиты',
        'btn_verification': 'Верификация',
        'btn_verification_done': 'Верификация',
        'btn_referrals': 'Рефералы',
        'btn_change_lang': '🌐 Сменить язык',
        'btn_my_tag': 'Мой тег',
        'btn_worker_panel': 'Воркер панель',
        'btn_admin_panel': 'Админ панель',
        'btn_admin_commands': 'Команды админов',
        'btn_support': 'Поддержка',
        'btn_verification_request': 'Заявка на верификацию',
        'btn_appeals': 'Обращения',
        'appeals_menu_text': """<tg-emoji emoji-id="5956561916573782596">📄</tg-emoji> <b>Центр обращений {bot_name}</b>

<tg-emoji emoji-id="5931546553868095844">⚙️</tg-emoji> <b>Раздел предложений и идей:</b>
• Предложения по улучшению функционала
• Идеи для новых функций
• Запросы на интеграции
• Отзывы о пользовательском опыте

<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>Раздел жалоб и претензий:</b>
• Жалобы на пользователей
• Проблемы со сделками
• Технические проблемы
• Некорректное поведение
• Предполагаемое мошенничество

<tg-emoji emoji-id="5904258298764334001">📞</tg-emoji> <b>Важная информация:</b>
• Все обращения рассматриваются в течение 24 часов
• Конфиденциальность гарантируется
• По жалобам на мошенничество — моментальная реакция
• Лучшие предложения внедряются в бота

<tg-emoji emoji-id="5811989245761426317">💡</tg-emoji> Выберите раздел для обращения:""",
        'appeal_suggest_text': """<tg-emoji emoji-id="5934504443772756682">✍️</tg-emoji> <b>Напишите ваше предложение:</b>

<tg-emoji emoji-id="5893193062850499428">ℹ️</tg-emoji> Опишите подробно вашу идею, как она улучшит работу бота и какие преимущества принесет пользователям.""",
        'appeal_complain_text': """<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> <b>Напишите вашу жалобу:</b>

<tg-emoji emoji-id="5893193062850499428">ℹ️</tg-emoji> Укажите:
• ID пользователя/сделки
• Суть проблемы
• Скриншоты (если есть)
• Желаемое решение""",
        'withdraw_menu_text': """<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>Вывод средств</b>

Выберите валюту для вывода:""",
        'withdraw_currency_text': """<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>Вывод {currency}</b>

<b>Ваш баланс:</b>
{bal_lines}
Введите сумму для вывода в <b>{currency}</b>:
<i>Доступно: {cur_balance} {currency}</i>""",
        'verification_request_sent': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Заявка отправлена!</b>\n\nМы рассмотрим её в ближайшее время.',
        'btn_appeals_suggest': 'Предложить',
        'btn_appeals_complain': 'Пожаловаться',
        'btn_admin_appeals': 'Жалобы и предложения',
        'btn_appeals_suggestions': 'Предложения',
        'btn_appeals_complaints': 'Жалобы',
        'btn_appeal_reply': 'Ответить',
        'btn_appeal_close': 'Завершить',
        'btn_my_mammoths': 'Мои мамонты',
        'btn_back_menu': 'В меню',
        'btn_back': 'Назад',
        'btn_refresh': 'Обновить',
        'btn_my_deals': 'Мои сделки',
        'btn_cancel': 'Отмена',
        'btn_send_receipt': 'Отправить чек',
        'btn_confirm_withdraw': 'Подтвердить вывод',
        'btn_withdraw_item': 'Вывести товар',
        'btn_all_deals': 'Все сделки',
        'btn_to_admin': 'В админку',
        'btn_new_deal': 'Новая сделка',

        # Реквизиты
        'bind_requisites': """<tg-emoji emoji-id="5332455502917949981">🏦</tg-emoji> <b>Привязка реквизитов:</b>
<tg-emoji emoji-id="5447644880824181073">⚠️</tg-emoji> <b>Для создания сделки необходимо привязать хотя бы одни реквизиты!
Укажите реквизиты для получения платежей:</b>
<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> Ton — для получения ton
<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> Карта — для получения рублей и других валют
<tg-emoji emoji-id="5343777479091831702">👛</tg-emoji> Usdt — для получения стейблкоинов
<tg-emoji emoji-id="5330319637156479518">📱</tg-emoji> Телефон — для Qiwi/юmoney
<tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji> <b>Выберите тип реквизитов</b> <tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji>""",

        'no_requisites_alert': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Для создания сделки необходимо привязать хотя бы одни реквизиты!',
        'blocked_alert': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> Вы заблокированы и не можете создавать сделки',

        # Создание сделки
        'create_deal_title': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> <b>СОЗДАНИЕ НОВОЙ СДЕЛКИ</b>',
        'create_deal_text': """<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> Создание новой сделки:
ВАЖНО: ЭТО ИЗМЕНЕНИЕ ТОЛЬКО ЕСЛИ ПРИ ВЫБОРЕ РОЛИ ВЫБРАТЬ "ПОКУПАТЕЛЬ"
Выберите валюту для оплаты:""",

        'create_deal_text_seller': """<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> Создание новой сделки:
Выберите валюту для получения оплаты:""",

        # Профиты
        'profit_new': '<tg-emoji emoji-id="6039802097916974085">🪙</tg-emoji> <b>НОВЫЙ ПРОФИТ!</b>',
        'profit_type': '<tg-emoji emoji-id="5197371802136892976">⛏</tg-emoji> <b>Тип:</b>',
        'profit_amount': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> <b>Сумма:</b>',
        'profit_desc': '<tg-emoji emoji-id="5197269100878907942">✍️</tg-emoji> <b>Описание:</b>',
        'profit_deal': '<tg-emoji emoji-id="5195033767969839232">🚀</tg-emoji> <b>Сделка:</b>',
        'profit_success': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Успешная мамонтизация!</b>',
        'profit_direct_transfer': 'Прямой перевод',

        # Язык
        'lang_select': '🌐 Выберите язык / Select language / 选择语言 / اختر اللغة:',
        'lang_ru': '<tg-emoji emoji-id="5449408995691341691">🇷🇺</tg-emoji> Русский',
        'lang_en': '🇬🇧 English',
        'lang_zh': '🇨🇳 中文',
        'lang_ar': '🇸🇦 عربي',

        # Алерты
        'already_verified': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Вы уже верифицированы!',
        'access_denied': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Доступ запрещён',
        'deal_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Сделка не найдена',
        'deal_already_paid': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Сделка уже оплачена или завершена',
        'deal_not_paid': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Сделка еще не оплачена',
        'deal_no_buyer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> В сделке нет покупателя',
        'not_buyer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Вы не являетесь покупателем в этой сделке',
        'not_seller': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Вы не являетесь продавцом в этой сделке',
        'insufficient_funds': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Недостаточно средств на балансе',
        'tag_workers_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Установка тега доступна только воркерам и администраторам',
        'no_tag_set': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> У вас не установлен тег',
        'workers_admins_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Доступно только воркерам и администраторам',
        'choose_payment_first': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Сначала выберите способ оплаты верификации',
        'payment_confirmed': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Оплата подтверждена, профит отправлен',
        'user_not_found': 'Пользователь не найден',

        # Верификация
        'verification_receipt_title': '📤 <b>ОТПРАВКА ЧЕКА НА ВЕРИФИКАЦИЮ</b>',
        'verification_receipt_text': """📤 <b>ОТПРАВКА ЧЕКА НА ВЕРИФИКАЦИЮ</b>

<b>Отправьте фото или документ с подтверждением перевода.</b>

<b>Требования к чеку:</b>
• Четкое изображение
• Видна сумма перевода
• Видна дата перевода
• Видны реквизиты получателя

<b>После отправки чека администратор проверит его и подтвердит верификацию.</b>
<i>Обычно проверка занимает до 15 минут.</i>""",

        # Теги
        'tag_manage_title': '🏷️ <b>УПРАВЛЕНИЕ ТЕГОМ</b>',
        'tag_current': '<b>Текущий тег:</b>',
        'tag_not_set': 'Не установлен',
        'tag_used_in_profits': '<b>Тег используется в профитах вместо вашего имени.</b>',
        'tag_example': '<i>Пример: В профитах будет отображаться "{tag}" вместо сгенерированного имени</i>',
        'tag_auto_hint': '<i>Если тег не установлен, будет сгенерировано автоматическое имя (воркер2035, воркер2914 и т.д.)</i>',
        'tag_choose_action': '<b>Выберите действие:</b>',
        'tag_setup_title': '🏷️ <b>УСТАНОВКА ТЕГА</b>',
        'tag_setup_text': """🏷️ <b>УСТАНОВКА ТЕГА</b>

<b>Введите ваш тег:</b>
• Тег должен начинаться с символа #
• Можно использовать буквы, цифры и подчеркивание
• Длина тега: от 2 до 20 символов
• Пример: #best_worker, #top_admin, #lolz_pro

<b>Тег будет отображаться в профитах.</b>
<b>Если тег не установлен, будет сгенерировано автоматическое имя.</b>

<b>Введите тег:</b>""",
        'tag_removed': '🗑️ <b>ТЕГ УДАЛЕН</b>',
        'tag_removed_text': """🗑️ <b>ТЕГ УДАЛЕН</b>

<b>Удаленный тег:</b> {tag}
<b>Теперь в профитах будет использоваться сгенерированное имя.</b>
<i>Вы можете установить новый тег в любое время.</i>""",
        'btn_set_tag': 'Установить тег',
        'btn_remove_tag': 'Удалить тег',
        'btn_set_new_tag': 'Установить новый',

        # Товары
        'items_title': '<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>МОИ ТОВАРЫ</b>',
        'items_empty': '<b>У вас пока нет товаров.</b>',
        'items_hint': '<i>Товары появляются здесь после успешного завершения сделок, где вы выступали в роли покупателя.</i>',
        'items_how_to': '<b>Как получить товар:</b>',
        'no_items_withdraw': '📭 <b>Нет товаров для вывода</b>\n\nУ вас пока нет невыведенных товаров.',

        # Вывод товара
        'withdraw_title': '📤 <b>ПОДТВЕРЖДЕНИЕ ВЫВОДА ТОВАРА</b>',
        'withdraw_text': """📤 <b>ПОДТВЕРЖДЕНИЕ ВЫВОДА ТОВАРА</b>

<b>Товар ID:</b> <code>{item_id}</code>
<b>Для вывода товара, пожалуйста, обратитесь в техподдержку:</b>
👉 {MANAGER_USERNAME}

<b>После обращения укажите номер товара и следуйте инструкциям поддержки.</b>
<i>Верифицированные пользователи получают приоритетное обслуживание и 0% комиссии.</i>

<b>Подтвердите вывод товара:</b>""",

        # Категория товара
        'category_title': """<tg-emoji emoji-id="5433653135799228968">📁</tg-emoji> <b>ВЫБЕРИТЕ КАТЕГОРИЮ ТОВАРА</b>

<b>Доступные категории:</b>
• <tg-emoji emoji-id="6037175527846975726">🎁</tg-emoji> Подарок — цифровые подарки, стикеры
• 🏷️ NFT тег — NFT метки, коллекции
• <tg-emoji emoji-id="5771695636411847302">📢</tg-emoji> Канал/чат — Telegram каналы, чаты
• <tg-emoji emoji-id="6028338546736107668">⭐</tg-emoji> Stars — Telegram Stars
• <tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> Другое — любой другой товар

<b>Выберите категорию:</b>""",

        # Оплата
        'payment_confirmed_buyer': """<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>ОПЛАТА ПОДТВЕРЖДЕНА</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Сделка:</b> #{deal_id}
<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Списано с баланса:</b> {amount} {currency}
<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>Остаток на балансе:</b> {balance} {currency}

<b>Ожидайте отправки товара от продавца.</b>
<i>Обычно это занимает до 15 минут.</i>

<b>Важно:</b> Товар будет передан только через поддержку!
Продавец отправит товар {MANAGER_USERNAME}, после проверки вы получите уведомление.""",

        'payment_received_seller': """<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>ОПЛАТА ПОЛУЧЕНА!</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Сделка:</b> #{deal_id}
<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>Покупатель:</b> @{buyer}
<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Верификация покупателя:</b> {verified}
<tg-emoji emoji-id="5811989245761426317">💸</tg-emoji> <b>Сумма:</b> {amount} {currency}

<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Средства зачислены на ваш баланс.</b>
Покупатель оплатил сделку с баланса. Отправьте товар поддержке!

<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji>️ <b>Критически важное правило:</b>
Товар должен быть передан исключительно поддержке - {MANAGER_USERNAME}!

<b>После того как вы отправили товар поддержке, нажмите кнопку снизу:</b>""",

        'btn_sent_item': 'Я отправил товар',

        # Сделка создана
        'deal_created': """<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>СДЕЛКА СОЗДАНА!</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>ID сделки:</b> #{deal_id}
<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Сумма:</b> {amount} {currency}
<tg-emoji emoji-id="5433653135799228968">📁</tg-emoji> <b>Категория:</b> {category}
<b>Ссылка/Описание:</b> {description}
<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>Продавец:</b> @{seller}
<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Верификация продавца:</b> {verified}

<b>Ссылка для покупателя:</b>
{link}

<b>Отправьте эту ссылку покупателю:</b>
{link}

<i>Как только покупатель перейдёт по ссылке, сделка начнётся.</i>""",

        # warning_title / btn_support_manager / btn_to_buyer удалены вместе с warning-викториной (ТЗ 2026-05-10)

        # Ошибки вывода
        'withdrawal_error': """<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>Ошибка вывода товара</b>

Произошла ошибка при обработке вашего запроса на вывод. Пожалуйста, свяжитесь с техподдержкой: {MANAGER_USERNAME}""",
        'balance_withdrawal_error': """<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>Ошибка вывода средств</b>

Произошла ошибка при обработке вашего запроса на вывод. Пожалуйста, свяжитесь с техподдержкой: {MANAGER_USERNAME}""",

        # Сделка завершена
        'deal_completed_buyer': """<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>СДЕЛКА УСПЕШНО ЗАВЕРШЕНА!</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>ID сделки:</b> #{deal_id}
<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Сумма:</b> {amount} {currency}
<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>Продавец:</b> @{seller}
<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>Товар:</b> {description}

<b>Информация:</b>
• Товар добавлен в раздел "Мои товары"
• Вы можете вывести его в любое время
• Для вывода перейдите в профиль и нажмите "Мои товары"

💙 Спасибо за использование {BOT_NAME} Relayer!""",

        'deal_completed_seller': """<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>СДЕЛКА УСПЕШНО ЗАВЕРШЕНА!</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>ID сделки:</b> #{deal_id}
<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Сумма:</b> {amount} {currency}
<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>Покупатель:</b> @{buyer}
<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>Товар:</b> {description}

<b>Информация:</b>
• Товар передан покупателю
• Сделка успешно завершена

💙 Спасибо за использование {BOT_NAME} Relayer!""",

        # Профиль
        'profile_title': '<b>🏆 ПРОФИЛЬ {BOT_NAME} Relayer</b>',
        'deals_empty': '📭 <b>У ВАС ПОКА НЕТ АКТИВНЫХ СДЕЛОК</b>\n\nСоздайте свою первую сделку с помощью кнопки ниже!',
        'deals_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>ВАШИ АКТИВНЫЕ СДЕЛКИ</b>',
        'deals_select': 'Выберите сделку для управления:',

        # Роли
        'role_user': '<tg-emoji emoji-id="5886412370347036129">👤</tg-emoji> Пользователь',
        'role_owner': '<tg-emoji emoji-id="5807868868886009920">👑</tg-emoji> Владелец системы',
        'role_admin': '⚙️ Администратор',
        'role_worker': '👷 Воркер',
        'role_blocked': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> (Заблокирован)',
        'verified_yes': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Верифицирован',
        'verified_no': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Не верифицирован',

        # Суммы вводов
        'enter_amount': '<tg-emoji emoji-id="5811989245761426317">💰</tg-emoji> <b>Введите сумму сделки:</b>',
        'invalid_amount': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕВЕРНЫЙ ФОРМАТ СУММЫ</b>\n\nВведите число, например: 1500 или 5.75',
        'amount_zero': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>СУММА ДОЛЖНА БЫТЬ БОЛЬШЕ НУЛЯ</b>',
        'description_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ССЫЛКА/ОПИСАНИЕ СЛИШКОМ КОРОТКОЕ</b>\n\nМинимум 5 символов',

        # Направления профита
        'direction_sell': 'Продажа товара мамонту',
        'direction_buy': 'Покупка товара у мамонта',
        'direction_ad': 'Реклама бота',
        'direction_deposit': 'Пополнение баланса мамонтом',

        # Баланс
        'balance_deposit': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>БАЛАНС УСПЕШНО ПОПОЛНЕН!</b>',
        'deposit_confirmed': """<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>БАЛАНС УСПЕШНО ПОПОЛНЕН!</b>

<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> <b>Сумма:</b> {amount} {currency}
<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>Текущий баланс:</b> {balance} {currency}

<b>Информация:</b>
• Средства зачислены на ваш баланс
• Вы можете использовать их для покупки товаров
• Для вывода средств обратитесь в техподдержку

💙 Спасибо за использование {BOT_NAME} Relayer!""",

        # Верификация инфо
        'verification_info': """<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> Верификация {BOT_NAME}

<tg-emoji emoji-id="5447644880824181073">🎯</tg-emoji> <b>Что дает премиум-статус:</b>
• <tg-emoji emoji-id="5902016123972358349">🔐</tg-emoji> Верификация продавца — знак доверия
• <tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Гарант сделок — защита от мошенников
• <tg-emoji emoji-id="5773677501825945508">⚡️</tg-emoji> Приоритетная поддержка — быстрые ответы
• <tg-emoji emoji-id="5895444149699612825">📈</tg-emoji> Сниженная комиссия — 0.5% вместо 1%
• <tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> Быстрые выплаты — в течение 1 часа
• <tg-emoji emoji-id="5413879192267595313">🎁</tg-emoji> Бонусы за рефералов — +10% к балансу

<tg-emoji emoji-id="5902016123972358349">🔒</tg-emoji> <b>Безопасность:</b>
• Шифрование всех данных
• Страхование сделок
• Юридическая защита
• 24/7 мониторинг

<tg-emoji emoji-id="5895444149699612825">📈</tg-emoji> <b>Преимущества:</b>
• Повышенное доверие покупателей
• Больше успешных сделок
• Персональный менеджер
• Эксклюзивные предложения

<tg-emoji emoji-id="5936017305585586269">🔰</tg-emoji> Подробнее можете узнать у поддержки""",

        'verification_info_verified': """<tg-emoji emoji-id="5902016123972358349">🔒</tg-emoji> Верификация

<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> Ваш аккаунт верифицирован.
Статус присвоен после проверки службой безопасности {BOT_NAME}.""",

        # Статистика
        'stats_title': '<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>СТАТИСТИКА {BOT_NAME} Relayer</b>',
        'stats_advantages': """⭐ <b>Наша платформа активно развивается!</b>
<i>Присоединяйтесь к растущему сообществу</i>

💙 <b>Преимущества {BOT_NAME} Relayer:</b>
• <tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Гарант сделок
• <tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> Быстрые выплаты
• <tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> Выгодные курсы
• 📞 Поддержка 24/7
• <tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> Система верификации

🤍 <b>Мы растем вместе с вами!</b>""",

        # Реквизиты пользователя
        'requisites_card': '<tg-emoji emoji-id="5967548335542767952">💳</tg-emoji> Карта',
        'requisites_ton': '⚡ Ton',
        'requisites_phone': '📱 Телефон',
        'requisites_usdt': '<tg-emoji emoji-id="5963312935148195483">💎</tg-emoji> Usdt',
        'not_specified': 'Не указан',
        'not_specified_f': 'Не указана',

        # Кнопки воркер панели
        'btn_my_stats': 'Моя статистика',
        'btn_my_deals_worker': 'Мои сделки',
        'btn_fake_deals': 'Накрутка сделок',
        'btn_fake_balance': 'Накрутка баланса',
        'btn_remove_deals': 'Открутка сделок',
        'btn_trim_profile': 'Урезать профиль',
        'btn_change_rating': 'Изменить оценку',

        # Items menu
        'items_total': 'Всего товаров:',
        'items_pending': 'Ожидают вывода:',
        'items_withdrawn': 'Выведено:',
        'items_pending_title': 'ОЖИДАЮТ ВЫВОДА:',
        'items_withdrawn_title': 'ВЫВЕДЕННЫЕ ТОВАРЫ:',
        'items_item': 'Товар',
        'items_desc': 'Описание',
        'items_received': 'Получен',
        'items_withdrawn_at': 'Выведен',
        'items_unknown': 'Неизвестно',
        'items_how_to_steps': """1. Найдите продавца и создайте сделку
2. Оплатите сделку с баланса
3. После подтверждения продавцом, товар появится здесь
4. Вы сможете вывести товар в любое время""",

        # Withdraw menu
        'withdraw_menu_title': 'ВЫВОД ТОВАРА',
        'withdraw_items_waiting': 'товаров, ожидающих вывода',
        'withdraw_select': 'Выберите товар для вывода или введите его ID:',

        # Balance withdraw
        'balance_withdraw_title': 'ВЫВОД СРЕДСТВ',
        'balance_your': 'Ваш баланс:',
        'balance_enter_amount': 'Введите сумму и валюту для вывода:',
        'balance_min': 'Минимальная сумма вывода:',
        'balance_contact_support': 'После запроса свяжитесь с поддержкой',
        'btn_to_profile': 'В профиль',

        # Verification menu buttons
        'btn_pay_card': 'Оплатить картой РФ',
        'btn_pay_usdt': 'Оплатить USDT',
        'btn_pay_kzt': 'Оплатить KZT',
        'btn_pay_byn': 'Оплатить BYN',
        'btn_pay_stars': 'Оплатить Stars',

        # Product categories
        'cat_gift': '🎁 Подарок',
        'cat_nft': '🏷️ Nft тег',
        'cat_channel': '<tg-emoji emoji-id="5771695636411847302">📢</tg-emoji> Канал/чат',
        'cat_stars': '<tg-emoji emoji-id="6028338546736107668">⭐</tg-emoji> Stars',
        'cat_other': '📦 Другое',
        'desc_gift_title': '📝 <b>ССЫЛКА НА ПОДАРОК</b>',
        'desc_gift_text': """📝 <b>ССЫЛКА НА ПОДАРОК</b>

<b>Категория:</b> {category}

<b>Вставьте ссылку на подарок:</b>
🎁 Создание сделки с подарком

Введите ссылку(-и) на подарок(-и) в одном из форматов:
https://... или t.me/...

Например:
t.me/nft/PlushPepe-1

<b>Важно:</b> Убедитесь, что ссылка правильная и ведет именно на тот товар, который вы продаете!

<b>Введите ссылку:</b>""",
        'desc_stars_text': """📝 <b>ОПИСАНИЕ ТОВАРА</b>

<b>Категория:</b> {category}

<b>Опишите подробно что вы продаёте:</b>
• Количество Stars
• Платформа (iOS/Android/Web)
• Дополнительные условия
• Способ передачи

<b>Пример:</b>
"1000 Telegram Stars для iOS, передача через бота"

<b>Введите описание:</b>""",
        'desc_other_text': """📝 <b>ОПИСАНИЕ ТОВАРА</b>

<b>Категория:</b> {category}

<b>Опишите подробно что вы продаёте:</b>
• Название товара
• Количество
• Условия передачи
• Дополнительная информация
• Состояние товара

<b>Будьте максимально подробны и честны!</b>

<b>Введите описание:</b>""",
        'desc_default_text': """📝 <b>ОПИСАНИЕ ТОВАРА</b>

<b>Категория:</b> {category}

<b>Опишите подробно что вы продаёте:</b>

Введите юзернейм(ы), которые хотите продать, в формате:
@username

Если у вас несколько юзернеймов, разделите их новыми строками, например:
@username1
@username2
@username3
<b>Введите описание:</b>""",

        # Profile labels
        'profile_name': 'Имя:',
        'profile_rating': 'Рейтинг:',
        'rating_no_deals': 'нету сделок',
        'profile_success_deals': 'Успешных сделок:',
        'profile_disputes_won': 'Споров выиграно:',
        'profile_active_deals': 'Активных сделок:',
        'profile_balance': 'Баланс:',

        # Deals list
        'deals_role_seller': '🛒 Продавец',
        'deals_role_buyer': '<tg-emoji emoji-id="5811989245761426317">💰</tg-emoji> Покупатель',
        'deals_buyer_label': 'Покупатель:',
        'deals_seller_label': 'Продавец:',
        'deals_awaiting': 'Ожидается',
        'deals_more': 'И еще {count} сделок...',
        'deals_deal': 'Сделка',

        # Deal view
        'deal_view_seller_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>ВАША СДЕЛКА</b>',
        'deal_view_buyer_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>ВАША СДЕЛКА</b>',
        'deal_view_id': '<b>ID:</b>',
        'deal_view_status': '<b>Статус:</b>',
        'deal_view_category': '<b>Категория:</b>',
        'deal_view_desc': '<b>Товар/Ссылка:</b>',
        'deal_view_amount': '<b>Сумма:</b>',
        'deal_view_payment_method': '<b>Метод оплаты:</b>',
        'deal_view_your_verification': '<b>Ваша верификация:</b>',
        'deal_view_buyer_link': '<b>Ссылка для покупателя:</b>',
        'deal_view_buyer': '<b>Покупатель:</b>',
        'deal_view_send_link': '<b>Отправьте эту ссылку покупателю:</b>',
        'deal_view_seller': '<b>Продавец:</b>',
        'deal_view_seller_rating': '<b>Рейтинг продавца:</b>',
        'deal_view_seller_verification': '<b>Верификация продавца:</b>',
        'deal_view_pay_from_balance': '<b>Оплата будет произведена с вашего баланса.</b>',
        'deal_status_awaiting_buyer': 'Ожидание покупателя',
        'deal_status_awaiting_payment': 'Ожидание оплаты',
        'deal_status_paid': 'Оплачено',
        'deal_buyer_awaiting': 'Ожидается',
        'deal_category_default': 'Товар',
        'deal_verified_yes': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Да',
        'deal_verified_no': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Нет',

        # Buyer joined
        'buyer_joined_seller': """<b><tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> К сделке #{deal_id} присоединился покупатель @{buyer}!</b>

<blockquote><tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> После получения средств, вы получите уведомление для передачи товара менеджеру</blockquote>

<blockquote>📈 Завершённых сделок у продавца: {success_deals}</blockquote>

<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Передача товара проходит ТОЛЬКО через менеджера {manager}. Не переводите товары напрямую продавцу!

❗️ Проверьте уведомление в боте о получение средств!""",

        'buyer_joined_buyer': """<b><tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> К сделке #{deal_id} присоединился продавец @{seller}!</b>

<blockquote><tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> Реквизиты менеджера для оплаты: {manager}</blockquote>

<blockquote>📈 Завершённых сделок у продавца: {success_deals}</blockquote>

<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Вся оплата проходит ТОЛЬКО через менеджера {manager}. Не переводите средства напрямую продавцу!

❗️ Проверьте реквизиты перед оплатой!

<b>Товар/Ссылка:</b> {description}

<tg-emoji emoji-id="5811989245761426317">💸</tg-emoji> <b>Сумма:</b> {amount} {currency}""",

        # Balance & requisites
        'balance_req_title': '<b><tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> БАЛАНС И РЕКВИЗИТЫ</b>',
        'balance_your_title': '<b>Ваш баланс:</b>',
        'requisites_your_title': '<b>Ваши реквизиты:</b>',
        'requisites_crypto_label': 'Криптокошелек',
        'requisites_card_label': 'Карта',
        'requisites_phone_label': 'Телефон',
        'balance_choose_action': '<b>Выберите действие:</b>',
        'not_specified_req': 'Не указан',
        'btn_deposit_balance': 'Пополнить баланс',
        'btn_withdraw_balance': 'Вывести',
        'btn_ton_wallet': 'Ton кошелёк',
        'btn_card_req': 'Карта',
        'btn_phone_req': 'Телефон',
        'btn_usdt_wallet': 'Usdt кошелёк',

        # Referral
        'referral_title': '<b><tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> Реф. система</b>',
        'referral_percent': 'Ваш реферальный процент',
        'referral_invited': 'Приглашено пользователей',
        'referral_balance_ton': 'Реф. баланс TON',
        'referral_balance_usdt': 'Реф. баланс USDT TON',
        'referral_link_label': '<b>Ваша ссылка для приглашения:\n\n{ref_link}</b>',
        'btn_copy_link': 'Копировать',

        # Buttons for deals
        'btn_pay_balance': 'Оплатить с баланса',
        'btn_open_dispute': 'Открыть спор',
        'btn_my_deals_nav': 'Мои сделки',
        'btn_deal_link': 'Сделка',

        # Deposit
        'deposit_select_currency_text': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> Пополнение баланса\n\nВыберите валюту для пополнения:',
        'deposit_currency_title_prefix': 'Пополнить баланс',
        'deposit_currency_support_hint': 'Получите реквизиты для пополнения у поддержки.\n<tg-emoji emoji-id="5447644880824181073">❗️</tg-emoji> После пополнения деньги зачисляются на ваш баланс.',
        'deposit_title': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>ПОПОЛНЕНИЕ БАЛАНСА</b>',
        'deposit_choose': '<b>Выберите способ пополнения:</b>',
        'deposit_card_ru': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> Карта РФ — пополнение рублями',
        'deposit_card_ua': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> Карта UA — пополнение гривнами',
        'deposit_crypto': '₿ Криптовалюта — BTC, ETH, USDT, TON, BNB, SOL',
        'deposit_stars': '⭐ Telegram Stars — пополнение звездами',
        'deposit_after': '<b>После выбора способа вам будут показаны реквизиты для перевода.</b>',
        'deposit_important': '<b>Важно:</b> После перевода обязательно отправьте чек кнопкой "📤 Отправить чек"!',
        'deposit_verified_hint': '<i>Верифицированные пользователи получают приоритетную обработку заявок</i>',
        'deposit_amount_title': '<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>ВВЕДИТЕ СУММУ ПОПОЛНЕНИЯ</b>',
        'deposit_method_label': '<b>Способ:</b>',
        'deposit_currency_label': '<b>Валюта:</b>',
        'deposit_min': '• Минимальная сумма:',
        'deposit_unlimited': 'не ограничена',
        'deposit_after_amount': '<b>После ввода суммы вы сможете отправить чек.</b>',
        'deposit_instructions': '<b>Инструкция:</b>',
        'deposit_instruction_1': '1. Переведите указанную сумму по реквизитам выше',
        'deposit_instruction_1_crypto': '1. Переведите {name} на указанный адрес',
        'deposit_instruction_2': '2. Сохраните чек/скриншот перевода',
        'deposit_instruction_3': '3. Нажмите кнопку "📤 Отправить чек"',
        'deposit_instruction_4': '4. Прикрепите фото или документ с подтверждением',
        'deposit_instruction_5': '5. После проверки администратором средства поступят на баланс',
        'deposit_important_note': '<b>Важно:</b> Без отправки чека пополнение не будет зачислено!',
        'deposit_requisites_label': '<b>Реквизиты для пополнения ({name}):</b>',
        'deposit_support_contact': 'Для получения актуальных реквизитов обратитесь в поддержку {support}',
        'deal_amount_title': '<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Создание сделки\n\n<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> Укажите сумму сделки:',
        'deal_amount_examples': '<tg-emoji emoji-id="5795328215886894640">📌</tg-emoji> Пример: 2000.50',
        'deal_amount_min': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> Указывайте точную сумму, чтобы избежать ошибок при обработке сделки.',
        'deal_amount_min_stars': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> Укажите количество Stars.',
        'deal_amount_enter': '',
        'deal_amount_too_small': '<tg-emoji emoji-id="5922712343011135025">❌</tg-emoji> <b>Слишком маленькая сумма</b>\n\nМинимальная сумма: {min_amount} {currency}',
        'deal_created_title': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>СДЕЛКА СОЗДАНА!</b>',
        'deal_gifts_count': '<b>Подарков в сделке:</b>',
        'deal_send_link_buyer': '<b>Отправьте эту ссылку покупателю:</b>',
        'deal_started_when': '<i>Как только покупатель перейдёт по ссылке, сделка начнётся.</i>',
        'deal_seller_label': '<tg-emoji emoji-id="6041705726206808304">👤</tg-emoji> <b>Продавец:</b>',
        'deal_seller_verif': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Верификация продавца:</b>',
        'card_ru_name': 'Карта РФ',
        'card_ua_name': 'Карта UA',
        'not_specified_val': 'Не указан',
        'deposit_reason_none': 'Не указана (свяжитесь с пользователем для уточнения)',
        'requisites_card_btn': 'Карта',
        'requisites_phone_btn': 'Телефон',

        # Deal view
        'deal_info_title': '<b>📋 Информация о сделке</b>',
        'deal_status_label': '<b>Статус:</b>',
        'deal_status_created': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> Ожидает оплаты',
        'deal_status_paid': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> Оплачена',
        'deal_status_completed': '<tg-emoji emoji-id="5893193062850499428">📱</tg-emoji> Завершена',
        'deal_status_disputed': '<tg-emoji emoji-id="5922712343011135025">❌</tg-emoji> Спор',
        'deal_buyer_awaiting': 'Ожидается',
        'deal_send_link': '<b>Отправьте эту ссылку покупателю:</b>',
        'deal_buyer_prompt': '<b>Для оплаты нажмите кнопку ниже</b>',

        # Seller sent item
        'seller_sent_item': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>ТОВАР ОТПРАВЛЕН!</b>',
        'seller_sent_wait': '<b>Ожидайте подтверждения от поддержки.</b>',

        # Verification payment
        'verification_pay_title': '🔰 <b>Оплата верификации ({method})</b>',
        'verification_pay_cost': '<b>Стоимость верификации:</b> {price} {currency}',
        'verification_pay_after': '<b>После перевода нажмите кнопку "📤 Отправить чек" и прикрепите подтверждение оплаты.</b>',
        'verif_receipt_text': '📤 <b>ОТПРАВКА ЧЕКА НА ВЕРИФИКАЦИЮ</b>\n\nОтправьте фото или документ с подтверждением перевода.\n\n<b>Требования к чеку:</b>\n• Чёткое изображение\n• Видна сумма перевода\n• Видна дата перевода\n• Видны реквизиты получателя\n\n<b>После отправки чека администратор проверит его и подтвердит верификацию.</b>\n<i>Обычно проверка занимает до 15 минут.</i>',
        'verif_pay_card_msg': '🔰 <b>ОПЛАТА ВЕРИФИКАЦИИ (КАРТА РФ)</b>\n\n<b>Стоимость верификации:</b> {price} RUB\n{details}\n\n<b>После перевода нажмите кнопку "📤 Отправить чек" и прикрепите подтверждение оплаты.</b>',
        'verif_pay_usdt_msg': '🔰 <b>ОПЛАТА ВЕРИФИКАЦИИ (USDT TRC20)</b>\n\n<b>Стоимость верификации:</b> {price} USDT\n{details}\n\n<b>После перевода нажмите кнопку "📤 Отправить чек" и прикрепите подтверждение оплаты.</b>',
        'verif_pay_simple_msg': '🔰 <b>ОПЛАТА ВЕРИФИКАЦИИ ({method})</b>\n\n<b>Стоимость верификации:</b> {price} {currency}\nСвяжитесь с поддержкой для уточнения реквизитов.\n\n<b>Инструкция:</b>\n1. Свяжитесь с {MANAGER_USERNAME} для оплаты.\n2. После проверки администратором средства поступят на баланс.',
        'verif_pay_stars_msg': '🔰 <b>ОПЛАТА ВЕРИФИКАЦИИ (Stars)</b>\n\n<b>Стоимость верификации:</b> {price} Stars\nПереведите оплату звёздами на аккаунт поддержки\nСеть: Stars\n\n<b>Инструкция:</b>\n1. Переведите Stars на аккаунт поддержки ({MANAGER_USERNAME})\n2. После проверки администратором средства поступят на баланс',

        # Error messages
        'error_own_deal': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Вы не можете присоединиться к своей собственной сделке как покупатель.',
        'error_deal_taken': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Эта сделка уже занята другим покупателем.',

        # Wallet updates
        'wallet_ton_title': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> <b>TON КОШЕЛЁК</b>',
        'wallet_crypto_title': '<tg-emoji emoji-id="5992430854909989581">🪙</tg-emoji> <b>КРИПТОКОШЕЛЁК</b>',
        'wallet_card_title': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> <b>БАНКОВСКАЯ КАРТА</b>',
        'wallet_phone_title': '<tg-emoji emoji-id="5330319637156479518">📱</tg-emoji> <b>НОМЕР ТЕЛЕФОНА</b>',
        'wallet_usdt_title': '<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> <b>USDT КОШЕЛЁК</b>',
        'wallet_current': '<b>Текущий адрес:</b>',
        'wallet_current_card': '<b>Текущие реквизиты:</b>',
        'wallet_current_phone': '<b>Текущий номер:</b>',
        'wallet_send_new': '<b>Отправьте новый адрес кошелька:</b>',
        'wallet_send_crypto': '<b>Отправьте адрес кошелька и сеть одним сообщением:</b>',
        'wallet_send_card': '<b>Отправьте новые реквизиты:</b>',
        'wallet_send_phone': '<b>Отправьте номер телефона:</b>',
        'wallet_send_usdt': '<b>Отправьте адрес Usdt (TRC20):</b>',
        'wallet_ton_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>TON КОШЕЛЁК ОБНОВЛЁН</b>',
        'wallet_crypto_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>КРИПТОКОШЕЛЁК ОБНОВЛЁН</b>',
        'wallet_card_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>БАНКОВСКАЯ КАРТА ОБНОВЛЕНА</b>',
        'wallet_phone_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>НОМЕР ТЕЛЕФОНА ОБНОВЛЁН</b>',
        'wallet_usdt_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>USDT КОШЕЛЁК ОБНОВЛЁН</b>',
        'wallet_new_address': '<b>Новый адрес:</b>',
        'wallet_new_crypto': '<b>Новые реквизиты:</b>',
        'wallet_new_card': '<b>Новые реквизиты:</b>',
        'wallet_new_phone': '<b>Новый номер:</b>',
        'wallet_card_note': '<b>Теперь вы можете получать рублёвые платежи на эту карту.</b>\n<i>Реквизиты будут автоматически показаны покупателям.</i>',
        'wallet_phone_note': '<b>Теперь вы можете получать платежи Qiwi/юmoney на этот номер.</b>\n<i>Убедитесь, что номер активен и привязан к кошельку.</i>',
        'wallet_usdt_note': '<b>Теперь вы можете получать Usdt платежи на этот кошелёк.</b>\n<i>Проверьте, что адрес принадлежит сети TRC20.</i>',
        'btn_all_requisites': 'Все реквизиты',
        'wallet_menu_title': """🏦 <b>УПРАВЛЕНИЕ РЕКВИЗИТАМИ</b>

<b>Укажите реквизиты для получения платежей:</b>
• <tg-emoji emoji-id='5992430854909989581'>🪙</tg-emoji> Криптокошелек — адрес и сеть (Ton, Trc-20 и т.д.)
• <tg-emoji emoji-id='5445353829304387411'>💳</tg-emoji> Карта — для получения рублей и других валют
• 📱 Телефон — в международном формате

<b>Примечание:</b> Stars не требуют реквизитов

<b>Важно:</b> Указывайте только проверенные реквизиты!

<b>Выберите тип реквизитов:</b>""",
        'wallet_ton_hint': """• Формат: UQ... или EQA...
• Обязательно проверьте правильность
• Адрес должен начинаться с UQ или EQ
<i>Адрес будет сохранён для получения платежей</i>""",
        'wallet_crypto_hint': """• Одним сообщением: адрес кошелька и сеть
• Пример: UQAbc123...xyz, сеть Ton
• Пример: TXaBc123...xyz, сеть Trc-20
<i>Реквизиты будут сохранены для получения крипто-платежей</i>""",
        'wallet_card_hint': """• Формат: 2200 1234 5678 9010
• Или: Банк — Номер карты
• Поддерживаются карты РФ, РБ, КЗ, UA
<i>Реквизиты будут сохранены для получения рублёвых платежей</i>""",
        'wallet_phone_hint': """• Формат: +79991234567
• Используется для Qiwi/юmoney
• Укажите номер с кодом страны
<i>Номер будет сохранён для получения платежей</i>""",
        'wallet_usdt_hint': """• Формат: T... (TRC20 сеть)
• Обязательно проверьте правильность
• Только сеть TRC20!
<i>Адрес будет сохранён для получения Usdt</i>""",

        # Admin panel buttons & messages
        'btn_add_worker': 'Добавить воркера',
        'btn_remove_worker': 'Удалить воркера',
        'btn_check_deals': 'Проверить сделки',
        'btn_demote_worker': 'Понизить воркера',
        'btn_export_csv': 'Экспорт в CSV',
        'btn_worker_panel_nav': 'Воркер панель',
        'btn_admin_panel_nav': 'Админ панель',
        'btn_all_deals': 'Все сделки',
        'btn_stats': 'Статистика',
        'btn_my_profile_nav': 'Мой профиль',
        'btn_my_items': 'Мои товары',
        'btn_my_deals_nav2': 'Мои сделки',
        'btn_manage_tag': 'Управление тегом',
        'btn_to_profile': 'В профиль',
        'btn_to_worker_panel': 'В воркер панель',
        'btn_confirm_withdraw': 'Подтвердить вывод',
        'btn_confirm_deposit': 'Подтвердить пополнение',
        'btn_decline': 'Отклонить',
        'btn_verify_user': 'Верифицировать',
        'btn_unverify_user': 'Снять верификацию',
        'btn_add_balance': 'Добавить',
        'btn_set_balance': 'Установить',
        'btn_deduct_balance': 'Списать',
        'btn_trim_deals': 'Урезать сделки',
        'btn_trim_balance': 'Урезать баланс',
        'btn_remove_admin': 'Удалить админа',
        'btn_profile_view': 'Профиль',
        'btn_demote': 'Понизить',
        'btn_select_other': 'Выбрать другого',
        'btn_to_list': 'К списку',
        'btn_new_broadcast': 'Новая рассылка',
        'btn_new_message': 'Новое сообщение',
        'btn_try_again': 'Попробовать снова',
        'btn_recipient_list': 'Список получателей',
        'btn_not_paid': 'Не оплатил',
        'btn_not_sent': 'Не отправил',
        'btn_wrong_item': 'Не тот товар',
        'btn_other_reason': 'Другое',
        'dispute_title': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>ОТКРЫТИЕ СПОРА</b>',
        'dispute_deal': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Сделка:</b>',
        'dispute_role': "<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>Ваша роль:</b>",
        'dispute_role_buyer': 'Покупатель',
        'dispute_role_seller': 'Продавец',
        'dispute_support': '👨\u200d💼 <b>Поддержка сделки:</b>',
        'dispute_confirm': '<b>Вы уверены, что хотите открыть спор?</b>\n<i>Администратор рассмотрит ваш спор в течение 24 часов.</i>',
        'dispute_reason': '<b>Выберите причину:</b>',
        'btn_contact_manager': 'Связаться с менеджером',
        'btn_to_deal': 'К сделке',
        'btn_deal_complete_profit': 'Завершить с профитом',
        'btn_update': 'Обновить',
        'btn_contact_support': 'Поддержка',
        'btn_balance_manage': 'Управление балансом',

        # Admin alerts
        'admin_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Доступ запрещён. Только администраторы могут выполнять это действие',
        'admin_complete_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Доступ запрещён. Только администраторы могут завершать сделки',
        'admin_confirm_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Доступ запрещён. Только администраторы могут подтверждать получение товара',
        'owner_only_admins': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Доступ запрещён. Только владелец системы может просматривать список всех админов',
        'owner_only_add_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Доступ запрещён. Только владелец системы может добавлять администраторов',
        'owner_only_remove_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Доступ запрещён. Только владелец системы может удалять администраторов',
        'admin_block_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Доступ запрещён. Только администраторы могут управлять блокировками',
        'cannot_block_owner': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Нельзя заблокировать владельца системы',
        'already_blocked': '⚠️ Пользователь уже заблокирован',
        'owner_unblock_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Только владелец системы может разблокировать владельца',
        'not_blocked': '⚠️ Пользователь не заблокирован',
        'user_not_worker': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Пользователь не является воркером',
        'method_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Метод не найден',
        'error_generic': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Ошибка',
        'deposit_approved': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Пополнение подтверждено!',
        'deposit_error': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Ошибка подтверждения',
        'deposit_declined': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Пополнение отклонено',
        'deposit_declined_user': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Ваш запрос на пополнение баланса был отклонен администратором. Свяжитесь с поддержкой для уточнения причин.',
        'user_verified_alert': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Пользователь верифицирован',
        'user_unverified_alert': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Верификация снята',
        'data_saved': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Данные сохранены успешно!',
        'you_are_blocked': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> Вы заблокированы',
        'export_in_dev': '📥 Функция экспорта в разработке',
        'lang_changed': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Язык изменён!',
        'payment_not_supported': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Оплата через подтверждение больше не поддерживается. Используйте оплату с баланса.',

        # Admin error messages
        'invalid_id_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕВЕРНЫЙ ФОРМАТ ID</b>\n\nВведите целое число',
        'invalid_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕВЕРНЫЙ ФОРМАТ</b>',
        'invalid_amount_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕВЕРНЫЙ ФОРМАТ СУММЫ</b>\n\nВведите число, например: 1000 или 0.01',
        'invalid_currency': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕВЕРНАЯ ВАЛЮТА</b>',
        'user_not_found_id': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ПОЛЬЗОВАТЕЛЬ НЕ НАЙДЕН</b>',
        'cannot_block_owner_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕЛЬЗЯ ЗАБЛОКИРОВАТЬ ВЛАДЕЛЬЦА СИСТЕМЫ</b>',
        'cannot_remove_owner': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕЛЬЗЯ УДАЛИТЬ ВЛАДЕЛЬЦА СИСТЕМЫ</b>',
        'cannot_add_owner_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕЛЬЗЯ ДОБАВИТЬ ВЛАДЕЛЬЦА СИСТЕМЫ КАК АДМИНА</b>',
        'edit_cancelled': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>Редактирование отменено.</b>',
        'method_not_found_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>Ошибка: метод не найден.</b>',
        'send_receipt_first': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Сначала выберите способ пополнения и введите сумму.',
        'send_photo_doc': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Пожалуйста, отправьте фото или документ с чеком.',
        'deal_deleted': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>СДЕЛКА НЕ НАЙДЕНА</b>\n\nСделка была удалена или не существует.',
        'scam_desc_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>СЛИШКОМ КОРОТКОЕ ОПИСАНИЕ</b>\n\nОпишите подробнее на что заскамили (минимум 3 символа).',
        'deal_complete_error': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ОШИБКА ЗАВЕРШЕНИЯ СДЕЛКИ</b>\n\nНе удалось завершить сделку.',
        'amount_negative': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕВЕРНАЯ СУММА</b>\n\nСумма должна быть больше 0',
        'amount_too_small': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>СЛИШКОМ МАЛЕНЬКАЯ СУММА</b>',
        'insufficient_funds_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕДОСТАТОЧНО СРЕДСТВ</b>',
        'tag_must_start_hash': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ТЕГ ДОЛЖЕН НАЧИНАТЬСЯ С СИМВОЛА #</b>\n\nПример: #best_worker',
        'tag_too_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ТЕГ СЛИШКОМ КОРОТКИЙ</b>\n\nМинимум 2 символа (включая #)',
        'tag_too_long': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ТЕГ СЛИШКОМ ДЛИННЫЙ</b>\n\nМаксимум 20 символов',
        'tag_already_used': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ТЕГ УЖЕ ИСПОЛЬЗУЕТСЯ</b>',
        'no_recipients': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>НЕТ ПОЛУЧАТЕЛЕЙ</b>\n\nДля выбранного типа рассылки не найдено получателей.',
        'verified_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>Верифицированные пользователи не найдены</b>',
        'deals_not_found_search': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>СДЕЛКИ НЕ НАЙДЕНЫ</b>',
        'users_not_found_search': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ПОЛЬЗОВАТЕЛИ НЕ НАЙДЕНЫ</b>',
        'bot_error': 'Ошибка использования бота.',
        'access_denied_block': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ДОСТУП ЗАПРЕЩЁН</b>\n\nТолько администраторы могут блокировать пользователей.',
        'access_denied_unblock': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ДОСТУП ЗАПРЕЩЁН</b>\n\nТолько администраторы могут разблокировать пользователей.',
        'access_denied_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ДОСТУП ЗАПРЕЩЁН</b>\nУ вас нет прав администратора',
        'deals_negative': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Количество сделок не может быть отрицательным',
        'enter_integer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Введите целое число',
        'amount_negative_balance': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Сумма не может быть отрицательной',

        # UI keyboard buttons (admin/worker/user-facing)
        'btn_deposit_card_ru': 'Карта РФ',
        'btn_deposit_card_ua': 'Карта UA',
        'btn_deposit_crypto': 'Криптовалюта',
        'btn_deposit_stars': 'Telegram Stars',
        'btn_admin_stats': 'Статистика',
        'btn_admin_users': 'Пользователи',
        'btn_admin_all_deals': 'Все сделки',
        'btn_admin_deal_activities': 'Действия в сделке',
        'btn_admin_user_activities': 'Действия пользователя',
        'btn_admin_broadcast': 'Рассылка',
        'btn_admin_workers_list': 'Список воркеров',
        'btn_admin_private_msg': 'Личное сообщение',
        'btn_admin_add_worker': 'Выдать воркера',
        'btn_admin_remove_worker': 'Удалить воркера',
        'btn_admin_check_deals': 'Проверить сделки',
        'btn_admin_demote_worker': 'Понизить воркера',
        'btn_admin_fake_deals': 'Накрутка сделок',
        'btn_admin_fake_balance': 'Накрутка баланса',
        'btn_admin_balance_mgmt': 'Управление балансом',
        'btn_admin_block_mgmt': 'Управление блокировками',
        'btn_admin_verif_requests': 'Заявки на верификацию',
        'btn_admin_verif_mgmt': 'Управление верификацией',
        'btn_admin_deposit_req': 'Реквизиты для пополнения',
        'btn_admin_admins_list': 'Список админов',
        'btn_admin_add_admin': 'Выдать админку',
        'btn_admin_remove_admin': 'Удалить админа',
        'btn_admin_system_info': 'Информация',
        'btn_verify_user_action': 'Верифицировать пользователя',
        'btn_unverify_user_action': 'Снять верификацию',
        'btn_verified_list': 'Список верифицированных',
        'btn_search_by_id': 'Поиск по ID',
        'btn_add_balance_action': 'Добавить баланс',
        'btn_set_balance_action': 'Установить баланс',
        'btn_deduct_balance_action': 'Списать баланс',
        'btn_check_balance': 'Проверить баланс',
        'btn_block_user': 'Заблокировать',
        'btn_unblock_user': 'Разблокировать',
        'btn_blocked_list': 'Список заблокированных',
        'btn_no_blocked': 'Нет заблокированных',
        'btn_no_admins': 'Нет администраторов',
        'btn_no_deals': 'Нет сделок',
        'btn_no_deal_activities': 'Нет сделок с активностью',
        'btn_search_deal': 'Поиск сделки',
        'btn_broadcast_all': 'Всем пользователям',
        'btn_broadcast_workers': 'Всем воркерам',
        'btn_broadcast_admins': 'Всем админам',
        'btn_broadcast_user': 'Конкретному пользователю',
        'btn_write_user': 'Написать пользователю',
        'btn_recipient_list_admin': 'Список получателей',
        'btn_prev': 'Назад',
        'btn_next': 'Вперед ➡️',
        'btn_owner_label': 'Владелец',
        'btn_admin_label': 'Админ',
        'btn_remove_worker_confirm': 'Удалить воркера',
        'btn_demote_confirm': 'Понизить',
        'btn_check_deals_worker': 'Проверить сделки',
        'btn_worker_stats': 'Статистика',
        'btn_card_short': 'Карта',
        'btn_phone_short': 'Телефон',
        'btn_payment_ton':   '⚡ Ton',
        'btn_payment_crypto': '🪙 Криптокошелек',
        'btn_payment_card':  '💳 Карта',
        'btn_payment_phone': '📱 Телефон',
        'btn_payment_usdt':  '💎 Usdt',
        'btn_role_seller':   '🔥 Я продавец',
        'btn_role_buyer':    '🛒 Я покупатель',
        'deal_role_title':   '🧾 <b>Новая сделка</b>',
        'deal_role_question':'💬 <i>Кем вы выступаете в этой сделке?</i>',
        'deal_role_seller_desc': '🔥 <b>Продавец</b> — вы продаёте товар/услугу и получаете оплату.',
        'deal_role_buyer_desc':  '🛒 <b>Покупатель</b> — вы платите и получаете товар/услугу.',
        'not_specified':  'Не указан',
        'not_specified_f':'Не указана',
    },

    'en': {
        'welcome': """<b><tg-emoji emoji-id="5893255507380014983">💼</tg-emoji> Welcome to {BOT_NAME} Relayer <tg-emoji emoji-id="5357080225463149588">🤝</tg-emoji></b>
<blockquote><i><tg-emoji emoji-id="5456140674028019486">⚡️</tg-emoji> Your trusted P2P escrow service:</i>
\t<tg-emoji emoji-id="5794182096603847292">1⃣</tg-emoji> Automated deals with NFTs & Telegram gifts
\t<tg-emoji emoji-id="5794303034292968945">2⃣</tg-emoji> <tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Full protection for both buyer and seller
\t<tg-emoji emoji-id="5794031944547178894">3⃣</tg-emoji> <tg-emoji emoji-id="6039802097916974085">🪙</tg-emoji> Powerful bot &amp; web dashboard
\t<tg-emoji emoji-id="5793901252987330401">4⃣</tg-emoji> <tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> All items go through our manager: {MANAGER_USERNAME}</blockquote>
<tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji> Pick an option below <tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji>""",

        'verified_status': '\n<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Status:</b> Verified',

        # Main menu buttons
        'btn_create_deal': 'New deal',
        'btn_my_profile': 'Profile',
        'btn_balance_req': 'Balance & payouts',
        'btn_verification': 'Get verified',
        'btn_verification_done': 'Verified ✅',
        'btn_referrals': 'Referrals',
        'btn_change_lang': '🌐 Change language',
        'btn_my_tag': 'My tag',
        'btn_worker_panel': 'Worker panel',
        'btn_admin_panel': 'Admin panel',
        'btn_support': 'Support',
        'btn_verification_request': 'Verification request',
        'btn_appeals': 'Appeals',
        'appeals_menu_text': """<tg-emoji emoji-id="5956561916573782596">📄</tg-emoji> <b>{bot_name} Support Center</b>

<tg-emoji emoji-id="5931546553868095844">⚙️</tg-emoji> <b>Suggestions & ideas:</b>
• Feature improvement suggestions
• Ideas for new features
• Integration requests
• User experience feedback

<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>Complaints & claims:</b>
• Complaints about users
• Deal issues
• Technical problems
• Improper behavior
• Suspected fraud

<tg-emoji emoji-id="5904258298764334001">📞</tg-emoji> <b>Important information:</b>
• All requests are reviewed within 24 hours
• Confidentiality is guaranteed
• Fraud reports get an instant response
• Best suggestions get implemented in the bot

<tg-emoji emoji-id="5811989245761426317">💡</tg-emoji> Choose a section for your request:""",
        'appeal_suggest_text': """<tg-emoji emoji-id="5934504443772756682">✍️</tg-emoji> <b>Write your suggestion:</b>

<tg-emoji emoji-id="5893193062850499428">ℹ️</tg-emoji> Describe your idea in detail — how it will improve the bot and what benefits it brings to users.""",
        'appeal_complain_text': """<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> <b>Write your complaint:</b>

<tg-emoji emoji-id="5893193062850499428">ℹ️</tg-emoji> Please specify:
• User/deal ID
• Description of the issue
• Screenshots (if any)
• Desired resolution""",
        'withdraw_menu_text': """<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>Withdraw funds</b>

Choose a currency to withdraw:""",
        'withdraw_currency_text': """<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>Withdraw {currency}</b>

<b>Your balance:</b>
{bal_lines}
Enter the amount to withdraw in <b>{currency}</b>:
<i>Available: {cur_balance} {currency}</i>""",
        'verification_request_sent': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Request sent!</b>\n\nWe will review it shortly.',
        'btn_appeals_suggest': 'Suggest',
        'btn_appeals_complain': 'Complain',
        'btn_admin_appeals': 'Appeals & Complaints',
        'btn_appeals_suggestions': 'Suggestions',
        'btn_appeals_complaints': 'Complaints',
        'btn_appeal_reply': 'Reply',
        'btn_appeal_close': 'Close',
        'btn_my_mammoths': 'My customers',
        'btn_back_menu': 'Menu',
        'btn_back': 'Back',
        'btn_refresh': 'Refresh',
        'btn_my_deals': 'My deals',
        'btn_cancel': 'Cancel',
        'btn_send_receipt': 'Send receipt',
        'btn_confirm_withdraw': 'Confirm withdrawal',
        'btn_withdraw_item': 'Claim item',
        'btn_all_deals': 'All deals',
        'btn_to_admin': 'Admin panel',
        'btn_new_deal': 'New deal',

        # Payout setup
        'bind_requisites': """<tg-emoji emoji-id="5332455502917949981">🏦</tg-emoji> <b>Set up payout details</b>
<tg-emoji emoji-id="5447644880824181073">⚠️</tg-emoji> <b>You need at least one payout method to create a deal.</b>
Choose how you'd like to be paid:
<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> TON — TON wallet
<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> Bank card — for fiat payouts
<tg-emoji emoji-id="5343777479091831702">👛</tg-emoji> USDT — TRC-20 stablecoin
<tg-emoji emoji-id="5330319637156479518">📱</tg-emoji> Phone — for YooMoney / SBP
<tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji> <b>Pick a method</b> <tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji>""",

        'no_requisites_alert': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Add at least one payout method before creating a deal.',
        'blocked_alert': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> You are blocked and can\'t create deals.',

        # Deal creation
        'create_deal_title': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> <b>NEW DEAL</b>',
        'create_deal_text': """<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> New deal:
IMPORTANT: THIS APPLIES ONLY WHEN SELECTING "BUYER" AS YOUR ROLE
Select the currency for payment:""",

        'create_deal_text_seller': """<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> New deal:
Select the currency to receive payment:""",

        # Profits
        'profit_new': '<tg-emoji emoji-id="6039802097916974085">🪙</tg-emoji> <b>NEW PROFIT</b>',
        'profit_type': '<tg-emoji emoji-id="5197371802136892976">⛏</tg-emoji> <b>Type:</b>',
        'profit_amount': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> <b>Amount:</b>',
        'profit_desc': '<tg-emoji emoji-id="5197269100878907942">✍️</tg-emoji> <b>Note:</b>',
        'profit_deal': '<tg-emoji emoji-id="5195033767969839232">🚀</tg-emoji> <b>Deal:</b>',
        'profit_success': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Deal closed successfully!</b>',
        'profit_direct_transfer': 'Direct transfer',

        # Language
        'lang_select': '🌐 Choose your language / Выберите язык / 选择语言 / اختر اللغة:',
        'lang_ru': '<tg-emoji emoji-id="5449408995691341691">🇷🇺</tg-emoji> Русский',
        'lang_en': '🇬🇧 English',
        'lang_zh': '🇨🇳 中文',
        'lang_ar': '🇸🇦 عربي',

        # Alerts
        'already_verified': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> You\'re already verified!',
        'access_denied': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Access denied',
        'deal_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Deal not found',
        'deal_already_paid': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> This deal has already been paid or closed',
        'deal_not_paid': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> This deal hasn\'t been paid yet',
        'deal_no_buyer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> This deal has no buyer yet',
        'not_buyer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> You\'re not the buyer of this deal',
        'not_seller': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> You\'re not the seller of this deal',
        'insufficient_funds': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Insufficient balance',
        'tag_workers_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Tags are available to workers and admins only',
        'no_tag_set': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> You haven\'t set a tag yet',
        'workers_admins_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Workers and admins only',
        'choose_payment_first': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Choose a payment method first',
        'payment_confirmed': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Payment confirmed — profit recorded',
        'user_not_found': 'User not found',

        # Verification
        'verification_receipt_title': '📤 <b>SUBMIT VERIFICATION RECEIPT</b>',
        'verification_receipt_text': """📤 <b>SUBMIT VERIFICATION RECEIPT</b>

<b>Send a photo or document showing the payment.</b>

<b>The receipt must show:</b>
• A clear, readable image
• The amount paid
• The payment date
• Recipient details

<b>An admin will review it once you submit.</b>
<i>Review usually takes up to 15 minutes.</i>""",

        # Tags
        'tag_manage_title': '🏷️ <b>TAG SETTINGS</b>',
        'tag_current': '<b>Current tag:</b>',
        'tag_not_set': 'Not set',
        'tag_used_in_profits': '<b>Your tag will appear in profit reports instead of your username.</b>',
        'tag_example': '<i>Example: profit reports will show "{tag}" instead of an auto-generated name.</i>',
        'tag_auto_hint': '<i>Without a tag, the bot generates names like worker2035, worker2914, etc.</i>',
        'tag_choose_action': '<b>Choose an action:</b>',
        'tag_setup_title': '🏷️ <b>SET A TAG</b>',
        'tag_setup_text': """🏷️ <b>SET A TAG</b>

<b>Tag rules:</b>
• Must start with #
• Letters, digits and underscores only
• 2 to 20 characters
• Examples: #best_worker, #top_admin, #lolz_pro

<b>This tag appears in profit reports.</b>
<b>Without one, an auto-generated name is used.</b>

<b>Type your tag:</b>""",
        'tag_removed': '🗑️ <b>TAG REMOVED</b>',
        'tag_removed_text': """🗑️ <b>TAG REMOVED</b>

<b>Removed:</b> {tag}
<b>Profit reports will now use an auto-generated name.</b>
<i>You can set a new tag any time.</i>""",
        'btn_set_tag': 'Set tag',
        'btn_remove_tag': 'Remove tag',
        'btn_set_new_tag': 'Set new tag',

        # Items
        'items_title': '<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>MY ITEMS</b>',
        'items_empty': '<b>No items yet.</b>',
        'items_hint': '<i>Items show up here after a deal closes where you were the buyer.</i>',
        'items_how_to': '<b>How to get items:</b>',
        'no_items_withdraw': '📭 <b>Nothing to claim</b>\n\nYou don\'t have any unclaimed items.',

        # Claim item
        'withdraw_title': '📤 <b>CLAIM ITEM</b>',
        'withdraw_text': """📤 <b>CLAIM ITEM</b>

<b>Item ID:</b> <code>{item_id}</code>
<b>To claim this item, contact our manager:</b>
👉 {MANAGER_USERNAME}

<b>Send them the item ID and follow their instructions.</b>
<i>Verified users get priority service and 0% fee.</i>

<b>Confirm claim:</b>""",

        # Product category
        'category_title': """<tg-emoji emoji-id="5433653135799228968">📁</tg-emoji> <b>PICK A CATEGORY</b>

<b>Available types:</b>
• <tg-emoji emoji-id="6037175527846975726">🎁</tg-emoji> Gift — Telegram gifts, stickers
• 🏷️ NFT username — usernames and collections
• <tg-emoji emoji-id="5771695636411847302">📢</tg-emoji> Channel / chat — Telegram channels & groups
• <tg-emoji emoji-id="6028338546736107668">⭐</tg-emoji> Stars — Telegram Stars
• <tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> Other — anything else

<b>Pick one:</b>""",

        # Payment
        'payment_confirmed_buyer': """<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>PAYMENT CONFIRMED</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Deal:</b> #{deal_id}
<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Charged from balance:</b> {amount} {currency}
<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>Balance left:</b> {balance} {currency}

<b>Waiting for the seller to hand off the item.</b>
<i>This usually takes up to 15 minutes.</i>

<b>Reminder:</b> all items are escrowed through our manager.
The seller transfers the item to {MANAGER_USERNAME} and you'll be notified once we verify it.""",

        'payment_received_seller': """<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>PAYMENT RECEIVED</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Deal:</b> #{deal_id}
<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>Buyer:</b> @{buyer}
<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Buyer verified:</b> {verified}
<tg-emoji emoji-id="5811989245761426317">💸</tg-emoji> <b>Amount:</b> {amount} {currency}

<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Funds added to your balance.</b>
The buyer paid from their wallet — now hand off the item to our manager.

<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji>️ <b>Critical rule:</b>
Transfer the item ONLY to {MANAGER_USERNAME}. Never directly to the buyer.

<b>Once you've sent it, tap the button below:</b>""",

        'btn_sent_item': 'Item sent',

        # Deal created
        'deal_created': """<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>DEAL CREATED</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Deal ID:</b> #{deal_id}
<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Amount:</b> {amount} {currency}
<tg-emoji emoji-id="5433653135799228968">📁</tg-emoji> <b>Category:</b> {category}
<b>Link / description:</b> {description}
<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>Seller:</b> @{seller}
<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Seller verified:</b> {verified}

<b>Buyer link:</b>
{link}

<b>Share this link with the buyer:</b>
{link}

<i>The deal starts as soon as the buyer opens it.</i>""",

        # warning_title / btn_support_manager / btn_to_buyer удалены вместе с warning-викториной (ТЗ 2026-05-10)

        # Withdrawal errors
        'withdrawal_error': """<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>Couldn't process the claim</b>

Something went wrong while processing your item claim. Please reach out to support: {MANAGER_USERNAME}""",
        'balance_withdrawal_error': """<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>Couldn't process the withdrawal</b>

Something went wrong while processing your withdrawal. Please reach out to support: {MANAGER_USERNAME}""",

        # Deal completed
        'deal_completed_buyer': """<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>DEAL CLOSED</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Deal ID:</b> #{deal_id}
<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Amount:</b> {amount} {currency}
<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>Seller:</b> @{seller}
<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>Item:</b> {description}

<b>What's next:</b>
• Item is now in "My Items"
• Claim it whenever you're ready
• Profile → My Items → pick it → claim

💙 Thanks for using {BOT_NAME} Relayer!""",

        'deal_completed_seller': """<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>DEAL CLOSED</b>

<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Deal ID:</b> #{deal_id}
<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>Amount:</b> {amount} {currency}
<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>Buyer:</b> @{buyer}
<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>Item:</b> {description}

<b>What's next:</b>
• Item delivered to the buyer
• Funds are settled

💙 Thanks for using {BOT_NAME} Relayer!""",

        # Profile
        'profile_title': '<b>🏆 {BOT_NAME} Relayer — PROFILE</b>',
        'deals_empty': '📭 <b>NO ACTIVE DEALS</b>\n\nTap the button below to create your first one.',
        'deals_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>YOUR ACTIVE DEALS</b>',
        'deals_select': 'Pick a deal to manage:',

        # Roles
        'role_user': '<tg-emoji emoji-id="5886412370347036129">👤</tg-emoji> User',
        'role_owner': '<tg-emoji emoji-id="5807868868886009920">👑</tg-emoji> System owner',
        'role_admin': '⚙️ Administrator',
        'role_worker': '👷 Worker',
        'role_blocked': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> (Blocked)',
        'verified_yes': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Verified',
        'verified_no': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Not verified',

        # Amount entry
        'enter_amount': '<tg-emoji emoji-id="5811989245761426317">💰</tg-emoji> <b>Enter the deal amount:</b>',
        'invalid_amount': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>INVALID AMOUNT</b>\n\nEnter a number, e.g. 1500 or 5.75',
        'amount_zero': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>AMOUNT MUST BE GREATER THAN ZERO</b>',
        'description_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>LINK / DESCRIPTION IS TOO SHORT</b>\n\nAt least 5 characters.',

        # Profit directions
        'direction_sell': 'Sold item to customer',
        'direction_buy': 'Bought item from customer',
        'direction_ad': 'Bot referral profit',
        'direction_deposit': 'Customer balance top-up',

        # Balance
        'balance_deposit': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>BALANCE TOPPED UP</b>',
        'deposit_confirmed': """<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>BALANCE TOPPED UP</b>

<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> <b>Amount:</b> {amount} {currency}
<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>Current balance:</b> {balance} {currency}

<b>What's next:</b>
• Funds are now on your balance
• Use them to pay for any deal
• For withdrawals, message support

💙 Thanks for using {BOT_NAME} Relayer!""",

        # Verification info
        'verification_info': """<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> {BOT_NAME} Verification

<tg-emoji emoji-id="5447644880824181073">🎯</tg-emoji> <b>What premium status gives you:</b>
• <tg-emoji emoji-id="5902016123972358349">🔐</tg-emoji> Seller verification — a trust badge
• <tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Deal guarantee — protection from scammers
• <tg-emoji emoji-id="5773677501825945508">⚡️</tg-emoji> Priority support — fast responses
• <tg-emoji emoji-id="5895444149699612825">📈</tg-emoji> Reduced commission — 0.5% instead of 1%
• <tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> Fast payouts — within 1 hour
• <tg-emoji emoji-id="5413879192267595313">🎁</tg-emoji> Referral bonuses — +10% to balance

<tg-emoji emoji-id="5902016123972358349">🔒</tg-emoji> <b>Security:</b>
• All data encrypted
• Deal insurance
• Legal protection
• 24/7 monitoring

<tg-emoji emoji-id="5895444149699612825">📈</tg-emoji> <b>Advantages:</b>
• Increased buyer trust
• More successful deals
• Personal manager
• Exclusive offers

<tg-emoji emoji-id="5936017305585586269">🔰</tg-emoji> For more details, contact support""",

        'verification_info_verified': """<tg-emoji emoji-id="5902016123972358349">🔒</tg-emoji> Verification

<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> Your account is verified.
Status granted after review by {BOT_NAME} security team.""",

        # Stats
        'stats_title': '<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>{BOT_NAME} Relayer — STATS</b>',
        'stats_advantages': """⭐ <b>The platform keeps growing.</b>
<i>Join the community.</i>

💙 <b>Why {BOT_NAME} Relayer:</b>
• <tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Real escrow on every deal
• <tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> Fast payouts
• <tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> Best rates around
• 📞 24/7 support
• <tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> Built-in verification

🤍 <b>Built with our users.</b>""",

        # Payout method labels
        'requisites_card': '<tg-emoji emoji-id="5967548335542767952">💳</tg-emoji> Card',
        'requisites_ton': '⚡ TON',
        'requisites_phone': '📱 Phone',
        'requisites_usdt': '<tg-emoji emoji-id="5963312935148195483">💎</tg-emoji> USDT',
        'not_specified': 'Not set',
        'not_specified_f': 'Not set',

        # Worker panel buttons
        'btn_my_stats': 'My stats',
        'btn_my_deals_worker': 'My deals',
        'btn_fake_deals': 'Fake deals',
        'btn_fake_balance': 'Fake balance',
        'btn_remove_deals': 'Remove deals',
        'btn_trim_profile': 'Reset profile',
        'btn_change_rating': 'Change rating',

        # Items menu
        'items_total': 'Total items:',
        'items_pending': 'Unclaimed:',
        'items_withdrawn': 'Claimed:',
        'items_pending_title': 'UNCLAIMED:',
        'items_withdrawn_title': 'CLAIMED:',
        'items_item': 'Item',
        'items_desc': 'Description',
        'items_received': 'Received',
        'items_withdrawn_at': 'Claimed',
        'items_unknown': 'Unknown',
        'items_how_to_steps': """1. Find a seller and open a deal
2. Pay it from your balance
3. Once the seller delivers — the item shows up here
4. Claim it whenever you want""",

        # Claim menu
        'withdraw_menu_title': 'CLAIM AN ITEM',
        'withdraw_items_waiting': 'items waiting to be claimed',
        'withdraw_select': 'Pick an item or paste its ID:',

        # Balance withdraw
        'balance_withdraw_title': 'WITHDRAW FUNDS',
        'balance_your': 'Your balance:',
        'balance_enter_amount': 'How much do you want to withdraw, and in which currency?',
        'balance_min': 'Minimum amount:',
        'balance_contact_support': 'Once you submit the request, message support to finish.',
        'btn_to_profile': 'Profile',

        # Verification menu buttons
        'btn_pay_card': 'RU card',
        'btn_pay_usdt': 'USDT',
        'btn_pay_kzt': 'KZT',
        'btn_pay_byn': 'BYN',
        'btn_pay_stars': 'Stars',

        # Product categories
        'cat_gift': '🎁 Gift',
        'cat_nft': '🏷️ NFT username',
        'cat_channel': '<tg-emoji emoji-id="5771695636411847302">📢</tg-emoji> Channel / chat',
        'cat_stars': '<tg-emoji emoji-id="6028338546736107668">⭐</tg-emoji> Stars',
        'cat_other': '📦 Other',
        'desc_gift_title': '📝 <b>GIFT LINK</b>',
        'desc_gift_text': """📝 <b>GIFT LINK</b>

<b>Category:</b> {category}

<b>Paste the gift link:</b>
• Just send the link
• Example: https://t.me/nft/EasterEgg-158557
• Make sure the gift is available

<b>Important:</b> Make sure the link is correct and leads to the exact item you're selling!

<b>Enter the link:</b>""",
        'desc_stars_text': """📝 <b>ITEM DESCRIPTION</b>

<b>Category:</b> {category}

<b>Describe in detail what you're selling:</b>
• Number of Stars
• Platform (iOS/Android/Web)
• Additional terms
• Delivery method

<b>Example:</b>
"1000 Telegram Stars for iOS, delivered via bot"

<b>Please be as detailed and honest as possible!</b>

<b>Enter the description:</b>""",
        'desc_other_text': """📝 <b>ITEM DESCRIPTION</b>

<b>Category:</b> {category}

<b>Describe in detail what you're selling:</b>
• Item name
• Quantity
• Delivery terms
• Additional info
• Item condition

<b>Please be as detailed and honest as possible!</b>

<b>Enter the description:</b>""",
        'desc_default_text': """📝 <b>ITEM DESCRIPTION</b>

<b>Category:</b> {category}

<b>Describe in detail what you're selling:</b>
• For NFT tags: tag name, network, rarity
• For channels/chats: link, subscriber count, topic
• Delivery terms

<b>Please be as detailed and honest as possible!</b>

<b>Enter the description:</b>""",

        # Profile labels
        'profile_name': 'Name:',
        'profile_rating': 'Rating:',
        'rating_no_deals': 'no deals yet',
        'profile_success_deals': 'Closed deals:',
        'profile_disputes_won': 'Disputes won:',
        'profile_active_deals': 'Active deals:',
        'profile_balance': 'Balance:',

        # Deals list
        'deals_role_seller': '🛒 Seller',
        'deals_role_buyer': '<tg-emoji emoji-id="5811989245761426317">💰</tg-emoji> Buyer',
        'deals_buyer_label': 'Buyer:',
        'deals_seller_label': 'Seller:',
        'deals_awaiting': 'Pending',
        'deals_more': '+{count} more deals…',
        'deals_deal': 'Deal',

        # Deal view
        'deal_view_seller_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>YOUR DEAL</b>',
        'deal_view_buyer_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>YOUR DEAL</b>',
        'deal_view_id': '<b>ID:</b>',
        'deal_view_status': '<b>Status:</b>',
        'deal_view_category': '<b>Category:</b>',
        'deal_view_desc': '<b>Item / link:</b>',
        'deal_view_amount': '<b>Amount:</b>',
        'deal_view_payment_method': '<b>Payment method:</b>',
        'deal_view_your_verification': '<b>You verified:</b>',
        'deal_view_buyer_link': '<b>Buyer link:</b>',
        'deal_view_buyer': '<b>Buyer:</b>',
        'deal_view_send_link': '<b>Share this link with the buyer:</b>',
        'deal_view_seller': '<b>Seller:</b>',
        'deal_view_seller_rating': '<b>Seller rating:</b>',
        'deal_view_seller_verification': '<b>Seller verified:</b>',
        'deal_view_pay_from_balance': '<b>Payment will be charged from your balance.</b>',
        'deal_status_awaiting_buyer': 'Waiting for buyer',
        'deal_status_awaiting_payment': 'Waiting for payment',
        'deal_status_paid': 'Paid',
        'deal_buyer_awaiting': 'Pending',
        'deal_category_default': 'Item',
        'deal_verified_yes': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Yes',
        'deal_verified_no': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> No',

        # Buyer joined
        'buyer_joined_seller': """<b><tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> @{buyer} joined deal #{deal_id}</b>

<blockquote><tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> Once the payment lands you'll get a ping — then hand the item off to our manager.</blockquote>

<blockquote>📈 Seller's closed deals: {success_deals}</blockquote>

<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Items go ONLY through {manager}. Never hand them directly to the buyer.

❗️ Watch for the payment notification in the bot.""",

        'buyer_joined_buyer': """<b><tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> Seller @{seller} joined deal #{deal_id}</b>

<blockquote><tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> Pay through our manager: {manager}</blockquote>

<blockquote>📈 Seller's closed deals: {success_deals}</blockquote>

<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Payments go ONLY through {manager}. Never pay the seller directly.

❗️ Double-check the payout details before sending money.

<b>Item / link:</b> {description}

<tg-emoji emoji-id="5811989245761426317">💸</tg-emoji> <b>Amount:</b> {amount} {currency}""",

        # Balance & payout details
        'balance_req_title': '<b><tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> BALANCE & PAYOUTS</b>',
        'balance_your_title': '<b>Your balance:</b>',
        'requisites_your_title': '<b>Your payout details:</b>',
        'requisites_crypto_label': 'Crypto wallet',
        'requisites_card_label': 'Card',
        'requisites_phone_label': 'Phone',
        'balance_choose_action': '<b>What do you want to do?</b>',
        'not_specified_req': 'Not set',
        'btn_deposit_balance': 'Deposit',
        'btn_withdraw_balance': 'Withdraw',
        'btn_ton_wallet': 'TON wallet',
        'btn_card_req': 'Card',
        'btn_phone_req': 'Phone',
        'btn_usdt_wallet': 'USDT wallet',

        # Referral
        'referral_title': '<b><tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> Referral program</b>',
        'referral_percent': 'Your share',
        'referral_invited': 'Invited users',
        'referral_balance_ton': 'TON earned',
        'referral_balance_usdt': 'USDT earned',
        'referral_link_label': '<b>Your referral link:\n\n{ref_link}</b>',
        'btn_copy_link': 'Copy',

        # Buttons for deals
        'btn_pay_balance': 'Pay from balance',
        'btn_open_dispute': 'Open dispute',
        'btn_my_deals_nav': 'My deals',
        'btn_deal_link': 'Deal',

        # Deposit
        'deposit_select_currency_text': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> Balance top-up\n\nSelect a currency to deposit:',
        'deposit_currency_title_prefix': 'Top up balance',
        'deposit_currency_support_hint': 'Get deposit details from support.\n<tg-emoji emoji-id="5447644880824181073">❗️</tg-emoji> Funds are credited to your balance after top-up.',
        'deposit_title': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>DEPOSIT</b>',
        'deposit_choose': '<b>Pick a deposit method:</b>',
        'deposit_card_ru': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> RU card — deposit in RUB',
        'deposit_card_ua': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> UA card — deposit in UAH',
        'deposit_crypto': '₿ Crypto — BTC, ETH, USDT, TON, BNB, SOL',
        'deposit_stars': '⭐ Telegram Stars — deposit in Stars',
        'deposit_after': '<b>Once you pick a method, the payment details will appear.</b>',
        'deposit_important': '<b>Important:</b> after sending the payment, hit "📤 Send receipt" so we can credit your balance.',
        'deposit_verified_hint': '<i>Verified users get priority processing.</i>',
        'deposit_amount_title': '<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>ENTER DEPOSIT AMOUNT</b>',
        'deposit_method_label': '<b>Method:</b>',
        'deposit_currency_label': '<b>Currency:</b>',
        'deposit_min': '• Minimum amount:',
        'deposit_unlimited': 'unlimited',
        'deposit_after_amount': '<b>After entering the amount you will be able to send the receipt.</b>',
        'deposit_instructions': '<b>Instructions:</b>',
        'deposit_instruction_1': '1. Transfer the specified amount using the details above',
        'deposit_instruction_1_crypto': '1. Transfer {name} to the specified address',
        'deposit_instruction_2': '2. Save the receipt/screenshot of the transfer',
        'deposit_instruction_3': '3. Click the "📤 Send receipt" button',
        'deposit_instruction_4': '4. Attach a photo or document as confirmation',
        'deposit_instruction_5': '5. After admin verification funds will be added to your balance',
        'deposit_important_note': '<b>Important:</b> Without sending the receipt your deposit will not be processed!',
        'deposit_requisites_label': '<b>Payment details ({name}):</b>',
        'deposit_support_contact': 'Contact support for current payment details: {support}',
        'deal_amount_title': '<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> Creating a deal\n\n<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> Enter the deal amount:',
        'deal_amount_examples': '<tg-emoji emoji-id="5795328215886894640">📌</tg-emoji> Example: 2000.50',
        'deal_amount_min': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> Enter the exact amount to avoid processing errors.',
        'deal_amount_min_stars': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> Enter the number of Stars.',
        'deal_amount_enter': '',
        'deal_amount_too_small': '<tg-emoji emoji-id="5922712343011135025">❌</tg-emoji> <b>AMOUNT TOO SMALL</b>\n\nMinimum: {min_amount} {currency}',
        'deal_created_title': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>DEAL CREATED!</b>',
        'deal_gifts_count': '<b>Gifts in deal:</b>',
        'deal_send_link_buyer': '<b>Send this link to the buyer:</b>',
        'deal_started_when': '<i>Once the buyer follows the link, the deal will start.</i>',
        'deal_seller_label': '<tg-emoji emoji-id="6041705726206808304">👤</tg-emoji> <b>Seller:</b>',
        'deal_seller_verif': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>Seller verification:</b>',
        'card_ru_name': 'RU Card',
        'card_ua_name': 'UA Card',
        'not_specified_val': 'Not specified',
        'deposit_reason_none': 'Not specified (contact the user for clarification)',
        'requisites_card_btn': 'Card',
        'requisites_phone_btn': 'Phone',

        # Deal view
        'deal_info_title': '<b>📋 DEAL DETAILS</b>',
        'deal_status_label': '<b>Status:</b>',
        'deal_status_created': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> Awaiting payment',
        'deal_status_paid': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> Paid',
        'deal_status_completed': '<tg-emoji emoji-id="5893193062850499428">📱</tg-emoji> Closed',
        'deal_status_disputed': '<tg-emoji emoji-id="5922712343011135025">❌</tg-emoji> Disputed',
        'deal_buyer_awaiting': 'Pending',
        'deal_send_link': '<b>Share this link with the buyer:</b>',
        'deal_buyer_prompt': '<b>Tap the button below to pay.</b>',

        # Seller sent item
        'seller_sent_item': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>ITEM SENT</b>',
        'seller_sent_wait': '<b>Sit tight — we\'re verifying it on our side.</b>',

        # Verification payment
        'verification_pay_title': '🔰 <b>VERIFICATION ({method})</b>',
        'verification_pay_cost': '<b>Fee:</b> {price} {currency}',
        'verification_pay_after': '<b>After paying, hit "📤 Send receipt" and attach proof.</b>',
        'verif_receipt_text': '📤 <b>SUBMIT VERIFICATION RECEIPT</b>\n\nSend a photo or document confirming the payment.\n\n<b>Receipt requirements:</b>\n• Clear image\n• Amount is visible\n• Date is visible\n• Recipient details are visible\n\n<b>Once submitted, the admin will review it and confirm your verification.</b>\n<i>Review usually takes up to 15 minutes.</i>',
        'verif_pay_card_msg': '🔰 <b>VERIFICATION PAYMENT (RU CARD)</b>\n\n<b>Fee:</b> {price} RUB\n{details}\n\n<b>Once you\'ve paid, tap "📤 Send receipt" and attach the proof.</b>',
        'verif_pay_usdt_msg': '🔰 <b>VERIFICATION PAYMENT (USDT TRC-20)</b>\n\n<b>Fee:</b> {price} USDT\n{details}\n\n<b>Once you\'ve paid, tap "📤 Send receipt" and attach the proof.</b>',
        'verif_pay_simple_msg': '🔰 <b>VERIFICATION PAYMENT ({method})</b>\n\n<b>Fee:</b> {price} {currency}\nReach out to support to confirm the payment details.\n\n<b>How it works:</b>\n1. Message {MANAGER_USERNAME} to pay.\n2. Once the admin reviews it, the amount lands on your balance.',
        'verif_pay_stars_msg': '🔰 <b>VERIFICATION PAYMENT (Stars)</b>\n\n<b>Fee:</b> {price} Stars\nSend the Stars to the support account.\nNetwork: Stars\n\n<b>How it works:</b>\n1. Send the Stars to the support account ({MANAGER_USERNAME}).\n2. Once the admin reviews it, the amount lands on your balance.',

        # Error messages
        'error_own_deal': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> You can\'t join your own deal as a buyer.',
        'error_deal_taken': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Another buyer has already taken this deal.',

        # Wallet updates
        'wallet_crypto_title': '<tg-emoji emoji-id="5992430854909989581">🪙</tg-emoji> <b>CRYPTO WALLET</b>',
        'wallet_send_crypto': '<b>Send the wallet address and network in one message:</b>',
        'wallet_crypto_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>CRYPTO WALLET UPDATED</b>',
        'wallet_new_crypto': '<b>New details:</b>',
        'wallet_crypto_hint': """• One message: wallet address and network
• Example: UQAbc123...xyz, network Ton
• Example: TXaBc123...xyz, network Trc-20
<i>Details will be saved for receiving crypto payments</i>""",
        'wallet_ton_title': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> <b>TON WALLET</b>',
        'wallet_card_title': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> <b>BANK CARD</b>',
        'wallet_phone_title': '<tg-emoji emoji-id="5330319637156479518">📱</tg-emoji> <b>PHONE NUMBER</b>',
        'wallet_usdt_title': '<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> <b>USDT WALLET</b>',
        'wallet_current': '<b>Current address:</b>',
        'wallet_current_card': '<b>Current details:</b>',
        'wallet_current_phone': '<b>Current number:</b>',
        'wallet_send_new': '<b>Send the new wallet address:</b>',
        'wallet_send_card': '<b>Send new card details:</b>',
        'wallet_send_phone': '<b>Send the phone number:</b>',
        'wallet_send_usdt': '<b>Send a TRC-20 USDT address:</b>',
        'wallet_ton_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>TON WALLET UPDATED</b>',
        'wallet_card_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>BANK CARD UPDATED</b>',
        'wallet_phone_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>PHONE NUMBER UPDATED</b>',
        'wallet_usdt_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>USDT WALLET UPDATED</b>',
        'wallet_new_address': '<b>New address:</b>',
        'wallet_new_card': '<b>New details:</b>',
        'wallet_new_phone': '<b>New number:</b>',
        'wallet_card_note': '<b>You can now accept ruble payments to this card.</b>\n<i>Buyers will see these details automatically.</i>',
        'wallet_phone_note': '<b>You can now accept SBP / YooMoney payments to this number.</b>\n<i>Make sure the number is active and linked to a wallet.</i>',
        'wallet_usdt_note': '<b>You can now accept USDT (TRC-20) payments here.</b>\n<i>Double-check the address is on the TRC-20 network.</i>',
        'btn_all_requisites': 'All payout details',
        'wallet_menu_title': """🏦 <b>MANAGE PAYMENT DETAILS</b>

<b>Set up your payment details:</b>
• <tg-emoji emoji-id='5992430854909989581'>🪙</tg-emoji> Crypto wallet — address and network (Ton, Trc-20, etc.)
• <tg-emoji emoji-id='5445353829304387411'>💳</tg-emoji> Card — to receive rubles and other currencies
• 📱 Phone — in international format

<b>Note:</b> Stars don't require payment details

<b>Important:</b> Only enter verified payment details!

<b>Choose the type:</b>""",
        'wallet_ton_hint': """• Format: UQ... or EQA...
• Double-check the address
• Must start with UQ or EQ
<i>Address will be saved for receiving payments</i>""",
        'wallet_card_hint': """• Format: 2200 1234 5678 9010
• Or: Bank — Card number
• Supports cards from RU, BY, KZ, UA
<i>Details will be saved for receiving ruble payments</i>""",
        'wallet_phone_hint': """• Format: +79991234567
• Used for Qiwi/юmoney
• Include country code
<i>Number will be saved for receiving payments</i>""",
        'wallet_usdt_hint': """• Format: T... (TRC20 network)
• Double-check the address
• TRC20 network only!
<i>Address will be saved for receiving Usdt</i>""",

        # Admin panel buttons & messages
        'btn_add_worker': 'Add worker',
        'btn_remove_worker': 'Remove worker',
        'btn_check_deals': 'Check deals',
        'btn_demote_worker': 'Demote worker',
        'btn_export_csv': 'Export to CSV',
        'btn_worker_panel_nav': 'Worker panel',
        'btn_admin_panel_nav': 'Admin panel',
        'btn_all_deals': 'All deals',
        'btn_stats': 'Statistics',
        'btn_my_profile_nav': 'My profile',
        'btn_my_items': 'My items',
        'btn_my_deals_nav2': 'My deals',
        'btn_manage_tag': 'Tag management',
        'btn_to_profile': 'To profile',
        'btn_to_worker_panel': 'Worker panel',
        'btn_confirm_withdraw': 'Confirm withdrawal',
        'btn_confirm_deposit': 'Confirm deposit',
        'btn_decline': 'Decline',
        'btn_verify_user': 'Verify',
        'btn_unverify_user': 'Remove verification',
        'btn_add_balance': 'Add',
        'btn_set_balance': 'Set',
        'btn_deduct_balance': 'Deduct',
        'btn_trim_deals': 'Trim deals',
        'btn_trim_balance': 'Trim balance',
        'btn_remove_admin': 'Remove admin',
        'btn_profile_view': 'Profile',
        'btn_demote': 'Demote',
        'btn_select_other': 'Select another',
        'btn_to_list': 'To list',
        'btn_new_broadcast': 'New broadcast',
        'btn_new_message': 'New message',
        'btn_try_again': 'Try again',
        'btn_recipient_list': 'Recipient list',
        'btn_not_paid': 'Not paid',
        'btn_not_sent': 'Not sent',
        'btn_wrong_item': 'Wrong item',
        'btn_other_reason': 'Other',
        'dispute_title': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>OPENING A DISPUTE</b>',
        'dispute_deal': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>Deal:</b>',
        'dispute_role': "<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>Your role:</b>",
        'dispute_role_buyer': 'Buyer',
        'dispute_role_seller': 'Seller',
        'dispute_support': '👨\u200d💼 <b>Deal support:</b>',
        'dispute_confirm': '<b>Are you sure you want to open a dispute?</b>\n<i>An administrator will review your dispute within 24 hours.</i>',
        'dispute_reason': '<b>Select reason:</b>',
        'btn_contact_manager': 'Contact manager',
        'btn_to_deal': 'To deal',
        'btn_deal_complete_profit': 'Complete with profit',
        'btn_update': 'Update',
        'btn_contact_support': 'Support',
        'btn_balance_manage': 'Balance management',

        # Admin alerts
        'admin_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Admins only.',
        'admin_complete_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Only admins can close deals.',
        'admin_confirm_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Only admins can confirm item receipt.',
        'owner_only_admins': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Only the system owner can view the admin list.',
        'owner_only_add_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Only the system owner can add admins.',
        'owner_only_remove_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Only the system owner can remove admins.',
        'admin_block_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Only admins can manage blocks.',
        'cannot_block_owner': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> You can\'t block the system owner.',
        'already_blocked': '⚠️ User is already blocked.',
        'owner_unblock_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Only the system owner can unblock the owner.',
        'not_blocked': '⚠️ User isn\'t blocked.',
        'user_not_worker': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> User isn\'t a worker.',
        'method_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Method not found.',
        'error_generic': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Error',
        'deposit_approved': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Deposit approved.',
        'deposit_error': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Couldn\'t approve the deposit.',
        'deposit_declined': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Deposit declined.',
        'deposit_declined_user': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Your deposit was declined by an admin. Reach out to support for details.',
        'user_verified_alert': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> User verified.',
        'user_unverified_alert': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Verification removed.',
        'data_saved': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Saved.',
        'you_are_blocked': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> You\'re blocked.',
        'export_in_dev': '📥 Export is still in development.',
        'lang_changed': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> Language updated.',
        'payment_not_supported': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> This payment flow is retired — pay from your balance instead.',

        # Admin error messages
        'invalid_id_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>INVALID ID</b>\n\nEnter a whole number.',
        'invalid_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>INVALID FORMAT</b>',
        'invalid_amount_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>INVALID AMOUNT</b>\n\nEnter a number, e.g. 1000 or 0.01.',
        'invalid_currency': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>INVALID CURRENCY</b>',
        'user_not_found_id': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>USER NOT FOUND</b>',
        'cannot_block_owner_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>CAN\'T BLOCK THE SYSTEM OWNER</b>',
        'cannot_remove_owner': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>CAN\'T REMOVE THE SYSTEM OWNER</b>',
        'cannot_add_owner_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>CAN\'T ADD THE SYSTEM OWNER AS AN ADMIN</b>',
        'edit_cancelled': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>Edit cancelled.</b>',
        'method_not_found_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>Method not found.</b>',
        'send_receipt_first': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Pick a deposit method and enter the amount first.',
        'send_photo_doc': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Send a photo or document with the receipt.',
        'deal_deleted': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>DEAL NOT FOUND</b>\n\nIt was deleted or never existed.',
        'scam_desc_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>DESCRIPTION TOO SHORT</b>\n\nGive at least 3 characters.',
        'deal_complete_error': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>FAILED TO CLOSE DEAL</b>',
        'amount_negative': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>INVALID AMOUNT</b>\n\nMust be greater than 0.',
        'amount_too_small': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>AMOUNT TOO SMALL</b>',
        'insufficient_funds_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>INSUFFICIENT FUNDS</b>',
        'tag_must_start_hash': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>TAGS MUST START WITH #</b>\n\nExample: #best_worker',
        'tag_too_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>TAG TOO SHORT</b>\n\nAt least 2 characters (including #).',
        'tag_too_long': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>TAG TOO LONG</b>\n\nMax 20 characters.',
        'tag_already_used': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>TAG ALREADY TAKEN</b>',
        'no_recipients': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>NO RECIPIENTS</b>\n\nNo one matches the chosen broadcast type.',
        'verified_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>No verified users yet.</b>',
        'deals_not_found_search': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>NO DEALS FOUND</b>',
        'users_not_found_search': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>NO USERS FOUND</b>',
        'bot_error': 'Bot error.',
        'access_denied_block': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ACCESS DENIED</b>\n\nAdmins only.',
        'access_denied_unblock': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ACCESS DENIED</b>\n\nAdmins only.',
        'access_denied_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ACCESS DENIED</b>\nYou don\'t have admin rights.',
        'deals_negative': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Deal count can\'t be negative.',
        'enter_integer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Enter a whole number.',
        'amount_negative_balance': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> Amount can\'t be negative.',

        # UI keyboard buttons (admin/worker/user-facing)
        'btn_deposit_card_ru': 'RU card',
        'btn_deposit_card_ua': 'UA card',
        'btn_deposit_crypto': 'Crypto',
        'btn_deposit_stars': 'Telegram Stars',
        'btn_admin_stats': 'Stats',
        'btn_admin_users': 'Users',
        'btn_admin_all_deals': 'All deals',
        'btn_admin_deal_activities': 'Deal activity',
        'btn_admin_user_activities': 'User activity',
        'btn_admin_broadcast': 'Broadcast',
        'btn_admin_workers_list': 'Workers',
        'btn_admin_private_msg': 'DM a user',
        'btn_admin_add_worker': 'Add worker',
        'btn_admin_remove_worker': 'Remove worker',
        'btn_admin_check_deals': 'Audit deals',
        'btn_admin_demote_worker': 'Demote',
        'btn_admin_fake_deals': 'Fake deals',
        'btn_admin_fake_balance': 'Fake balance',
        'btn_admin_balance_mgmt': 'Balance ops',
        'btn_admin_block_mgmt': 'Blocks',
        'btn_admin_verif_requests': 'Verification queue',
        'btn_admin_verif_mgmt': 'Verification ops',
        'btn_admin_deposit_req': 'Deposit details',
        'btn_admin_admins_list': 'Admins',
        'btn_admin_add_admin': 'Add admin',
        'btn_admin_remove_admin': 'Remove admin',
        'btn_admin_system_info': 'Info',
        'btn_admin_commands': 'Admin commands',
        'btn_verify_user_action': 'Verify user',
        'btn_unverify_user_action': 'Unverify',
        'btn_verified_list': 'Verified users',
        'btn_search_by_id': 'Search by ID',
        'btn_add_balance_action': 'Add balance',
        'btn_set_balance_action': 'Set balance',
        'btn_deduct_balance_action': 'Deduct',
        'btn_check_balance': 'Check balance',
        'btn_block_user': 'Block',
        'btn_unblock_user': 'Unblock',
        'btn_blocked_list': 'Blocked',
        'btn_no_blocked': 'Nobody blocked',
        'btn_no_admins': 'No admins',
        'btn_no_deals': 'No deals',
        'btn_no_deal_activities': 'No active deals',
        'btn_search_deal': 'Search deal',
        'btn_broadcast_all': 'Everyone',
        'btn_broadcast_workers': 'All workers',
        'btn_broadcast_admins': 'All admins',
        'btn_broadcast_user': 'One user',
        'btn_write_user': 'Message user',
        'btn_recipient_list_admin': 'Recipients',
        'btn_prev': 'Back',
        'btn_next': 'Next ➡️',
        'btn_owner_label': 'Owner',
        'btn_admin_label': 'Admin',
        'btn_remove_worker_confirm': 'Remove worker',
        'btn_demote_confirm': 'Demote',
        'btn_check_deals_worker': 'Audit deals',
        'btn_worker_stats': 'Stats',
        'btn_card_short': 'Card',
        'btn_phone_short': 'Phone',
        'btn_payment_ton':   '⚡ Ton',
        'btn_payment_crypto': '🪙 Crypto wallet',
        'btn_payment_card':  '💳 Card',
        'btn_payment_phone': '📱 Phone',
        'btn_payment_usdt':  '💎 Usdt',
        'btn_role_seller':   '🔥 I am seller',
        'btn_role_buyer':    '🛒 I am buyer',
        'deal_role_title':   '🧾 <b>New deal</b>',
        'deal_role_question':'💬 <i>What is your role in this deal?</i>',
        'deal_role_seller_desc': '🔥 <b>Seller</b> — you sell a product/service and receive payment.',
        'deal_role_buyer_desc':  '🛒 <b>Buyer</b> — you pay and receive the product/service.',
        'not_specified':  'Not set',
        'not_specified_f':'Not set',
    },
    'zh': {
        'welcome': '<b><tg-emoji emoji-id="5893255507380014983">💼</tg-emoji> 欢迎来到 {BOT_NAME} Relayer <tg-emoji emoji-id="5357080225463149588">🤝</tg-emoji></b>\n\n<blockquote><i><tg-emoji emoji-id="5456140674028019486">⚡️</tg-emoji> 您可信赖的 P2P 担保服务：</i>\n\t<tg-emoji emoji-id="5794182096603847292">1⃣</tg-emoji> <tg-emoji emoji-id="5967389567781703494">💼</tg-emoji> NFT 和礼物的自动交易\n\t<tg-emoji emoji-id="5794303034292968945">2⃣</tg-emoji> <tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> 全面保护买卖双方\n\t<tg-emoji emoji-id="5794031944547178894">3⃣</tg-emoji> <tg-emoji emoji-id="6039802097916974085">🪙</tg-emoji> 强大的机器人与网站功能\n\t<tg-emoji emoji-id="5793901252987330401">4⃣</tg-emoji> <tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> 商品通过经理交接：{MANAGER_USERNAME}</blockquote>\n    \n<tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji> 请选择下方操作 <tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji>',
        'verified_status': '\n<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>状态：</b> 已认证用户',
        'btn_create_deal': '创建交易',
        'btn_my_profile': '我的资料',
        'btn_balance_req': '余额与收款方式',
        'btn_verification': '认证',
        'btn_verification_done': '认证',
        'btn_referrals': '推荐计划',
        'btn_change_lang': '🌐 更改语言',
        'btn_my_tag': '我的标签',
        'btn_worker_panel': '工作人员面板',
        'btn_admin_panel': '管理员面板',
        'btn_admin_commands': '管理员命令',
        'btn_support': '客服支持',
        'btn_verification_request': '提交认证申请',
        'btn_appeals': '申诉中心',
        'appeals_menu_text': """<tg-emoji emoji-id="5956561916573782596">📄</tg-emoji> <b>{bot_name} 支持中心</b>

<tg-emoji emoji-id="5931546553868095844">⚙️</tg-emoji> <b>建议与想法：</b>
• 功能改进建议
• 新功能创意
• 集成请求
• 用户体验反馈

<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>投诉与申诉：</b>
• 用户投诉
• 交易问题
• 技术问题
• 不当行为
• 涉嫌欺诈

<tg-emoji emoji-id="5904258298764334001">📞</tg-emoji> <b>重要信息：</b>
• 所有请求将在24小时内处理
• 保证保密
• 欺诈举报将立即处理
• 最佳建议将被采纳到机器人中

<tg-emoji emoji-id="5811989245761426317">💡</tg-emoji> 请选择您要提交的类别：""",
        'appeal_suggest_text': """<tg-emoji emoji-id="5934504443772756682">✍️</tg-emoji> <b>请写下您的建议：</b>

<tg-emoji emoji-id="5893193062850499428">ℹ️</tg-emoji> 详细描述您的想法，说明它将如何改善机器人以及为用户带来哪些好处。""",
        'appeal_complain_text': """<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> <b>请写下您的投诉：</b>

<tg-emoji emoji-id="5893193062850499428">ℹ️</tg-emoji> 请注明：
• 用户/交易ID
• 问题描述
• 截图（如有）
• 期望的解决方案""",
        'withdraw_menu_text': """<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>提现</b>

请选择要提现的货币：""",
        'withdraw_currency_text': """<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>提现 {currency}</b>

<b>您的余额：</b>
{bal_lines}
请输入要提现的 <b>{currency}</b> 数量：
<i>可用：{cur_balance} {currency}</i>""",
        'verification_request_sent': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>申请已发送！</b>\n\n我们会尽快审核。',
        'btn_appeals_suggest': '提建议',
        'btn_appeals_complain': '投诉',
        'btn_admin_appeals': '投诉与建议',
        'btn_appeals_suggestions': '建议',
        'btn_appeals_complaints': '投诉',
        'btn_appeal_reply': '回复',
        'btn_appeal_close': '关闭',
        'btn_my_mammoths': '我的客户',
        'btn_back_menu': '返回菜单',
        'btn_back': '返回',
        'btn_refresh': '刷新',
        'btn_my_deals': '我的交易',
        'btn_cancel': '取消',
        'btn_send_receipt': '发送凭证',
        'btn_confirm_withdraw': '确认提取',
        'btn_withdraw_item': '提取商品',
        'btn_all_deals': '所有交易',
        'btn_to_admin': '进入管理面板',
        'btn_new_deal': '新建交易',
        'bind_requisites': '<tg-emoji emoji-id="5332455502917949981">🏦</tg-emoji> <b>绑定收款方式：</b>\n<tg-emoji emoji-id="5447644880824181073">⚠️</tg-emoji> <b>创建交易前必须绑定至少一种收款方式！\n请设置用于收款的方式：</b>\n<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> Ton — 用于接收 TON\n<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> 银行卡 — 用于接收卢布及其他货币\n<tg-emoji emoji-id="5343777479091831702">👛</tg-emoji> Usdt — 用于接收稳定币\n<tg-emoji emoji-id="5330319637156479518">📱</tg-emoji> 电话号码 — 用于 Qiwi/юmoney\n<tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji> <b>请选择收款方式类型</b> <tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji>',
        'no_requisites_alert': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 创建交易前必须绑定至少一种收款方式！',
        'blocked_alert': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> 您已被封禁，无法创建交易',
        'create_deal_title': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> <b>创建新交易</b>',
        'create_deal_text': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> 创建新交易：\n重要提示：仅在选择"买家"角色时适用\n选择支付货币：',
        'create_deal_text_seller': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> 创建新交易：\n选择收款货币：',
        'profit_new': '<tg-emoji emoji-id="6039802097916974085">🪙</tg-emoji> <b>新的收益！</b>',
        'profit_type': '<tg-emoji emoji-id="5197371802136892976">⛏</tg-emoji> <b>类型：</b>',
        'profit_amount': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> <b>金额：</b>',
        'profit_desc': '<tg-emoji emoji-id="5197269100878907942">✍️</tg-emoji> <b>描述：</b>',
        'profit_deal': '<tg-emoji emoji-id="5195033767969839232">🚀</tg-emoji> <b>交易：</b>',
        'profit_success': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>交易成功完成！</b>',
        'profit_direct_transfer': '直接转账',
        'lang_select': '🌐 选择语言 / Select language / 选择语言 / اختر اللغة:',
        'lang_ru': '<tg-emoji emoji-id="5449408995691341691">🇷🇺</tg-emoji> Русский',
        'lang_en': '🇬🇧 English',
        'lang_zh': '🇨🇳 中文',
        'lang_ar': '🇸🇦 عربي',
        'already_verified': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> 您已通过认证！',
        'access_denied': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 访问被拒绝',
        'deal_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 未找到该交易',
        'deal_already_paid': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 该交易已支付或已完成',
        'deal_not_paid': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 该交易尚未付款',
        'deal_no_buyer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 该交易没有买家',
        'not_buyer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 您不是该交易的买家',
        'not_seller': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 您不是该交易的卖家',
        'insufficient_funds': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 余额不足',
        'tag_workers_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 仅工作人员和管理员可以设置标签',
        'no_tag_set': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 您尚未设置标签',
        'workers_admins_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 仅工作人员和管理员可用',
        'choose_payment_first': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 请先选择认证付款方式',
        'payment_confirmed': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> 付款已确认，收益已发送',
        'user_not_found': '未找到该用户',
        'verification_receipt_title': '📤 <b>提交认证凭证</b>',
        'verification_receipt_text': '📤 <b>提交认证凭证</b>\n\n<b>请发送转账凭证的照片或文件。</b>\n\n<b>凭证要求：</b>\n• 图像清晰\n• 可见转账金额\n• 可见转账日期\n• 可见收款方信息\n\n<b>提交凭证后，管理员将进行审核并确认认证。</b>\n<i>通常审核时间不超过 15 分钟。</i>',
        'tag_manage_title': '🏷️ <b>标签管理</b>',
        'tag_current': '<b>当前标签：</b>',
        'tag_not_set': '未设置',
        'tag_used_in_profits': '<b>标签将代替您的名称显示在收益记录中。</b>',
        'tag_example': '<i>示例：收益记录中将显示 "{tag}" 而非自动生成的名称</i>',
        'tag_auto_hint': '<i>如未设置标签，将自动生成一个名称（如 воркер2035、воркер2914 等）</i>',
        'tag_choose_action': '<b>请选择操作：</b>',
        'tag_setup_title': '🏷️ <b>设置标签</b>',
        'tag_setup_text': '🏷️ <b>设置标签</b>\n\n<b>请输入您的标签：</b>\n• 标签必须以 # 符号开头\n• 可使用字母、数字和下划线\n• 标签长度：2 至 20 个字符\n• 示例：#best_worker、#top_admin、#lolz_pro\n\n<b>标签将显示在收益记录中。</b>\n<b>如未设置标签，将自动生成一个名称。</b>\n\n<b>请输入标签：</b>',
        'tag_removed': '🗑️ <b>标签已删除</b>',
        'tag_removed_text': '🗑️ <b>标签已删除</b>\n\n<b>已删除的标签：</b> {tag}\n<b>现在收益记录中将使用自动生成的名称。</b>\n<i>您可以随时设置新的标签。</i>',
        'btn_set_tag': '设置标签',
        'btn_remove_tag': '删除标签',
        'btn_set_new_tag': '设置新标签',
        'items_title': '<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>我的商品</b>',
        'items_empty': '<b>您目前还没有商品。</b>',
        'items_hint': '<i>当您作为买家成功完成交易后，商品会显示在这里。</i>',
        'items_how_to': '<b>如何领取商品：</b>',
        'no_items_withdraw': '📭 <b>没有待提取的商品</b>\n\n您目前没有未提取的商品。',
        'withdraw_title': '📤 <b>确认提取商品</b>',
        'withdraw_text': '📤 <b>确认提取商品</b>\n\n<b>商品 ID：</b> <code>{item_id}</code>\n<b>如需提取商品，请联系客服：</b>\n👉 {MANAGER_USERNAME}\n\n<b>联系后请说明商品编号并按照客服指示操作。</b>\n<i>已认证用户享有优先服务和 0% 手续费。</i>\n\n<b>请确认提取商品：</b>',
        'category_title': '<tg-emoji emoji-id="5433653135799228968">📁</tg-emoji> <b>请选择商品类别</b>\n\n<b>可选类别：</b>\n• <tg-emoji emoji-id="6037175527846975726">🎁</tg-emoji> 礼物 — 数字礼物、贴纸\n• 🏷️ NFT 标签 — NFT 标记、合集\n• <tg-emoji emoji-id="5771695636411847302">📢</tg-emoji> 频道/群组 — Telegram 频道、群组\n• <tg-emoji emoji-id="6028338546736107668">⭐</tg-emoji> Stars — Telegram Stars\n• <tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> 其他 — 任何其他商品\n\n<b>请选择类别：</b>',
        'payment_confirmed_buyer': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>付款已确认</b>\n\n<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>交易：</b> #{deal_id}\n<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>已从余额扣除：</b> {amount} {currency}\n<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>余额结余：</b> {balance} {currency}\n\n<b>请等待卖家发送商品。</b>\n<i>通常不超过 15 分钟。</i>\n\n<b>重要：</b>商品只能通过客服交接！\n卖家会将商品发送给 {MANAGER_USERNAME}，审核后您会收到通知。',
        'payment_received_seller': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>已收到付款！</b>\n\n<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>交易：</b> #{deal_id}\n<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>买家：</b> @{buyer}\n<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>买家认证状态：</b> {verified}\n<tg-emoji emoji-id="5811989245761426317">💸</tg-emoji> <b>金额：</b> {amount} {currency}\n\n<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>资金已存入您的余额。</b>\n买家已通过余额完成支付。请将商品发送给客服！\n\n<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji>️ <b>重要规则：</b>\n商品只能交接给客服 - {MANAGER_USERNAME}！\n\n<b>将商品发送给客服后，请点击下方按钮：</b>',
        'btn_sent_item': '我已发送商品',
        'deal_created': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>交易已创建！</b>\n\n<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>交易 ID：</b> #{deal_id}\n<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>金额：</b> {amount} {currency}\n<tg-emoji emoji-id="5433653135799228968">📁</tg-emoji> <b>类别：</b> {category}\n<b>链接/描述：</b> {description}\n<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>卖家：</b> @{seller}\n<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>卖家认证状态：</b> {verified}\n\n<b>买家专属链接：</b>\n{link}\n\n<b>请将此链接发送给买家：</b>\n{link}\n\n<i>买家点击链接后，交易即可开始。</i>',
        'withdrawal_error': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>提取商品时出错</b>\n\n处理您的提取请求时发生错误。请联系客服：{MANAGER_USERNAME}',
        'balance_withdrawal_error': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>提取资金时出错</b>\n\n处理您的提取请求时发生错误。请联系客服：{MANAGER_USERNAME}',
        'deal_completed_buyer': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>交易成功完成！</b>\n\n<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>交易 ID：</b> #{deal_id}\n<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>金额：</b> {amount} {currency}\n<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>卖家：</b> @{seller}\n<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>商品：</b> {description}\n\n<b>提示：</b>\n• 商品已添加到"我的商品"\n• 您可以随时提取该商品\n• 如需提取，请前往个人资料并点击"我的商品"\n\n💙 感谢您使用 {BOT_NAME} Relayer！',
        'deal_completed_seller': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>交易成功完成！</b>\n\n<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>交易 ID：</b> #{deal_id}\n<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>金额：</b> {amount} {currency}\n<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>买家：</b> @{buyer}\n<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>商品：</b> {description}\n\n<b>提示：</b>\n• 商品已交付给买家\n• 交易已成功完成\n\n💙 感谢您使用 {BOT_NAME} Relayer！',
        'profile_title': '<b>🏆 {BOT_NAME} Relayer 个人资料</b>',
        'deals_empty': '📭 <b>您目前没有进行中的交易</b>\n\n点击下方按钮创建您的第一笔交易！',
        'deals_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>您的进行中交易</b>',
        'deals_select': '请选择要管理的交易：',
        'role_user': '<tg-emoji emoji-id="5886412370347036129">👤</tg-emoji> 用户',
        'role_owner': '<tg-emoji emoji-id="5807868868886009920">👑</tg-emoji> 系统所有者',
        'role_admin': '⚙️ 管理员',
        'role_worker': '👷 工作人员',
        'role_blocked': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji>（已封禁）',
        'verified_yes': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> 已认证',
        'verified_no': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 未认证',
        'enter_amount': '<tg-emoji emoji-id="5811989245761426317">💰</tg-emoji> <b>请输入交易金额：</b>',
        'invalid_amount': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>金额格式错误</b>\n\n请输入数字，例如：1500 或 5.75',
        'amount_zero': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>金额必须大于零</b>',
        'description_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>链接/描述过短</b>\n\n至少需要 5 个字符',
        'direction_sell': '向客户出售商品',
        'direction_buy': '从客户购买商品',
        'direction_ad': '机器人广告',
        'direction_deposit': '客户充值余额',
        'balance_deposit': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>余额充值成功！</b>',
        'deposit_confirmed': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>余额充值成功！</b>\n\n<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> <b>金额：</b> {amount} {currency}\n<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>当前余额：</b> {balance} {currency}\n\n<b>提示：</b>\n• 资金已存入您的余额\n• 您可以用它购买商品\n• 如需提取资金，请联系客服\n\n💙 感谢您使用 {BOT_NAME} Relayer！',
        'verification_info': '<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> {BOT_NAME} 认证\n\n<tg-emoji emoji-id="5447644880824181073">🎯</tg-emoji> <b>高级状态带来的好处：</b>\n• <tg-emoji emoji-id="5902016123972358349">🔐</tg-emoji> 卖家认证 — 信任标志\n• <tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> 交易担保 — 防诈骗保护\n• <tg-emoji emoji-id="5773677501825945508">⚡️</tg-emoji> 优先支持 — 快速响应\n• <tg-emoji emoji-id="5895444149699612825">📈</tg-emoji> 手续费降低 — 0.5%（原1%）\n• <tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> 快速提款 — 1小时内\n• <tg-emoji emoji-id="5413879192267595313">🎁</tg-emoji> 推荐奖励 — 余额+10%\n\n<tg-emoji emoji-id="5902016123972358349">🔒</tg-emoji> <b>安全保障：</b>\n• 全数据加密\n• 交易保险\n• 法律保护\n• 24/7 监控\n\n<tg-emoji emoji-id="5895444149699612825">📈</tg-emoji> <b>优势：</b>\n• 提升买家信任度\n• 更多成功交易\n• 专属客服经理\n• 独家优惠\n\n<tg-emoji emoji-id="5936017305585586269">🔰</tg-emoji> 如需了解更多，请联系客服',
        'verification_info_verified': '<tg-emoji emoji-id="5902016123972358349">🔒</tg-emoji> 认证\n\n<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> 您的账户已认证。\n该状态由 {BOT_NAME} 安全团队审核后授予。',
        'stats_title': '<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>{BOT_NAME} Relayer 统计数据</b>',
        'stats_advantages': '⭐ <b>我们的平台正在快速发展！</b>\n<i>加入不断壮大的社区</i>\n\n💙 <b>{BOT_NAME} Relayer 的优势：</b>\n• 🔒 交易担保\n• <tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> 快速结算\n• <tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> 优惠汇率\n• 📞 7x24 客服支持\n• <tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> 认证体系\n\n🤍 <b>我们与您一起成长！</b>',
        'requisites_card': '<tg-emoji emoji-id="5967548335542767952">💳</tg-emoji> 银行卡',
        'requisites_ton': '⚡ Ton',
        'requisites_phone': '📱 电话号码',
        'requisites_usdt': '<tg-emoji emoji-id="5963312935148195483">💎</tg-emoji> Usdt',
        'not_specified': '未设置',
        'not_specified_f': '未设置',
        'btn_my_stats': '我的统计',
        'btn_my_deals_worker': '我的交易',
        'btn_fake_deals': '刷交易数',
        'btn_fake_balance': '刷余额',
        'btn_remove_deals': '撤销交易数',
        'btn_trim_profile': '精简资料',
        'btn_change_rating': '更改评分',
        'items_total': '商品总数：',
        'items_pending': '待提取：',
        'items_withdrawn': '已提取：',
        'items_pending_title': '待提取商品：',
        'items_withdrawn_title': '已提取商品：',
        'items_item': '商品',
        'items_desc': '描述',
        'items_received': '已收到',
        'items_withdrawn_at': '已提取',
        'items_unknown': '未知',
        'items_how_to_steps': '1. 找到卖家并创建交易\n2. 使用余额支付交易\n3. 卖家确认后，商品会显示在这里\n4. 您可以随时提取商品',
        'withdraw_menu_title': '提取商品',
        'withdraw_items_waiting': '个商品待提取',
        'withdraw_select': '请选择要提取的商品或输入其 ID：',
        'balance_withdraw_title': '提取资金',
        'balance_your': '您的余额：',
        'balance_enter_amount': '请输入要提取的金额和货币：',
        'balance_min': '最低提取金额：',
        'balance_contact_support': '提交申请后请联系客服',
        'btn_to_profile': '返回资料',
        'btn_pay_card': '使用俄罗斯银行卡付款',
        'btn_pay_usdt': '使用 USDT 付款',
        'btn_pay_kzt': '使用 KZT 付款',
        'btn_pay_byn': '使用 BYN 付款',
        'btn_pay_stars': '使用 Stars 付款',
        'cat_gift': '🎁 礼物',
        'cat_nft': '🏷️ NFT 标签',
        'cat_channel': '<tg-emoji emoji-id="5771695636411847302">📢</tg-emoji> 频道/群组',
        'cat_stars': '<tg-emoji emoji-id="6028338546736107668">⭐</tg-emoji> Stars',
        'cat_other': '📦 其他',
        'desc_gift_title': '📝 <b>礼物链接</b>',
        'desc_gift_text': """📝 <b>礼物链接</b>

<b>类别：</b> {category}

<b>粘贴礼物链接：</b>
• 直接发送链接即可
• 示例：https://t.me/nft/EasterEgg-158557
• 请确认礼物可用

<b>重要：</b>请确保链接正确，并指向您要出售的确切商品！

<b>请输入链接：</b>""",
        'desc_stars_text': """📝 <b>商品描述</b>

<b>类别：</b> {category}

<b>请详细描述您要出售的商品：</b>
• Stars 数量
• 平台（iOS/Android/Web）
• 附加条件
• 交付方式

<b>示例：</b>
"1000 个 Telegram Stars，适用于 iOS，通过机器人交付"

<b>请尽可能详细和如实描述！</b>

<b>请输入描述：</b>""",
        'desc_other_text': """📝 <b>商品描述</b>

<b>类别：</b> {category}

<b>请详细描述您要出售的商品：</b>
• 商品名称
• 数量
• 交付条件
• 附加信息
• 商品状态

<b>请尽可能详细和如实描述！</b>

<b>请输入描述：</b>""",
        'desc_default_text': """📝 <b>商品描述</b>

<b>类别：</b> {category}

<b>请详细描述您要出售的商品：</b>
• NFT 标签：标签名称、网络、稀有度
• 频道/群组：链接、订阅人数、主题
• 交付条件

<b>请尽可能详细和如实描述！</b>

<b>请输入描述：</b>""",
        'profile_name': '姓名：',
        'profile_rating': '评分：',
        'rating_no_deals': '暂无交易',
        'profile_success_deals': '成功交易数：',
        'profile_disputes_won': '纠纷获胜数：',
        'profile_active_deals': '进行中交易数：',
        'profile_balance': '余额：',
        'deals_role_seller': '🛒 卖家',
        'deals_role_buyer': '<tg-emoji emoji-id="5811989245761426317">💰</tg-emoji> 买家',
        'deals_buyer_label': '买家：',
        'deals_seller_label': '卖家：',
        'deals_awaiting': '等待中',
        'deals_more': '还有 {count} 笔交易……',
        'deals_deal': '交易',
        'deal_view_seller_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>您的交易</b>',
        'deal_view_buyer_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>您的交易</b>',
        'deal_view_id': '<b>ID：</b>',
        'deal_view_status': '<b>状态：</b>',
        'deal_view_category': '<b>类别：</b>',
        'deal_view_desc': '<b>商品/链接：</b>',
        'deal_view_amount': '<b>金额：</b>',
        'deal_view_payment_method': '<b>付款方式：</b>',
        'deal_view_your_verification': '<b>您的认证状态：</b>',
        'deal_view_buyer_link': '<b>买家专属链接：</b>',
        'deal_view_buyer': '<b>买家：</b>',
        'deal_view_send_link': '<b>请将此链接发送给买家：</b>',
        'deal_view_seller': '<b>卖家：</b>',
        'deal_view_seller_rating': '<b>卖家评分：</b>',
        'deal_view_seller_verification': '<b>卖家认证状态：</b>',
        'deal_view_pay_from_balance': '<b>将从您的余额中扣款支付。</b>',
        'deal_status_awaiting_buyer': '等待买家',
        'deal_status_awaiting_payment': '等待付款',
        'deal_status_paid': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> 已支付',
        'deal_buyer_awaiting': '等待中',
        'deal_category_default': '商品',
        'deal_verified_yes': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> 是',
        'deal_verified_no': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 否',
        'buyer_joined_seller': '<b><tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> 买家 @{buyer} 已加入交易 #{deal_id}！</b>\n\n<blockquote><tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> 收到款项后，您会收到通知，将商品交给经理</blockquote>\n\n<blockquote>📈 该卖家已完成交易数：{success_deals}</blockquote>\n\n<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> 商品交接只能通过经理 {manager} 进行。请不要直接将商品转给卖家！\n\n❗️ 请留意机器人中关于收款的通知！',
        'buyer_joined_buyer': '<b><tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> 卖家 @{seller} 已加入交易 #{deal_id}！</b>\n\n<blockquote><tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> 付款经理信息：{manager}</blockquote>\n\n<blockquote>📈 该卖家已完成交易数：{success_deals}</blockquote>\n\n<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> 所有付款只能通过经理 {manager} 进行。请不要直接将资金转给卖家！\n\n❗️ 付款前请仔细核对收款信息！\n\n<b>商品/链接：</b> {description}\n\n<tg-emoji emoji-id="5811989245761426317">💸</tg-emoji> <b>金额：</b> {amount} {currency}',
        'balance_req_title': '<b><tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> 余额与收款方式</b>',
        'balance_your_title': '<b>您的余额：</b>',
        'requisites_your_title': '<b>您的收款方式：</b>',
        'requisites_crypto_label': '加密钱包',
        'requisites_card_label': '银行卡',
        'requisites_phone_label': '电话号码',
        'balance_choose_action': '<b>请选择操作：</b>',
        'not_specified_req': '未设置',
        'btn_deposit_balance': '充值余额',
        'btn_withdraw_balance': '提取',
        'btn_ton_wallet': 'Ton 钱包',
        'btn_card_req': '银行卡',
        'btn_phone_req': '电话号码',
        'btn_usdt_wallet': 'Usdt 钱包',
        'referral_title': '<b><tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> 推荐系统</b>',
        'referral_percent': '您的推荐返佣比例',
        'referral_invited': '已邀请用户数',
        'referral_balance_ton': '推荐余额 TON',
        'referral_balance_usdt': '推荐余额 USDT TON',
        'referral_link_label': '<b>您的邀请链接：\n\n{ref_link}</b>',
        'btn_copy_link': '复制',
        'btn_pay_balance': '使用余额付款',
        'btn_open_dispute': '提起纠纷',
        'btn_my_deals_nav': '我的交易',
        'btn_deal_link': '交易',
        'deposit_select_currency_text': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> 余额充值\n\n请选择充值货币：',
        'deposit_currency_title_prefix': '充值余额',
        'deposit_currency_support_hint': '请联系客服获取充值收款信息。\n<tg-emoji emoji-id="5447644880824181073">❗️</tg-emoji> 充值后资金将记入您的余额。',
        'deposit_title': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>余额充值</b>',
        'deposit_choose': '<b>请选择充值方式：</b>',
        'deposit_card_ru': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> 俄罗斯银行卡 — 卢布充值',
        'deposit_card_ua': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> 乌克兰银行卡 — 格里夫纳充值',
        'deposit_crypto': '₿ 加密货币 — BTC、ETH、USDT、TON、BNB、SOL',
        'deposit_stars': '⭐ Telegram Stars — 使用 Stars 充值',
        'deposit_after': '<b>选择方式后，系统会显示转账收款信息。</b>',
        'deposit_important': '<b>重要：</b>转账后请务必点击"📤 发送凭证"按钮！',
        'deposit_verified_hint': '<i>已认证用户的申请将获得优先处理</i>',
        'deposit_amount_title': '<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>请输入充值金额</b>',
        'deposit_method_label': '<b>方式：</b>',
        'deposit_currency_label': '<b>货币：</b>',
        'deposit_min': '• 最低金额：',
        'deposit_unlimited': '无限制',
        'deposit_after_amount': '<b>输入金额后即可发送凭证。</b>',
        'deposit_instructions': '<b>操作说明：</b>',
        'deposit_instruction_1': '1. 按照上方收款信息转账指定金额',
        'deposit_instruction_1_crypto': '1. 将 {name} 转账至上方地址',
        'deposit_instruction_2': '2. 保存转账凭证/截图',
        'deposit_instruction_3': '3. 点击"📤 发送凭证"按钮',
        'deposit_instruction_4': '4. 上传凭证照片或文件',
        'deposit_instruction_5': '5. 管理员审核后资金将充入余额',
        'deposit_important_note': '<b>重要：</b>未发送凭证将不予充值！',
        'deposit_requisites_label': '<b>{name} 收款信息：</b>',
        'deposit_support_contact': '请联系客服获取最新收款信息：{support}',
        'deal_amount_title': '<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> 创建交易\n\n<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> 请输入交易金额：',
        'deal_amount_examples': '<tg-emoji emoji-id="5795328215886894640">📌</tg-emoji> 示例：2000.50',
        'deal_amount_min': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> 请填写准确金额，以避免交易处理错误。',
        'deal_amount_min_stars': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> 请输入Stars数量。',
        'deal_amount_enter': '',
        'deal_amount_too_small': '<tg-emoji emoji-id="5922712343011135025">❌</tg-emoji> <b>金额过小</b>\n\n最低金额：{min_amount} {currency}',
        'deal_created_title': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>交易已创建！</b>',
        'deal_gifts_count': '<b>礼物数量：</b>',
        'deal_send_link_buyer': '<b>请将此链接发送给买家：</b>',
        'deal_started_when': '<i>买家点击链接后，交易即可开始。</i>',
        'deal_seller_label': '<tg-emoji emoji-id="6041705726206808304">👤</tg-emoji> <b>卖家：</b>',
        'deal_seller_verif': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>卖家认证：</b>',
        'card_ru_name': '俄罗斯银行卡',
        'card_ua_name': '乌克兰银行卡',
        'not_specified_val': '未设置',
        'deposit_reason_none': '未说明（请联系用户确认）',
        'requisites_card_btn': '银行卡',
        'requisites_phone_btn': '电话号码',
        'deal_info_title': '<b>📋 交易信息</b>',
        'deal_status_label': '<b>状态：</b>',
        'deal_status_created': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> 等待付款',
        'deal_status_completed': '<tg-emoji emoji-id="5893193062850499428">📱</tg-emoji> 已完成',
        'deal_status_disputed': '<tg-emoji emoji-id="5922712343011135025">❌</tg-emoji> 纠纷中',
        'deal_send_link': '<b>请将此链接发送给买家：</b>',
        'deal_buyer_prompt': '<b>请点击下方按钮付款</b>',
        'seller_sent_item': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>商品已发送！</b>',
        'seller_sent_wait': '<b>请等待客服确认。</b>',
        'verification_pay_title': '🔰 <b>认证付款（{method}）</b>',
        'verification_pay_cost': '<b>认证费用：</b> {price} {currency}',
        'verification_pay_after': '<b>转账后请点击"📤 发送凭证"按钮并附上付款凭证。</b>',
        'verif_receipt_text': '📤 <b>提交认证凭证</b>\n\n请发送付款确认的照片或文件。\n\n<b>凭证要求：</b>\n• 图像清晰\n• 金额可见\n• 日期可见\n• 收款方信息可见\n\n<b>提交后，管理员将审核并确认您的认证。</b>\n<i>审核通常最多需要15分钟。</i>',
        'verif_pay_card_msg': '🔰 <b>认证付款（俄罗斯银行卡）</b>\n\n<b>认证费用：</b> {price} RUB\n{details}\n\n<b>转账后请点击"📤 发送凭证"按钮并附上付款凭证。</b>',
        'verif_pay_usdt_msg': '🔰 <b>认证付款（USDT TRC20）</b>\n\n<b>认证费用：</b> {price} USDT\n{details}\n\n<b>转账后请点击"📤 发送凭证"按钮并附上付款凭证。</b>',
        'verif_pay_simple_msg': '🔰 <b>认证付款（{method}）</b>\n\n<b>认证费用：</b> {price} {currency}\n请联系客服确认收款信息。\n\n<b>操作说明：</b>\n1. 联系 {MANAGER_USERNAME} 进行付款。\n2. 管理员审核后，资金将存入您的余额。',
        'verif_pay_stars_msg': '🔰 <b>认证付款（Stars）</b>\n\n<b>认证费用：</b> {price} Stars\n请使用 Stars 向客服账号付款\n网络：Stars\n\n<b>操作说明：</b>\n1. 将 Stars 转给客服账号（{MANAGER_USERNAME}）\n2. 管理员审核后，资金将存入您的余额',
        'error_own_deal': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 您不能作为买家加入自己创建的交易。',
        'error_deal_taken': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 该交易已被其他买家占用。',
        'wallet_crypto_title': '<tg-emoji emoji-id="5992430854909989581">🪙</tg-emoji> <b>加密钱包</b>',
        'wallet_send_crypto': '<b>请用一条消息发送钱包地址和网络：</b>',
        'wallet_crypto_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>加密钱包已更新</b>',
        'wallet_new_crypto': '<b>新信息：</b>',
        'wallet_crypto_hint': """• 一条消息：钱包地址和网络
• 例如：UQAbc123...xyz，网络 Ton
• 例如：TXaBc123...xyz，网络 Trc-20
<i>信息将被保存用于接收加密货币付款</i>""",
        'wallet_ton_title': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> <b>TON 钱包</b>',
        'wallet_card_title': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> <b>银行卡</b>',
        'wallet_phone_title': '<tg-emoji emoji-id="5330319637156479518">📱</tg-emoji> <b>电话号码</b>',
        'wallet_usdt_title': '<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> <b>USDT 钱包</b>',
        'wallet_current': '<b>当前地址：</b>',
        'wallet_current_card': '<b>当前收款信息：</b>',
        'wallet_current_phone': '<b>当前号码：</b>',
        'wallet_send_new': '<b>请发送新的钱包地址：</b>',
        'wallet_send_card': '<b>请发送新的收款信息：</b>',
        'wallet_send_phone': '<b>请发送电话号码：</b>',
        'wallet_send_usdt': '<b>请发送 Usdt 地址（TRC20）：</b>',
        'wallet_ton_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>TON 钱包已更新</b>',
        'wallet_card_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>银行卡已更新</b>',
        'wallet_phone_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>电话号码已更新</b>',
        'wallet_usdt_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>USDT 钱包已更新</b>',
        'wallet_new_address': '<b>新地址：</b>',
        'wallet_new_card': '<b>新的收款信息：</b>',
        'wallet_new_phone': '<b>新号码：</b>',
        'wallet_card_note': '<b>现在您可以通过此银行卡接收卢布付款。</b>\n<i>收款信息将自动展示给买家。</i>',
        'wallet_phone_note': '<b>现在您可以通过此号码接收 Qiwi/юmoney 付款。</b>\n<i>请确保号码有效并已绑定钱包。</i>',
        'wallet_usdt_note': '<b>现在您可以通过此钱包接收 Usdt 付款。</b>\n<i>请确认该地址属于 TRC20 网络。</i>',
        'btn_all_requisites': '所有收款方式',
        'wallet_menu_title': """🏦 <b>管理收款方式</b>

<b>设置您的收款方式：</b>
• <tg-emoji emoji-id='5992430854909989581'>🪙</tg-emoji> 加密钱包 — 地址和网络（Ton、Trc-20 等）
• <tg-emoji emoji-id='5445353829304387411'>💳</tg-emoji> 银行卡 — 用于接收卢布及其他货币
• 📱 电话号码 — 国际格式

<b>说明：</b>Stars 不需要收款方式

<b>重要：</b>请只填写经过验证的收款方式！

<b>请选择收款方式类型：</b>""",
        'wallet_ton_hint': """• 格式：UQ... 或 EQA...
• 请务必核对地址正确性
• 地址必须以 UQ 或 EQ 开头
<i>地址将保存用于接收付款</i>""",
        'wallet_card_hint': """• 格式：2200 1234 5678 9010
• 或：银行名称 — 卡号
• 支持俄罗斯、白俄罗斯、哈萨克斯坦、乌克兰银行卡
<i>收款信息将保存用于接收卢布付款</i>""",
        'wallet_phone_hint': """• 格式：+79991234567
• 用于 Qiwi/юmoney
• 请包含国家代码
<i>号码将保存用于接收付款</i>""",
        'wallet_usdt_hint': """• 格式：T...（TRC20 网络）
• 请务必核对地址正确性
• 仅限 TRC20 网络！
<i>地址将保存用于接收 Usdt</i>""",
        'btn_add_worker': '添加工作人员',
        'btn_remove_worker': '移除工作人员',
        'btn_check_deals': '检查交易',
        'btn_demote_worker': '降级工作人员',
        'btn_export_csv': '导出为 CSV',
        'btn_worker_panel_nav': '工作人员面板',
        'btn_admin_panel_nav': '管理员面板',
        'btn_stats': '统计',
        'btn_my_profile_nav': '我的资料',
        'btn_my_items': '我的商品',
        'btn_my_deals_nav2': '我的交易',
        'btn_manage_tag': '标签管理',
        'btn_to_worker_panel': '返回工作人员面板',
        'btn_confirm_deposit': '确认充值',
        'btn_decline': '拒绝',
        'btn_verify_user': '认证',
        'btn_unverify_user': '取消认证',
        'btn_not_paid': '未付款',
        'btn_not_sent': '未发货',
        'btn_wrong_item': '商品不符',
        'btn_other_reason': '其他原因',
        'dispute_title': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>发起纠纷</b>',
        'dispute_deal': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>交易：</b>',
        'dispute_role': "<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>您的角色：</b>",
        'dispute_role_buyer': '买家',
        'dispute_role_seller': '卖家',
        'dispute_support': '👨\u200d💼 <b>交易客服：</b>',
        'dispute_confirm': '<b>您确定要发起纠纷吗？</b>\n<i>管理员将在24小时内处理您的纠纷。</i>',
        'dispute_reason': '<b>请选择原因：</b>',
        'btn_contact_manager': '联系经理',
        'btn_to_deal': '查看交易',
        'btn_contact_support': '客服支持',
        'admin_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 访问被拒绝。仅管理员可执行此操作',
        'admin_complete_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 访问被拒绝。仅管理员可完成交易',
        'admin_confirm_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 访问被拒绝。仅管理员可确认收货',
        'owner_only_admins': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 访问被拒绝。仅系统所有者可查看所有管理员列表',
        'owner_only_add_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 访问被拒绝。仅系统所有者可添加管理员',
        'owner_only_remove_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 访问被拒绝。仅系统所有者可移除管理员',
        'admin_block_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 访问被拒绝。仅管理员可管理封禁',
        'cannot_block_owner': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 无法封禁系统所有者',
        'already_blocked': '⚠️ 该用户已被封禁',
        'owner_unblock_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 仅系统所有者可解封系统所有者',
        'not_blocked': '⚠️ 该用户未被封禁',
        'user_not_worker': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 该用户不是工作人员',
        'method_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 未找到该方法',
        'error_generic': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 出现错误',
        'deposit_approved': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> 充值已确认！',
        'deposit_error': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 确认时出错',
        'deposit_declined': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 充值已被拒绝',
        'deposit_declined_user': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 您的充值申请已被管理员拒绝。请联系客服了解详情。',
        'user_verified_alert': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> 用户已通过认证',
        'user_unverified_alert': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 认证已取消',
        'data_saved': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> 数据已成功保存！',
        'you_are_blocked': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> 您已被封禁',
        'export_in_dev': '📥 导出功能正在开发中',
        'lang_changed': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> 语言已更改！',
        'payment_not_supported': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 不再支持通过确认方式付款。请使用余额付款。',
        'invalid_id_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>ID 格式错误</b>\n\n请输入整数',
        'invalid_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>格式错误</b>',
        'invalid_amount_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>金额格式错误</b>\n\n请输入数字，例如：1000 或 0.01',
        'invalid_currency': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>货币无效</b>',
        'user_not_found_id': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>未找到该用户</b>',
        'cannot_block_owner_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>无法封禁系统所有者</b>',
        'cannot_remove_owner': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>无法移除系统所有者</b>',
        'cannot_add_owner_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>无法将系统所有者添加为管理员</b>',
        'edit_cancelled': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>编辑已取消。</b>',
        'method_not_found_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>错误：未找到该方法。</b>',
        'send_receipt_first': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 请先选择充值方式并输入金额。',
        'send_photo_doc': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 请发送凭证的照片或文件。',
        'deal_deleted': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>未找到该交易</b>\n\n该交易已被删除或不存在。',
        'scam_desc_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>描述过短</b>\n\n请详细描述被骗情况（至少 3 个字符）。',
        'deal_complete_error': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>完成交易出错</b>\n\n无法完成该交易。',
        'amount_negative': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>金额无效</b>\n\n金额必须大于 0',
        'amount_too_small': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>金额过小</b>',
        'insufficient_funds_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>余额不足</b>',
        'tag_must_start_hash': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>标签必须以 # 符号开头</b>\n\n示例：#best_worker',
        'tag_too_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>标签过短</b>\n\n最少 2 个字符（包含 #）',
        'tag_too_long': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>标签过长</b>\n\n最多 20 个字符',
        'tag_already_used': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>该标签已被使用</b>',
        'no_recipients': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>没有收件人</b>\n\n未找到符合所选群发类型的收件人。',
        'verified_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>未找到已认证用户</b>',
        'deals_not_found_search': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>未找到交易</b>',
        'users_not_found_search': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>未找到用户</b>',
        'bot_error': '机器人使用出错。',
        'access_denied_block': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>访问被拒绝</b>\n\n仅管理员可以封禁用户。',
        'access_denied_unblock': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>访问被拒绝</b>\n\n仅管理员可以解封用户。',
        'access_denied_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>访问被拒绝</b>\n您没有管理员权限',
        'deals_negative': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 交易数量不能为负数',
        'enter_integer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 请输入整数',
        'amount_negative_balance': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> 金额不能为负数',
        'btn_deposit_card_ru': '俄罗斯银行卡',
        'btn_deposit_card_ua': '乌克兰银行卡',
        'btn_deposit_crypto': '加密货币',
        'btn_deposit_stars': 'Telegram Stars',
        'btn_payment_ton':   '⚡ Ton',
        'btn_payment_crypto': '🪙 加密钱包',
        'btn_payment_card':  '💳 银行卡',
        'btn_payment_phone': '📱 电话号码',
        'btn_payment_usdt':  '💎 Usdt',
        'btn_role_seller':   '🔥 我是卖家',
        'btn_role_buyer':    '🛒 我是买家',
        'deal_role_title':   '🧾 <b>新交易</b>',
        'deal_role_question':'💬 <i>您在此交易中的角色是什么？</i>',
        'deal_role_seller_desc': '🔥 <b>卖家</b> — 您出售商品/服务并收款。',
        'deal_role_buyer_desc':  '🛒 <b>买家</b> — 您付款并获得商品/服务。',
        'not_specified':  '未设置',
        'not_specified_f':'未设置',
    },
    'ar': {
        'welcome': '<b><tg-emoji emoji-id="5893255507380014983">💼</tg-emoji> مرحبًا بك في {BOT_NAME} Relayer <tg-emoji emoji-id="5357080225463149588">🤝</tg-emoji></b>\n\n<blockquote><i><tg-emoji emoji-id="5456140674028019486">⚡️</tg-emoji> ضامن معاملاتك الموثوق من نوع P2P:</i>\n\t<tg-emoji emoji-id="5794182096603847292">1⃣</tg-emoji> <tg-emoji emoji-id="5967389567781703494">💼</tg-emoji> صفقات تلقائية للهدايا و NFT\n\t<tg-emoji emoji-id="5794303034292968945">2⃣</tg-emoji> <tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> حماية كاملة لكلا الطرفين\n\t<tg-emoji emoji-id="5794031944547178894">3⃣</tg-emoji> <tg-emoji emoji-id="6039802097916974085">🪙</tg-emoji> إمكانيات واسعة للبوت والموقع\n\t<tg-emoji emoji-id="5793901252987330401">4⃣</tg-emoji> <tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> تسليم المنتجات عبر المدير: {MANAGER_USERNAME}</blockquote>\n    \n<tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji> اختر الإجراء أدناه <tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji>',
        'verified_status': '\n<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>الحالة:</b> مستخدم موثّق',
        'btn_create_deal': 'إنشاء صفقة',
        'btn_my_profile': 'ملفي الشخصي',
        'btn_balance_req': 'الرصيد وبيانات الدفع',
        'btn_verification': 'التوثيق',
        'btn_verification_done': 'التوثيق',
        'btn_referrals': 'الإحالات',
        'btn_change_lang': '🌐 تغيير اللغة',
        'btn_my_tag': 'علامتي',
        'btn_worker_panel': 'لوحة الموظف',
        'btn_admin_panel': 'لوحة الإدارة',
        'btn_admin_commands': 'أوامر المشرف',
        'btn_support': 'الدعم الفني',
        'btn_verification_request': 'طلب التوثيق',
        'btn_appeals': 'المراسلات',
        'appeals_menu_text': """<tg-emoji emoji-id="5956561916573782596">📄</tg-emoji> <b>مركز الدعم {bot_name}</b>

<tg-emoji emoji-id="5931546553868095844">⚙️</tg-emoji> <b>قسم الاقتراحات والأفكار:</b>
• اقتراحات لتحسين الوظائف
• أفكار لميزات جديدة
• طلبات التكامل
• ملاحظات حول تجربة المستخدم

<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>قسم الشكاوى والمطالبات:</b>
• شكاوى ضد المستخدمين
• مشاكل في الصفقات
• مشاكل تقنية
• سلوك غير لائق
• اشتباه في الاحتيال

<tg-emoji emoji-id="5904258298764334001">📞</tg-emoji> <b>معلومات مهمة:</b>
• تتم مراجعة جميع الطلبات خلال 24 ساعة
• السرية مضمونة
• استجابة فورية لبلاغات الاحتيال
• أفضل الاقتراحات يتم تطبيقها في البوت

<tg-emoji emoji-id="5811989245761426317">💡</tg-emoji> اختر القسم المناسب لطلبك:""",
        'appeal_suggest_text': """<tg-emoji emoji-id="5934504443772756682">✍️</tg-emoji> <b>اكتب اقتراحك:</b>

<tg-emoji emoji-id="5893193062850499428">ℹ️</tg-emoji> صف فكرتك بالتفصيل - كيف ستحسن البوت وما الفوائد التي تجلبها للمستخدمين.""",
        'appeal_complain_text': """<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> <b>اكتب شكواك:</b>

<tg-emoji emoji-id="5893193062850499428">ℹ️</tg-emoji> يرجى تحديد:
• معرف المستخدم/الصفقة
• وصف المشكلة
• لقطات شاشة (إن وجدت)
• الحل المطلوب""",
        'withdraw_menu_text': """<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>سحب الأموال</b>

اختر العملة للسحب:""",
        'withdraw_currency_text': """<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>سحب {currency}</b>

<b>رصيدك:</b>
{bal_lines}
أدخل المبلغ المراد سحبه بعملة <b>{currency}</b>:
<i>المتاح: {cur_balance} {currency}</i>""",
        'verification_request_sent': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم إرسال الطلب!</b>\n\nسنقوم بمراجعته قريباً.',
        'btn_appeals_suggest': 'اقتراح',
        'btn_appeals_complain': 'شكوى',
        'btn_admin_appeals': 'الشكاوى والاقتراحات',
        'btn_appeals_suggestions': 'الاقتراحات',
        'btn_appeals_complaints': 'الشكاوى',
        'btn_appeal_reply': 'رد',
        'btn_appeal_close': 'إغلاق',
        'btn_my_mammoths': 'عملائي',
        'btn_back_menu': 'القائمة الرئيسية',
        'btn_back': 'رجوع',
        'btn_refresh': 'تحديث',
        'btn_my_deals': 'صفقاتي',
        'btn_cancel': 'إلغاء',
        'btn_send_receipt': 'إرسال الإيصال',
        'btn_confirm_withdraw': 'تأكيد السحب',
        'btn_withdraw_item': 'سحب المنتج',
        'btn_all_deals': 'جميع الصفقات',
        'btn_to_admin': 'لوحة الإدارة',
        'btn_new_deal': 'صفقة جديدة',
        'bind_requisites': '<tg-emoji emoji-id="5332455502917949981">🏦</tg-emoji> <b>ربط بيانات الدفع:</b>\n<tg-emoji emoji-id="5447644880824181073">⚠️</tg-emoji> <b>يجب ربط وسيلة دفع واحدة على الأقل لإنشاء صفقة!\nيرجى تحديد وسيلة استلام المدفوعات:</b>\n<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> Ton — لاستلام عملة TON\n<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> بطاقة مصرفية — لاستلام الروبل وعملات أخرى\n<tg-emoji emoji-id="5343777479091831702">👛</tg-emoji> Usdt — لاستلام العملات المستقرة\n<tg-emoji emoji-id="5330319637156479518">📱</tg-emoji> رقم الهاتف — لخدمة Qiwi/юmoney\n<tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji> <b>اختر نوع وسيلة الدفع</b> <tg-emoji emoji-id="5406745015365943482">⬇️</tg-emoji>',
        'no_requisites_alert': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> يجب ربط وسيلة دفع واحدة على الأقل لإنشاء صفقة!',
        'blocked_alert': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> تم حظرك ولا يمكنك إنشاء صفقات',
        'create_deal_title': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> <b>إنشاء صفقة جديدة</b>',
        'create_deal_text': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> إنشاء صفقة جديدة:\nمهم: ينطبق هذا فقط عند اختيار دور "المشتري"\nاختر عملة الدفع:',
        'create_deal_text_seller': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> إنشاء صفقة جديدة:\nاختر عملة استلام الدفع:',
        'profit_new': '<tg-emoji emoji-id="6039802097916974085">🪙</tg-emoji> <b>ربح جديد!</b>',
        'profit_type': '<tg-emoji emoji-id="5197371802136892976">⛏</tg-emoji> <b>النوع:</b>',
        'profit_amount': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> <b>المبلغ:</b>',
        'profit_desc': '<tg-emoji emoji-id="5197269100878907942">✍️</tg-emoji> <b>الوصف:</b>',
        'profit_deal': '<tg-emoji emoji-id="5195033767969839232">🚀</tg-emoji> <b>الصفقة:</b>',
        'profit_success': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تمت الصفقة بنجاح!</b>',
        'profit_direct_transfer': 'تحويل مباشر',
        'lang_select': '🌐 اختر اللغة / Выберите язык / Select language / 选择语言:',
        'lang_ru': '<tg-emoji emoji-id="5449408995691341691">🇷🇺</tg-emoji> Русский',
        'lang_en': '🇬🇧 English',
        'lang_zh': '🇨🇳 中文',
        'lang_ar': '🇸🇦 عربي',
        'already_verified': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> أنت موثّق بالفعل!',
        'access_denied': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم رفض الوصول',
        'deal_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> الصفقة غير موجودة',
        'deal_already_paid': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم دفع هذه الصفقة أو إتمامها بالفعل',
        'deal_not_paid': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> لم يتم دفع هذه الصفقة بعد',
        'deal_no_buyer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> لا يوجد مشترٍ لهذه الصفقة',
        'not_buyer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> أنت لست المشتري في هذه الصفقة',
        'not_seller': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> أنت لست البائع في هذه الصفقة',
        'insufficient_funds': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> الرصيد غير كافٍ',
        'tag_workers_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تعيين العلامة متاح فقط للموظفين والمسؤولين',
        'no_tag_set': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> لم تقم بتعيين علامة',
        'workers_admins_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> متاح فقط للموظفين والمسؤولين',
        'choose_payment_first': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> يرجى اختيار طريقة دفع التوثيق أولاً',
        'payment_confirmed': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> تم تأكيد الدفع، وتم إرسال الربح',
        'user_not_found': 'المستخدم غير موجود',
        'verification_receipt_title': '📤 <b>إرسال إيصال التوثيق</b>',
        'verification_receipt_text': '📤 <b>إرسال إيصال التوثيق</b>\n\n<b>يرجى إرسال صورة أو مستند يثبت التحويل.</b>\n\n<b>متطلبات الإيصال:</b>\n• صورة واضحة\n• يظهر فيها مبلغ التحويل\n• يظهر فيها تاريخ التحويل\n• تظهر فيها بيانات المستلم\n\n<b>بعد إرسال الإيصال، سيقوم المسؤول بمراجعته وتأكيد التوثيق.</b>\n<i>عادةً ما تستغرق المراجعة حتى 15 دقيقة.</i>',
        'tag_manage_title': '🏷️ <b>إدارة العلامة</b>',
        'tag_current': '<b>العلامة الحالية:</b>',
        'tag_not_set': 'غير محددة',
        'tag_used_in_profits': '<b>تُستخدم العلامة في سجل الأرباح بدلاً من اسمك.</b>',
        'tag_example': '<i>مثال: سيظهر "{tag}" في سجل الأرباح بدلاً من الاسم المُولَّد تلقائيًا</i>',
        'tag_auto_hint': '<i>إذا لم تحدد علامة، سيتم توليد اسم تلقائي (مثل воркер2035، воркер2914 وغيرها)</i>',
        'tag_choose_action': '<b>اختر الإجراء:</b>',
        'tag_setup_title': '🏷️ <b>تعيين العلامة</b>',
        'tag_setup_text': '🏷️ <b>تعيين العلامة</b>\n\n<b>أدخل علامتك:</b>\n• يجب أن تبدأ العلامة برمز #\n• يمكن استخدام الحروف والأرقام والشرطة السفلية\n• طول العلامة: من 2 إلى 20 حرفًا\n• مثال: #best_worker، #top_admin، #lolz_pro\n\n<b>ستظهر العلامة في سجل الأرباح.</b>\n<b>إذا لم يتم تعيين علامة، سيتم توليد اسم تلقائي.</b>\n\n<b>أدخل العلامة:</b>',
        'tag_removed': '🗑️ <b>تم حذف العلامة</b>',
        'tag_removed_text': '🗑️ <b>تم حذف العلامة</b>\n\n<b>العلامة المحذوفة:</b> {tag}\n<b>سيتم الآن استخدام اسم مُولَّد تلقائيًا في سجل الأرباح.</b>\n<i>يمكنك تعيين علامة جديدة في أي وقت.</i>',
        'btn_set_tag': 'تعيين علامة',
        'btn_remove_tag': 'حذف العلامة',
        'btn_set_new_tag': 'تعيين علامة جديدة',
        'items_title': '<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>منتجاتي</b>',
        'items_empty': '<b>لا توجد لديك منتجات حتى الآن.</b>',
        'items_hint': '<i>تظهر المنتجات هنا بعد إتمام الصفقات بنجاح عندما تكون المشتري.</i>',
        'items_how_to': '<b>كيفية استلام المنتج:</b>',
        'no_items_withdraw': '📭 <b>لا توجد منتجات للسحب</b>\n\nليس لديك حاليًا منتجات غير مسحوبة.',
        'withdraw_title': '📤 <b>تأكيد سحب المنتج</b>',
        'withdraw_text': '📤 <b>تأكيد سحب المنتج</b>\n\n<b>رقم المنتج:</b> <code>{item_id}</code>\n<b>لسحب المنتج، يرجى التواصل مع الدعم الفني:</b>\n👉 {MANAGER_USERNAME}\n\n<b>بعد التواصل، يرجى ذكر رقم المنتج واتباع تعليمات الدعم.</b>\n<i>يحصل المستخدمون الموثقون على خدمة ذات أولوية وبدون عمولة 0%.</i>\n\n<b>تأكيد سحب المنتج:</b>',
        'category_title': '<tg-emoji emoji-id="5433653135799228968">📁</tg-emoji> <b>اختر فئة المنتج</b>\n\n<b>الفئات المتاحة:</b>\n• <tg-emoji emoji-id="6037175527846975726">🎁</tg-emoji> هدية — هدايا رقمية، ملصقات\n• 🏷️ علامة NFT — رموز NFT، مجموعات\n• <tg-emoji emoji-id="5771695636411847302">📢</tg-emoji> قناة/مجموعة — قنوات ومجموعات تيليجرام\n• <tg-emoji emoji-id="6028338546736107668">⭐</tg-emoji> Stars — نجوم تيليجرام\n• <tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> أخرى — أي منتج آخر\n\n<b>اختر الفئة:</b>',
        'payment_confirmed_buyer': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم تأكيد الدفع</b>\n\n<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>الصفقة:</b> #{deal_id}\n<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>تم الخصم من الرصيد:</b> {amount} {currency}\n<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>الرصيد المتبقي:</b> {balance} {currency}\n\n<b>يرجى انتظار إرسال المنتج من البائع.</b>\n<i>عادةً يستغرق ذلك حتى 15 دقيقة.</i>\n\n<b>هام:</b> سيتم تسليم المنتج فقط عبر الدعم الفني!\nسيرسل البائع المنتج إلى {MANAGER_USERNAME}، وبعد المراجعة ستتلقى إشعارًا.',
        'payment_received_seller': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>تم استلام الدفع!</b>\n\n<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>الصفقة:</b> #{deal_id}\n<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>المشتري:</b> @{buyer}\n<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>توثيق المشتري:</b> {verified}\n<tg-emoji emoji-id="5811989245761426317">💸</tg-emoji> <b>المبلغ:</b> {amount} {currency}\n\n<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>تم إضافة الأموال إلى رصيدك.</b>\nدفع المشتري الصفقة من رصيده. يرجى إرسال المنتج إلى الدعم الفني!\n\n<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji>️ <b>قاعدة بالغة الأهمية:</b>\nيجب تسليم المنتج حصريًا للدعم الفني - {MANAGER_USERNAME}!\n\n<b>بعد إرسال المنتج إلى الدعم الفني، اضغط الزر أدناه:</b>',
        'btn_sent_item': 'لقد أرسلت المنتج',
        'deal_created': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم إنشاء الصفقة!</b>\n\n<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>رقم الصفقة:</b> #{deal_id}\n<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>المبلغ:</b> {amount} {currency}\n<tg-emoji emoji-id="5433653135799228968">📁</tg-emoji> <b>الفئة:</b> {category}\n<b>الرابط/الوصف:</b> {description}\n<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>البائع:</b> @{seller}\n<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>توثيق البائع:</b> {verified}\n\n<b>رابط المشتري:</b>\n{link}\n\n<b>أرسل هذا الرابط إلى المشتري:</b>\n{link}\n\n<i>بمجرد أن ينقر المشتري على الرابط، ستبدأ الصفقة.</i>',
        'withdrawal_error': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>خطأ في سحب المنتج</b>\n\nحدث خطأ أثناء معالجة طلب السحب الخاص بك. يرجى التواصل مع الدعم الفني: {MANAGER_USERNAME}',
        'balance_withdrawal_error': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>خطأ في سحب الأموال</b>\n\nحدث خطأ أثناء معالجة طلب السحب الخاص بك. يرجى التواصل مع الدعم الفني: {MANAGER_USERNAME}',
        'deal_completed_buyer': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تمت الصفقة بنجاح!</b>\n\n<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>رقم الصفقة:</b> #{deal_id}\n<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>المبلغ:</b> {amount} {currency}\n<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>البائع:</b> @{seller}\n<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>المنتج:</b> {description}\n\n<b>معلومات:</b>\n• تمت إضافة المنتج إلى قسم "منتجاتي"\n• يمكنك سحبه في أي وقت\n• للسحب، انتقل إلى ملفك الشخصي واضغط "منتجاتي"\n\n💙 شكرًا لاستخدامك {BOT_NAME} Relayer!',
        'deal_completed_seller': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تمت الصفقة بنجاح!</b>\n\n<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>رقم الصفقة:</b> #{deal_id}\n<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>المبلغ:</b> {amount} {currency}\n<tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> <b>المشتري:</b> @{buyer}\n<tg-emoji emoji-id="5778672437122045013">📦</tg-emoji> <b>المنتج:</b> {description}\n\n<b>معلومات:</b>\n• تم تسليم المنتج إلى المشتري\n• تمت الصفقة بنجاح\n\n💙 شكرًا لاستخدامك {BOT_NAME} Relayer!',
        'profile_title': '<b>🏆 الملف الشخصي - {BOT_NAME} Relayer</b>',
        'deals_empty': '📭 <b>لا توجد لديك صفقات نشطة حاليًا</b>\n\nأنشئ صفقتك الأولى باستخدام الزر أدناه!',
        'deals_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>صفقاتك النشطة</b>',
        'deals_select': 'اختر الصفقة التي تريد إدارتها:',
        'role_user': '<tg-emoji emoji-id="5886412370347036129">👤</tg-emoji> مستخدم',
        'role_owner': '<tg-emoji emoji-id="5807868868886009920">👑</tg-emoji> مالك النظام',
        'role_admin': '⚙️ مسؤول',
        'role_worker': '👷 موظف',
        'role_blocked': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> (محظور)',
        'verified_yes': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> موثّق',
        'verified_no': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> غير موثّق',
        'enter_amount': '<tg-emoji emoji-id="5811989245761426317">💰</tg-emoji> <b>أدخل مبلغ الصفقة:</b>',
        'invalid_amount': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>تنسيق المبلغ غير صحيح</b>\n\nأدخل رقمًا، مثل: 1500 أو 5.75',
        'amount_zero': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>يجب أن يكون المبلغ أكبر من صفر</b>',
        'description_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>الرابط/الوصف قصير جدًا</b>\n\nالحد الأدنى 5 أحرف',
        'direction_sell': 'بيع منتج للعميل',
        'direction_buy': 'شراء منتج من العميل',
        'direction_ad': 'إعلان البوت',
        'direction_deposit': 'إيداع رصيد من العميل',
        'balance_deposit': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>تم شحن الرصيد بنجاح!</b>',
        'deposit_confirmed': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم شحن الرصيد بنجاح!</b>\n\n<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> <b>المبلغ:</b> {amount} {currency}\n<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>الرصيد الحالي:</b> {balance} {currency}\n\n<b>معلومات:</b>\n• تمت إضافة الأموال إلى رصيدك\n• يمكنك استخدامها لشراء المنتجات\n• لسحب الأموال، يرجى التواصل مع الدعم الفني\n\n💙 شكرًا لاستخدامك {BOT_NAME} Relayer!',
        'verification_info': '<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> توثيق {BOT_NAME}\n\n<tg-emoji emoji-id="5447644880824181073">🎯</tg-emoji> <b>ما يمنحك إياه الحساب المميز:</b>\n• <tg-emoji emoji-id="5902016123972358349">🔐</tg-emoji> توثيق البائع — شارة ثقة\n• <tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> ضمان الصفقات — حماية من المحتالين\n• <tg-emoji emoji-id="5773677501825945508">⚡️</tg-emoji> دعم ذو أولوية — ردود سريعة\n• <tg-emoji emoji-id="5895444149699612825">📈</tg-emoji> عمولة مخفضة — 0.5% بدلاً من 1%\n• <tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> صرف سريع — خلال ساعة واحدة\n• <tg-emoji emoji-id="5413879192267595313">🎁</tg-emoji> مكافآت الإحالة — +10% للرصيد\n\n<tg-emoji emoji-id="5902016123972358349">🔒</tg-emoji> <b>الأمان:</b>\n• تشفير جميع البيانات\n• تأمين الصفقات\n• حماية قانونية\n• مراقبة 24/7\n\n<tg-emoji emoji-id="5895444149699612825">📈</tg-emoji> <b>المزايا:</b>\n• ثقة أعلى من المشترين\n• صفقات ناجحة أكثر\n• مدير شخصي\n• عروض حصرية\n\n<tg-emoji emoji-id="5936017305585586269">🔰</tg-emoji> للمزيد من التفاصيل تواصل مع الدعم',
        'verification_info_verified': '<tg-emoji emoji-id="5902016123972358349">🔒</tg-emoji> التوثيق\n\n<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> حسابك موثَّق.\nتم منح الحالة بعد مراجعة من فريق أمان {BOT_NAME}.',
        'stats_title': '<tg-emoji emoji-id="5895444149699612825">📊</tg-emoji> <b>إحصائيات {BOT_NAME} Relayer</b>',
        'stats_advantages': '⭐ <b>منصتنا في تطور مستمر!</b>\n<i>انضم إلى مجتمعنا المتنامي</i>\n\n💙 <b>مزايا {BOT_NAME} Relayer:</b>\n• 🔒 ضمان المعاملات\n• <tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> مدفوعات سريعة\n• <tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> أسعار صرف مميزة\n• 📞 دعم فني على مدار الساعة\n• <tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> نظام توثيق\n\n🤍 <b>نحن ننمو معكم!</b>',
        'requisites_card': '<tg-emoji emoji-id="5967548335542767952">💳</tg-emoji> بطاقة',
        'requisites_ton': '⚡ Ton',
        'requisites_phone': '📱 الهاتف',
        'requisites_usdt': '<tg-emoji emoji-id="5963312935148195483">💎</tg-emoji> Usdt',
        'not_specified': 'غير محدد',
        'not_specified_f': 'غير محددة',
        'btn_my_stats': 'إحصائياتي',
        'btn_my_deals_worker': 'صفقاتي',
        'btn_fake_deals': 'تضخيم الصفقات',
        'btn_fake_balance': 'تضخيم الرصيد',
        'btn_remove_deals': 'تقليص الصفقات',
        'btn_trim_profile': 'تبسيط الملف الشخصي',
        'btn_change_rating': 'تغيير التقييم',
        'items_total': 'إجمالي المنتجات:',
        'items_pending': 'بانتظار السحب:',
        'items_withdrawn': 'تم سحبها:',
        'items_pending_title': 'بانتظار السحب:',
        'items_withdrawn_title': 'المنتجات المسحوبة:',
        'items_item': 'المنتج',
        'items_desc': 'الوصف',
        'items_received': 'تم الاستلام',
        'items_withdrawn_at': 'تم السحب',
        'items_unknown': 'غير معروف',
        'items_how_to_steps': '1. ابحث عن البائع وأنشئ صفقة\n2. ادفع الصفقة من رصيدك\n3. بعد تأكيد البائع، سيظهر المنتج هنا\n4. يمكنك سحب المنتج في أي وقت',
        'withdraw_menu_title': 'سحب المنتج',
        'withdraw_items_waiting': 'منتجات بانتظار السحب',
        'withdraw_select': 'اختر المنتج المراد سحبه أو أدخل رقمه:',
        'balance_withdraw_title': 'سحب الأموال',
        'balance_your': 'رصيدك:',
        'balance_enter_amount': 'أدخل المبلغ والعملة المراد سحبها:',
        'balance_min': 'الحد الأدنى للسحب:',
        'balance_contact_support': 'بعد تقديم الطلب، تواصل مع الدعم الفني',
        'btn_to_profile': 'الملف الشخصي',
        'btn_pay_card': 'الدفع ببطاقة روسية',
        'btn_pay_usdt': 'الدفع بـ USDT',
        'btn_pay_kzt': 'الدفع بـ KZT',
        'btn_pay_byn': 'الدفع بـ BYN',
        'btn_pay_stars': 'الدفع بـ Stars',
        'cat_gift': '🎁 هدية',
        'cat_nft': '🏷️ علامة NFT',
        'cat_channel': '<tg-emoji emoji-id="5771695636411847302">📢</tg-emoji> قناة/مجموعة',
        'cat_stars': '<tg-emoji emoji-id="6028338546736107668">⭐</tg-emoji> Stars',
        'cat_other': '📦 أخرى',
        'desc_gift_title': '📝 <b>رابط الهدية</b>',
        'desc_gift_text': """📝 <b>رابط الهدية</b>

<b>الفئة:</b> {category}

<b>الصق رابط الهدية:</b>
• فقط أرسل الرابط
• مثال: https://t.me/nft/EasterEgg-158557
• تأكد من توفر الهدية

<b>هام:</b> تأكد من صحة الرابط وأنه يؤدي بالضبط إلى المنتج الذي تبيعه!

<b>أدخل الرابط:</b>""",
        'desc_stars_text': """📝 <b>وصف المنتج</b>

<b>الفئة:</b> {category}

<b>صف بالتفصيل ما تبيعه:</b>
• عدد النجوم Stars
• المنصة (iOS/Android/Web)
• شروط إضافية
• طريقة التسليم

<b>مثال:</b>
"1000 نجمة تيليجرام لنظام iOS، يتم التسليم عبر البوت"

<b>كن دقيقًا وصادقًا قدر الإمكان!</b>

<b>أدخل الوصف:</b>""",
        'desc_other_text': """📝 <b>وصف المنتج</b>

<b>الفئة:</b> {category}

<b>صف بالتفصيل ما تبيعه:</b>
• اسم المنتج
• الكمية
• شروط التسليم
• معلومات إضافية
• حالة المنتج

<b>كن دقيقًا وصادقًا قدر الإمكان!</b>

<b>أدخل الوصف:</b>""",
        'desc_default_text': """📝 <b>وصف المنتج</b>

<b>الفئة:</b> {category}

<b>صف بالتفصيل ما تبيعه:</b>
• لعلامة NFT: اسم العلامة، الشبكة، الندرة
• للقناة/المجموعة: الرابط، عدد المشتركين، الموضوع
• شروط التسليم

<b>كن دقيقًا وصادقًا قدر الإمكان!</b>

<b>أدخل الوصف:</b>""",
        'profile_name': 'الاسم:',
        'profile_rating': 'التقييم:',
        'rating_no_deals': 'لا توجد صفقات',
        'profile_success_deals': 'الصفقات الناجحة:',
        'profile_disputes_won': 'النزاعات المربوحة:',
        'profile_active_deals': 'الصفقات النشطة:',
        'profile_balance': 'الرصيد:',
        'deals_role_seller': '🛒 البائع',
        'deals_role_buyer': '<tg-emoji emoji-id="5811989245761426317">💰</tg-emoji> المشتري',
        'deals_buyer_label': 'المشتري:',
        'deals_seller_label': 'البائع:',
        'deals_awaiting': 'قيد الانتظار',
        'deals_more': 'و {count} صفقات أخرى...',
        'deals_deal': 'صفقة',
        'deal_view_seller_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>صفقتك</b>',
        'deal_view_buyer_title': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>صفقتك</b>',
        'deal_view_id': '<b>الرقم:</b>',
        'deal_view_status': '<b>الحالة:</b>',
        'deal_view_category': '<b>الفئة:</b>',
        'deal_view_desc': '<b>المنتج/الرابط:</b>',
        'deal_view_amount': '<b>المبلغ:</b>',
        'deal_view_payment_method': '<b>طريقة الدفع:</b>',
        'deal_view_your_verification': '<b>حالة توثيقك:</b>',
        'deal_view_buyer_link': '<b>رابط المشتري:</b>',
        'deal_view_buyer': '<b>المشتري:</b>',
        'deal_view_send_link': '<b>أرسل هذا الرابط إلى المشتري:</b>',
        'deal_view_seller': '<b>البائع:</b>',
        'deal_view_seller_rating': '<b>تقييم البائع:</b>',
        'deal_view_seller_verification': '<b>توثيق البائع:</b>',
        'deal_view_pay_from_balance': '<b>سيتم الدفع من رصيدك.</b>',
        'deal_status_awaiting_buyer': 'بانتظار المشتري',
        'deal_status_awaiting_payment': 'بانتظار الدفع',
        'deal_status_paid': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> تم الدفع',
        'deal_buyer_awaiting': 'قيد الانتظار',
        'deal_category_default': 'منتج',
        'deal_verified_yes': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> نعم',
        'deal_verified_no': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> لا',
        'buyer_joined_seller': '<b><tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> انضم المشتري @{buyer} إلى الصفقة #{deal_id}!</b>\n\n<blockquote><tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> بعد استلام الأموال، ستتلقى إشعارًا لتسليم المنتج للمدير</blockquote>\n\n<blockquote>📈 عدد الصفقات المكتملة للبائع: {success_deals}</blockquote>\n\n<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> يتم تسليم المنتج فقط عبر المدير {manager}. لا تقم بتسليم المنتجات مباشرة للبائع!\n\n❗️ تحقق من إشعار استلام الأموال في البوت!',
        'buyer_joined_buyer': '<b><tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> انضم البائع @{seller} إلى الصفقة #{deal_id}!</b>\n\n<blockquote><tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> بيانات الدفع الخاصة بالمدير: {manager}</blockquote>\n\n<blockquote>📈 عدد الصفقات المكتملة للبائع: {success_deals}</blockquote>\n\n<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> تتم جميع المدفوعات فقط عبر المدير {manager}. لا تقم بتحويل الأموال مباشرة للبائع!\n\n❗️ تحقق من بيانات الدفع قبل التحويل!\n\n<b>المنتج/الرابط:</b> {description}\n\n<tg-emoji emoji-id="5811989245761426317">💸</tg-emoji> <b>المبلغ:</b> {amount} {currency}',
        'balance_req_title': '<b><tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> الرصيد وبيانات الدفع</b>',
        'balance_your_title': '<b>رصيدك:</b>',
        'requisites_your_title': '<b>بيانات الدفع الخاصة بك:</b>',
        'requisites_crypto_label': 'محفظة العملات المشفرة',
        'requisites_card_label': 'بطاقة',
        'requisites_phone_label': 'الهاتف',
        'balance_choose_action': '<b>اختر الإجراء:</b>',
        'not_specified_req': 'غير محدد',
        'btn_deposit_balance': 'شحن الرصيد',
        'btn_withdraw_balance': 'سحب',
        'btn_ton_wallet': 'محفظة Ton',
        'btn_card_req': 'بطاقة',
        'btn_phone_req': 'الهاتف',
        'btn_usdt_wallet': 'محفظة Usdt',
        'referral_title': '<b><tg-emoji emoji-id="6032693626394382504">👤</tg-emoji> نظام الإحالة</b>',
        'referral_percent': 'نسبة الإحالة الخاصة بك',
        'referral_invited': 'عدد المستخدمين المدعوين',
        'referral_balance_ton': 'رصيد الإحالة TON',
        'referral_balance_usdt': 'رصيد الإحالة USDT TON',
        'referral_link_label': '<b>رابط الدعوة الخاص بك:\n\n{ref_link}</b>',
        'btn_copy_link': 'نسخ',
        'btn_pay_balance': 'الدفع من الرصيد',
        'btn_open_dispute': 'فتح نزاع',
        'btn_my_deals_nav': 'صفقاتي',
        'btn_deal_link': 'الصفقة',
        'deposit_select_currency_text': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> شحن الرصيد\n\nاختر عملة الإيداع:',
        'deposit_currency_title_prefix': 'شحن الرصيد',
        'deposit_currency_support_hint': 'احصل على تفاصيل الإيداع من الدعم.\n<tg-emoji emoji-id="5447644880824181073">❗️</tg-emoji> تُضاف الأموال إلى رصيدك بعد الشحن.',
        'deposit_title': '<tg-emoji emoji-id="5778421276024509124">💰</tg-emoji> <b>شحن الرصيد</b>',
        'deposit_choose': '<b>اختر طريقة الشحن:</b>',
        'deposit_card_ru': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> بطاقة روسية — شحن بالروبل',
        'deposit_card_ua': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> بطاقة أوكرانية — شحن بالهريفنيا',
        'deposit_crypto': '₿ عملات رقمية — BTC، ETH، USDT، TON، BNB، SOL',
        'deposit_stars': '⭐ نجوم تيليجرام — شحن بالنجوم',
        'deposit_after': '<b>بعد اختيار الطريقة، ستظهر لك بيانات التحويل.</b>',
        'deposit_important': '<b>هام:</b> بعد التحويل، يجب إرسال الإيصال عبر زر "📤 إرسال الإيصال"!',
        'deposit_verified_hint': '<i>يحصل المستخدمون الموثقون على معالجة ذات أولوية للطلبات</i>',
        'deposit_amount_title': '<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> <b>أدخل مبلغ الشحن</b>',
        'deposit_method_label': '<b>الطريقة:</b>',
        'deposit_currency_label': '<b>العملة:</b>',
        'deposit_min': '• الحد الأدنى:',
        'deposit_unlimited': 'غير محدود',
        'deposit_after_amount': '<b>بعد إدخال المبلغ يمكنك إرسال الإيصال.</b>',
        'deposit_instructions': '<b>التعليمات:</b>',
        'deposit_instruction_1': '1. حوّل المبلغ المحدد وفق بيانات الدفع أعلاه',
        'deposit_instruction_1_crypto': '1. حوّل {name} إلى العنوان أعلاه',
        'deposit_instruction_2': '2. احفظ الإيصال/لقطة الشاشة',
        'deposit_instruction_3': '3. اضغط زر "📤 إرسال الإيصال"',
        'deposit_instruction_4': '4. أرفق صورة أو مستند كتأكيد',
        'deposit_instruction_5': '5. بعد مراجعة المسؤول ستُضاف الأموال للرصيد',
        'deposit_important_note': '<b>هام:</b> بدون إرسال الإيصال لن يُحسب الشحن!',
        'deposit_requisites_label': '<b>بيانات الدفع ({name}):</b>',
        'deposit_support_contact': 'تواصل مع الدعم للحصول على بيانات الدفع الحالية: {support}',
        'deal_amount_title': '<tg-emoji emoji-id="5902016123972358349">🛡</tg-emoji> إنشاء الصفقة\n\n<tg-emoji emoji-id="5902056028513505203">💰</tg-emoji> أدخل مبلغ الصفقة:',
        'deal_amount_examples': '<tg-emoji emoji-id="5795328215886894640">📌</tg-emoji> مثال: 2000.50',
        'deal_amount_min': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> أدخل المبلغ الدقيق لتجنب أخطاء المعالجة.',
        'deal_amount_min_stars': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> أدخل عدد النجوم.',
        'deal_amount_enter': '',
        'deal_amount_too_small': '<tg-emoji emoji-id="5922712343011135025">❌</tg-emoji> <b>المبلغ صغير جداً</b>\n\nالحد الأدنى: {min_amount} {currency}',
        'deal_created_title': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم إنشاء الصفقة!</b>',
        'deal_gifts_count': '<b>عدد الهدايا في الصفقة:</b>',
        'deal_send_link_buyer': '<b>أرسل هذا الرابط للمشتري:</b>',
        'deal_started_when': '<i>بمجرد أن يتبع المشتري الرابط، ستبدأ الصفقة.</i>',
        'deal_seller_label': '<tg-emoji emoji-id="6041705726206808304">👤</tg-emoji> <b>البائع:</b>',
        'deal_seller_verif': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>توثيق البائع:</b>',
        'card_ru_name': 'بطاقة روسية',
        'card_ua_name': 'بطاقة أوكرانية',
        'not_specified_val': 'غير محدد',
        'deposit_reason_none': 'غير محدد (تواصل مع المستخدم للتوضيح)',
        'requisites_card_btn': 'بطاقة',
        'requisites_phone_btn': 'هاتف',
        'deal_info_title': '<b>📋 معلومات الصفقة</b>',
        'deal_status_label': '<b>الحالة:</b>',
        'deal_status_created': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> بانتظار الدفع',
        'deal_status_completed': '<tg-emoji emoji-id="5893193062850499428">📱</tg-emoji> مكتملة',
        'deal_status_disputed': '<tg-emoji emoji-id="5922712343011135025">❌</tg-emoji> نزاع',
        'deal_send_link': '<b>أرسل هذا الرابط إلى المشتري:</b>',
        'deal_buyer_prompt': '<b>اضغط الزر أدناه للدفع</b>',
        'seller_sent_item': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم إرسال المنتج!</b>',
        'seller_sent_wait': '<b>يرجى انتظار تأكيد الدعم الفني.</b>',
        'verification_pay_title': '🔰 <b>دفع التوثيق ({method})</b>',
        'verification_pay_cost': '<b>تكلفة التوثيق:</b> {price} {currency}',
        'verification_pay_after': '<b>بعد التحويل، اضغط زر "📤 إرسال الإيصال" وأرفق إثبات الدفع.</b>',
        'verif_receipt_text': '📤 <b>إرسال إيصال التوثيق</b>\n\nأرسل صورة أو مستنداً يؤكد الدفع.\n\n<b>متطلبات الإيصال:</b>\n• صورة واضحة\n• المبلغ مرئي\n• التاريخ مرئي\n• بيانات المستلم مرئية\n\n<b>بعد الإرسال، سيراجع المسؤول الإيصال ويؤكد توثيقك.</b>\n<i>عادةً ما تستغرق المراجعة حتى 15 دقيقة.</i>',
        'verif_pay_card_msg': '🔰 <b>دفع التوثيق (بطاقة روسية)</b>\n\n<b>تكلفة التوثيق:</b> {price} RUB\n{details}\n\n<b>بعد التحويل، اضغط زر "📤 إرسال الإيصال" وأرفق إثبات الدفع.</b>',
        'verif_pay_usdt_msg': '🔰 <b>دفع التوثيق (USDT TRC20)</b>\n\n<b>تكلفة التوثيق:</b> {price} USDT\n{details}\n\n<b>بعد التحويل، اضغط زر "📤 إرسال الإيصال" وأرفق إثبات الدفع.</b>',
        'verif_pay_simple_msg': '🔰 <b>دفع التوثيق ({method})</b>\n\n<b>تكلفة التوثيق:</b> {price} {currency}\nيرجى التواصل مع الدعم الفني لمعرفة بيانات الدفع.\n\n<b>التعليمات:</b>\n1. تواصل مع {MANAGER_USERNAME} للدفع.\n2. بعد مراجعة المسؤول، ستُضاف الأموال إلى رصيدك.',
        'verif_pay_stars_msg': '🔰 <b>دفع التوثيق (Stars)</b>\n\n<b>تكلفة التوثيق:</b> {price} Stars\nقم بتحويل النجوم إلى حساب الدعم الفني\nالشبكة: Stars\n\n<b>التعليمات:</b>\n1. حوّل النجوم إلى حساب الدعم الفني ({MANAGER_USERNAME})\n2. بعد مراجعة المسؤول، ستُضاف الأموال إلى رصيدك',
        'error_own_deal': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> لا يمكنك الانضمام كمشترٍ إلى صفقتك الخاصة.',
        'error_deal_taken': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> هذه الصفقة محجوزة بالفعل من قبل مشترٍ آخر.',
        'wallet_crypto_title': '<tg-emoji emoji-id="5992430854909989581">🪙</tg-emoji> <b>محفظة العملات المشفرة</b>',
        'wallet_send_crypto': '<b>أرسل عنوان المحفظة والشبكة في رسالة واحدة:</b>',
        'wallet_crypto_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم تحديث محفظة العملات المشفرة</b>',
        'wallet_new_crypto': '<b>البيانات الجديدة:</b>',
        'wallet_crypto_hint': """• رسالة واحدة: عنوان المحفظة والشبكة
• مثال: UQAbc123...xyz، شبكة Ton
• مثال: TXaBc123...xyz، شبكة Trc-20
<i>سيتم حفظ البيانات لاستقبال المدفوعات بالعملات المشفرة</i>""",
        'wallet_ton_title': '<tg-emoji emoji-id="5773677501825945508">⚡</tg-emoji> <b>محفظة TON</b>',
        'wallet_card_title': '<tg-emoji emoji-id="5445353829304387411">💳</tg-emoji> <b>البطاقة المصرفية</b>',
        'wallet_phone_title': '<tg-emoji emoji-id="5330319637156479518">📱</tg-emoji> <b>رقم الهاتف</b>',
        'wallet_usdt_title': '<tg-emoji emoji-id="5836907383292436018">💎</tg-emoji> <b>محفظة USDT</b>',
        'wallet_current': '<b>العنوان الحالي:</b>',
        'wallet_current_card': '<b>بيانات الدفع الحالية:</b>',
        'wallet_current_phone': '<b>الرقم الحالي:</b>',
        'wallet_send_new': '<b>أرسل عنوان المحفظة الجديد:</b>',
        'wallet_send_card': '<b>أرسل بيانات الدفع الجديدة:</b>',
        'wallet_send_phone': '<b>أرسل رقم الهاتف:</b>',
        'wallet_send_usdt': '<b>أرسل عنوان Usdt (TRC20):</b>',
        'wallet_ton_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم تحديث محفظة TON</b>',
        'wallet_card_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم تحديث البطاقة المصرفية</b>',
        'wallet_phone_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم تحديث رقم الهاتف</b>',
        'wallet_usdt_updated': '<tg-emoji emoji-id="5774022692642492953">✅</tg-emoji> <b>تم تحديث محفظة USDT</b>',
        'wallet_new_address': '<b>العنوان الجديد:</b>',
        'wallet_new_card': '<b>بيانات الدفع الجديدة:</b>',
        'wallet_new_phone': '<b>الرقم الجديد:</b>',
        'wallet_card_note': '<b>يمكنك الآن استلام مدفوعات بالروبل على هذه البطاقة.</b>\n<i>سيتم عرض بيانات الدفع تلقائيًا للمشترين.</i>',
        'wallet_phone_note': '<b>يمكنك الآن استلام مدفوعات Qiwi/юmoney على هذا الرقم.</b>\n<i>تأكد من أن الرقم نشط ومرتبط بالمحفظة.</i>',
        'wallet_usdt_note': '<b>يمكنك الآن استلام مدفوعات Usdt على هذه المحفظة.</b>\n<i>تحقق من أن العنوان يتبع شبكة TRC20.</i>',
        'btn_all_requisites': 'جميع بيانات الدفع',
        'wallet_menu_title': """🏦 <b>إدارة بيانات الدفع</b>

<b>حدد بيانات استلام المدفوعات:</b>
• <tg-emoji emoji-id='5992430854909989581'>🪙</tg-emoji> محفظة العملات المشفرة — العنوان والشبكة (Ton، Trc-20، إلخ)
• <tg-emoji emoji-id='5445353829304387411'>💳</tg-emoji> بطاقة — لاستلام الروبل وعملات أخرى
• 📱 هاتف — بالصيغة الدولية

<b>ملاحظة:</b> لا تحتاج Stars إلى بيانات دفع

<b>هام:</b> أدخل بيانات دفع موثوقة فقط!

<b>اختر النوع:</b>""",
        'wallet_ton_hint': """• الصيغة: UQ... أو EQA...
• تحقق من صحة العنوان
• يجب أن يبدأ العنوان بـ UQ أو EQ
<i>سيتم حفظ العنوان لاستلام المدفوعات</i>""",
        'wallet_card_hint': """• الصيغة: 2200 1234 5678 9010
• أو: البنك — رقم البطاقة
• تدعم بطاقات RU وBY وKZ وUA
<i>سيتم حفظ البيانات لاستلام مدفوعات الروبل</i>""",
        'wallet_phone_hint': """• الصيغة: +79991234567
• يُستخدم لـ Qiwi/юmoney
• أدخل الرقم مع رمز الدولة
<i>سيتم حفظ الرقم لاستلام المدفوعات</i>""",
        'wallet_usdt_hint': """• الصيغة: T... (شبكة TRC20)
• تحقق من صحة العنوان
• شبكة TRC20 فقط!
<i>سيتم حفظ العنوان لاستلام Usdt</i>""",
        'btn_add_worker': 'إضافة موظف',
        'btn_remove_worker': 'إزالة موظف',
        'btn_check_deals': 'فحص الصفقات',
        'btn_demote_worker': 'تخفيض رتبة موظف',
        'btn_export_csv': 'تصدير إلى CSV',
        'btn_worker_panel_nav': 'لوحة الموظف',
        'btn_admin_panel_nav': 'لوحة الإدارة',
        'btn_stats': 'الإحصائيات',
        'btn_my_profile_nav': 'ملفي الشخصي',
        'btn_my_items': 'منتجاتي',
        'btn_my_deals_nav2': 'صفقاتي',
        'btn_manage_tag': 'إدارة العلامة',
        'btn_to_worker_panel': 'لوحة الموظف',
        'btn_confirm_deposit': 'تأكيد الشحن',
        'btn_decline': 'رفض',
        'btn_verify_user': 'توثيق',
        'btn_unverify_user': 'إلغاء التوثيق',
        'btn_not_paid': 'لم يدفع',
        'btn_not_sent': 'لم يرسل',
        'btn_wrong_item': 'منتج خاطئ',
        'btn_other_reason': 'سبب آخر',
        'dispute_title': '<tg-emoji emoji-id="5904692292324692386">⚠️</tg-emoji> <b>فتح نزاع</b>',
        'dispute_deal': '<tg-emoji emoji-id="5956561916573782596">📋</tg-emoji> <b>الصفقة:</b>',
        'dispute_role': "<tg-emoji emoji-id='6041705726206808304'>👤</tg-emoji> <b>دورك:</b>",
        'dispute_role_buyer': 'المشتري',
        'dispute_role_seller': 'البائع',
        'dispute_support': '👨\u200d💼 <b>دعم الصفقة:</b>',
        'dispute_confirm': '<b>هل أنت متأكد من رغبتك في فتح نزاع؟</b>\n<i>سيراجع المسؤول نزاعك خلال 24 ساعة.</i>',
        'dispute_reason': '<b>اختر السبب:</b>',
        'btn_contact_manager': 'التواصل مع المدير',
        'btn_to_deal': 'الذهاب إلى الصفقة',
        'btn_contact_support': 'الدعم الفني',
        'admin_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم رفض الوصول. هذا الإجراء متاح للمسؤولين فقط',
        'admin_complete_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم رفض الوصول. إتمام الصفقات متاح للمسؤولين فقط',
        'admin_confirm_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم رفض الوصول. تأكيد استلام المنتج متاح للمسؤولين فقط',
        'owner_only_admins': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم رفض الوصول. عرض قائمة جميع المسؤولين متاح لمالك النظام فقط',
        'owner_only_add_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم رفض الوصول. إضافة المسؤولين متاحة لمالك النظام فقط',
        'owner_only_remove_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم رفض الوصول. إزالة المسؤولين متاحة لمالك النظام فقط',
        'admin_block_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم رفض الوصول. إدارة الحظر متاحة للمسؤولين فقط',
        'cannot_block_owner': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> لا يمكن حظر مالك النظام',
        'already_blocked': '⚠️ المستخدم محظور بالفعل',
        'owner_unblock_only': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> إلغاء حظر مالك النظام متاح لمالك النظام فقط',
        'not_blocked': '⚠️ المستخدم غير محظور',
        'user_not_worker': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> المستخدم ليس موظفًا',
        'method_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> الطريقة غير موجودة',
        'error_generic': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> حدث خطأ',
        'deposit_approved': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> تم تأكيد الشحن!',
        'deposit_error': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> خطأ في التأكيد',
        'deposit_declined': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم رفض الشحن',
        'deposit_declined_user': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم رفض طلب شحن رصيدك من قبل المسؤول. تواصل مع الدعم الفني لمعرفة السبب.',
        'user_verified_alert': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> تم توثيق المستخدم',
        'user_unverified_alert': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> تم إلغاء التوثيق',
        'data_saved': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> تم حفظ البيانات بنجاح!',
        'you_are_blocked': '<tg-emoji emoji-id="5922712343011135025">🚫</tg-emoji> تم حظرك',
        'export_in_dev': '📥 ميزة التصدير قيد التطوير',
        'lang_changed': '<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji> تم تغيير اللغة!',
        'payment_not_supported': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> الدفع عبر التأكيد لم يعد مدعومًا. استخدم الدفع من الرصيد.',
        'invalid_id_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>تنسيق الرقم غير صحيح</b>\n\nأدخل عددًا صحيحًا',
        'invalid_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>تنسيق غير صحيح</b>',
        'invalid_amount_format': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>تنسيق المبلغ غير صحيح</b>\n\nأدخل رقمًا، مثل: 1000 أو 0.01',
        'invalid_currency': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>عملة غير صحيحة</b>',
        'user_not_found_id': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>المستخدم غير موجود</b>',
        'cannot_block_owner_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>لا يمكن حظر مالك النظام</b>',
        'cannot_remove_owner': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>لا يمكن إزالة مالك النظام</b>',
        'cannot_add_owner_admin': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>لا يمكن إضافة مالك النظام كمسؤول</b>',
        'edit_cancelled': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>تم إلغاء التعديل.</b>',
        'method_not_found_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>خطأ: الطريقة غير موجودة.</b>',
        'send_receipt_first': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> يرجى أولاً اختيار طريقة الشحن وإدخال المبلغ.',
        'send_photo_doc': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> يرجى إرسال صورة أو مستند يحتوي على الإيصال.',
        'deal_deleted': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>الصفقة غير موجودة</b>\n\nتم حذف الصفقة أو أنها غير موجودة.',
        'scam_desc_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>الوصف قصير جدًا</b>\n\nصف بالتفصيل ما حدث من احتيال (3 أحرف على الأقل).',
        'deal_complete_error': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>خطأ في إتمام الصفقة</b>\n\nتعذر إتمام الصفقة.',
        'amount_negative': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>مبلغ غير صحيح</b>\n\nيجب أن يكون المبلغ أكبر من 0',
        'amount_too_small': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>المبلغ صغير جدًا</b>',
        'insufficient_funds_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>الرصيد غير كافٍ</b>',
        'tag_must_start_hash': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>يجب أن تبدأ العلامة برمز #</b>\n\nمثال: #best_worker',
        'tag_too_short': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>العلامة قصيرة جدًا</b>\n\nالحد الأدنى حرفان (بما في ذلك #)',
        'tag_too_long': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>العلامة طويلة جدًا</b>\n\nالحد الأقصى 20 حرفًا',
        'tag_already_used': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>هذه العلامة مستخدمة بالفعل</b>',
        'no_recipients': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>لا يوجد مستلمون</b>\n\nلم يتم العثور على مستلمين لنوع البث المحدد.',
        'verified_not_found': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>لم يتم العثور على مستخدمين موثقين</b>',
        'deals_not_found_search': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>لم يتم العثور على صفقات</b>',
        'users_not_found_search': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>لم يتم العثور على مستخدمين</b>',
        'bot_error': 'خطأ في استخدام البوت.',
        'access_denied_block': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>تم رفض الوصول</b>\n\nحظر المستخدمين متاح للمسؤولين فقط.',
        'access_denied_unblock': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>تم رفض الوصول</b>\n\nإلغاء حظر المستخدمين متاح للمسؤولين فقط.',
        'access_denied_full': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> <b>تم رفض الوصول</b>\nليس لديك صلاحيات المسؤول',
        'deals_negative': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> لا يمكن أن يكون عدد الصفقات سالبًا',
        'enter_integer': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> أدخل عددًا صحيحًا',
        'amount_negative_balance': '<tg-emoji emoji-id="5920344347152224466">❌</tg-emoji> لا يمكن أن يكون المبلغ سالبًا',
        'btn_deposit_card_ru': 'بطاقة روسية',
        'btn_deposit_card_ua': 'بطاقة أوكرانية',
        'btn_deposit_crypto': 'عملات رقمية',
        'btn_deposit_stars': 'نجوم تيليجرام',
        'btn_payment_ton':   '⚡ Ton',
        'btn_payment_crypto': '🪙 محفظة العملات المشفرة',
        'btn_payment_card':  '💳 بطاقة',
        'btn_payment_phone': '📱 هاتف',
        'btn_payment_usdt':  '💎 Usdt',
        'btn_role_seller':   '🔥 أنا البائع',
        'btn_role_buyer':    '🛒 أنا المشتري',
        'deal_role_title':   '🧾 <b>صفقة جديدة</b>',
        'deal_role_question':'💬 <i>ما هو دورك في هذه الصفقة؟</i>',
        'deal_role_seller_desc': '🔥 <b>البائع</b> — تبيع منتجاً/خدمة وتستلم الدفع.',
        'deal_role_buyer_desc':  '🛒 <b>المشتري</b> — تدفع وتستلم المنتج/الخدمة.',
        'not_specified':  'غير محدد',
        'not_specified_f':'غير محددة',
    },
}


def get_text(user_id, key, users_dict=None):
    """Получает локализованный текст для пользователя"""
    lang = 'ru'
    if users_dict and user_id in users_dict:
        lang = users_dict[user_id].get('lang', 'ru')
    texts = TEXTS.get(lang, TEXTS['ru'])
    text = texts.get(key, TEXTS['ru'].get(key, key))
    if lang == 'ar' and isinstance(text, str) and text:
        # RTL-выравнивание для арабского: оборачиваем текст в Unicode-маркеры
        # Right-to-Left Embedding (RLE) ... Pop Directional Formatting (PDF),
        # плюс RLM в начале каждой строки, чтобы Telegram стабильно выравнивал
        # текст и пунктуацию справа налево даже при наличии HTML-тегов,
        # эмодзи и плейсхолдеров вида {amount}.
        RLM = '\u200f'
        lines = text.split('\n')
        text = '\n'.join((RLM + line) if line.strip() else line for line in lines)
    if isinstance(text, str) and '{BOT_NAME}' in text:
        try:
            from bot_core import BOT_NAME
            text = text.replace('{BOT_NAME}', BOT_NAME)
        except Exception:
            text = text.replace('{BOT_NAME}', 'Lolz')
    if isinstance(text, str) and '{MANAGER_USERNAME}' in text:
        try:
            from bot_core import MANAGER_USERNAME
            text = text.replace('{MANAGER_USERNAME}', MANAGER_USERNAME)
        except Exception:
            pass
    return text


def get_lang(user_id, users_dict=None):
    """Получает язык пользователя"""
    if users_dict and user_id in users_dict:
        return users_dict[user_id].get('lang', 'ru')
    return 'ru'
