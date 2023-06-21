from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

Inline_keyboard_one = InlineKeyboardMarkup(row_width=2)
Inline_keyboard_two = InlineKeyboardMarkup(row_width=2)

Inline_keyboard_one.add(
    InlineKeyboardButton('Зрозуміло', callback_data="Main_Func")
)

Inline_keyboard_two.add(
    InlineKeyboardButton('Повернутись назад', callback_data="back"),
)
