from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Creation of buttons
markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# Creation of main butttons
markup.add(
    KeyboardButton('Test api request'),
    KeyboardButton(''),
    KeyboardButton('None'))
