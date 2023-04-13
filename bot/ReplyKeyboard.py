from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Creation of buttons
markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# Creation of main butttons
markup.add(
    KeyboardButton('Check my imei'),
    KeyboardButton('Test http req'),
    KeyboardButton('None'))