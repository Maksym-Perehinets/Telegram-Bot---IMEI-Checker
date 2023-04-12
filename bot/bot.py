from telebot import TeleBot, types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import json
from config import BOT_TOKEN


bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(msg: types.Message):
    bot.send_message(msg.chat.id, "Привіт тепер ти можеш мене використовувати!")
    bot.register_next_step_handler(msg, buttons)


@bot.message_handler(commands=['button'])
def buttons(msg: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton('Cheak my imei'), KeyboardButton('Say my name'), KeyboardButton('None'))
    bot.send_message(msg.chat.id, 'chose what you need', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def button_answ(msg: types.Message):
    if msg.text == 'Cheak my imei':
        bot.send_message(msg.chat.id, 'Enter your imei:')
    elif msg.text == 'Say my name':
        msg_json = msg.json['from']
        bot.send_message(msg.chat.id, str(msg_json['first_name']))
    bot.register_next_step_handler(msg, imei_cheak)


def imei_cheak(msg: types.Message):
    bot.send_message(msg.chat.id, f"imei {msg.text} is valid")


bot.infinity_polling()
