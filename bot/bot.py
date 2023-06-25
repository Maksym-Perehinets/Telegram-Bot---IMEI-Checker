from telebot import TeleBot, types
from imei_http_req import ImeiRequests
from config import BOT_TOKEN
from time import sleep
from Inline_keyboard import Inline_keyboard_one, Inline_keyboard_back, Inline_keyboard_get_file
from ReplyKeyboard import markup

bot = TeleBot(BOT_TOKEN)

resp_file = None

@bot.message_handler(commands=['start'])  # Start comad hendler
def start_command(msg: types.Message):
    # Redirecting to the next stage
    bot.send_message(msg.chat.id, "Привіт я розроблений з метою полегшення перевірки IMEI твого iPhone. ",
                     reply_markup=Inline_keyboard_one
                     )


@bot.callback_query_handler(func=lambda msg: True)
def response(msg):
    if msg.data == 'back':
        bot.send_message(msg.message.chat.id, "Menue", reply_markup=markup)
        bot.register_next_step_handler(msg.message, messages)
    elif msg.data == 'generate_file':
        global resp_file
        bot.edit_message_reply_markup(msg.message.chat.id, msg.message.id)
        a = bot.send_document(msg.message.chat.id, document=resp_file, visible_file_name='response.json')
        bot.send_message(msg.message.chat.id, "Menue", reply_markup=markup)
    else:
        bot.send_message(msg.message.chat.id, "Menue", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def messages(msg):
    service_id = ImeiRequests.get_id(None, msg.text)
    bot.send_message(msg.chat.id, "Send your Imei number", reply_markup=Inline_keyboard_back)
    bot.register_next_step_handler(msg, imei_resp, service_id)


def imei_resp(msg, service_id):
    if ImeiRequests.get_id(None, msg.text) is None:
        global resp_file
        resp = ImeiRequests.user_request(None, service_id, msg.text)
        resp_file = ImeiRequests.response_to_file(None, resp)
        bot.send_message(msg.chat.id, resp, reply_markup=Inline_keyboard_get_file)




if __name__ == '__main__':
    try:
        bot.infinity_polling()
    except NameError:
        sleep(10)
        bot.infinity_polling()
