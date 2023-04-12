from telebot import TeleBot, types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from imei_http_req import ImeiRequests
from config import BOT_TOKEN


bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])  # Start comad hendler
def start_command(msg: types.Message):
    bot.send_message(msg.chat.id, "Привіт тепер ти можеш мене використовувати!")
    # Redirecting to the next stage
    bot.register_next_step_handler(msg, buttons)


@bot.message_handler(commands=['button'])  # Defining a function with buttons
def buttons(msg: types.Message):
    # Creation of buttons
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # Creation of main butttons
    markup.add(
        KeyboardButton('Check my imei'),
        KeyboardButton('Test http req'),
        KeyboardButton('None'))
    bot.send_message(msg.chat.id, 'chose what you need', reply_markup=markup)


@bot.message_handler(content_types=['text'])  # Button press hendler
def button_answ(msg: types.Message):
    if msg.text == 'Check my imei':  # Case one(checking imei actuality)
        bot.send_message(msg.chat.id, 'Enter your imei:')
        bot.register_next_step_handler(msg, imei_cheak)
    elif msg.text == 'Test http req':  # Case two(sending a test request)
        bot.send_message(msg.chat.id, str(ImeiRequests.test_request()))
        bot.register_next_step_handler(msg, imei_cheak)
    bot.register_next_step_handler(msg, buttons)  # Returns to options


def imei_cheak(msg: types.Message):  # Doing shit and lie =)
    bot.send_message(msg.chat.id, f"imei {msg.text} is valid")


bot.infinity_polling()
