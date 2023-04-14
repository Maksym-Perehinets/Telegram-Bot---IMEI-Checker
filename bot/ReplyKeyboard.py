from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Creation of buttons
markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# Creation of main butttons
markup.add(
    KeyboardButton('Icloud ON/Of'),
    KeyboardButton('Icloud clean/lost'),
    KeyboardButton('Перевірка оператора'),
    KeyboardButton('Перевірка lock/unlock'),
    KeyboardButton('Перевірка MDM статусу Iphone'),
    KeyboardButton('Перевірка Icloud на Mac'),
    KeyboardButton('Serial number to IMEI'),
    KeyboardButton('IMEI to serial number'),
    KeyboardButton('Iphone Basic info'),  # Apple basic check
    KeyboardButton('Iphone Advanced info'),  # Apple Advanced check
    KeyboardButton('Activation check'),
    KeyboardButton('Дата Купівлі'),
    KeyboardButton('Перевірка MDM (Mac, Ipad, Iphone)'),
    KeyboardButton('Мій аккаунт'),
    KeyboardButton('Перевірка оператора')
    )
