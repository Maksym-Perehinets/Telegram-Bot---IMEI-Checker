from telebot import TeleBot, types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from imei_http_req import ImeiRequests
from config import BOT_TOKEN


bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(msg: types.Message):
    bot.send_message(msg.chat.id, "Привіт тепер ти можеш мене використовувати!")
    bot.register_next_step_handler(msg, buttons)


@bot.message_handler(commands=['button'])
def buttons(msg: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton('Cheak my imei'), KeyboardButton('Test http req'), KeyboardButton('None'))
    bot.send_message(msg.chat.id, 'chose what you need', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def button_answ(msg: types.Message):
    if msg.text == 'Cheak my imei':
        bot.send_message(msg.chat.id, 'Enter your imei:')
        bot.register_next_step_handler(msg, imei_cheak)
    elif msg.text == 'Test http req':
        bot.send_message(msg.chat.id, str(ImeiRequests.test_request()))
        bot.register_next_step_handler(msg, imei_cheak)
    bot.register_next_step_handler(msg, buttons)



def imei_cheak(msg: types.Message):
    bot.send_message(msg.chat.id, f"imei {msg.text} is valid")


bot.infinity_polling()
