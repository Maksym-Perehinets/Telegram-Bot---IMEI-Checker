from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

Inline_keyboard_one = InlineKeyboardMarkup(row_width=2)
Inline_keyboard_back = InlineKeyboardMarkup(row_width=2)
Inline_keyboard_get_file = InlineKeyboardMarkup(row_width=2)
Inline_keyboard_balance = InlineKeyboardMarkup(row_width=2)

Inline_keyboard_one.add(
    InlineKeyboardButton('Зрозуміло', callback_data="Main_Func")
)

Inline_keyboard_back.add(
    InlineKeyboardButton('Повернутись назад', callback_data="back"),
)

Inline_keyboard_get_file.add(
    InlineKeyboardButton('Отримати txt файл з даними', callback_data="generate_file")
)

Inline_keyboard_balance.add(
    InlineKeyboardButton('Повернутись назад', callback_data="back"),
    InlineKeyboardButton('Поповнити рахунок', url="https://t.me/Maksym_Per"),
)