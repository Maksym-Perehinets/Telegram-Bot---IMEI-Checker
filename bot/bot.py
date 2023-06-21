import json
from telebot import TeleBot, types
from imei_http_req import ImeiRequests
from config import BOT_TOKEN
from time import sleep
from Inline_keyboard import Inline_keyboard_one, Inline_keyboard_two
from ReplyKeyboard import markup, markup_back

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])  # Start comad hendler
def start_command(msg: types.Message):
    # Redirecting to the next stage
    bot.send_message(msg.chat.id, "Привіт я розроблений з метою полегшення перевірки IMEI твого iPhone. "
                                  "Коротнка інформація. Для поповнення балансу напишіть @user",
                     reply_markup=Inline_keyboard_one
                     )


@bot.callback_query_handler(func=lambda msg: True)
def response(msg):
    if msg.data == 'back':
        bot.send_message(msg.message.chat.id, "Menue", reply_markup=markup)
        bot.register_next_step_handler(msg.message, messages)
    else:
        bot.send_message(msg.message.chat.id, "Menue", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def messages(msg):
    print('messages')
    service_id = ImeiRequests.get_id(None, msg.text)
    bot.send_message(msg.chat.id, "Send your Imei number", reply_markup=Inline_keyboard_two)
    bot.register_next_step_handler(msg, imei_resp, service_id)


def imei_resp(msg, service_id):
    print('imei_response')
    if ImeiRequests.get_id(None, msg.text) is None:
        bot.send_message(msg.chat.id, ImeiRequests.user_request(None, service_id, msg.text))

if __name__ == '__main__':
    try:
        bot.infinity_polling()
    except NameError:
        sleep(10)
        bot.infinity_polling()
