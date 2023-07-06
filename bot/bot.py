from telebot import TeleBot, types
from imei_http_req import ImeiRequests
from credentials.config import BOT_TOKEN
from time import sleep
from Inline_keyboard import Inline_keyboard_one, Inline_keyboard_back, Inline_keyboard_get_file, Inline_keyboard_balance
from ReplyKeyboard import markup
from sheets_api import SheetApi

bot = TeleBot(BOT_TOKEN)

resp_file = None
IMEI = ImeiRequests()
sh_api = SheetApi()


@bot.message_handler(commands=['start'])  # Handle start command and add user id to the table 
def start_command(msg: types.Message):
    # Redirecting to the next stage
    bot.send_message(msg.chat.id,
                     "Привіт я розроблений з метою полегшення перевірки IMEI твого iPhone. "
                     "Created by https://t.me/Maksym_Per",
                     reply_markup=Inline_keyboard_one
                     )
    sh_api.creat_new_user(str(msg.from_user.id))


@bot.callback_query_handler(func=lambda msg: True)
def response(msg):
    if msg.data == 'back':
        bot.send_message(msg.message.chat.id, "Menue", reply_markup=markup)
        bot.register_next_step_handler(msg.message, messages)
    elif msg.data == 'generate_file':
        global resp_file
        bot.edit_message_reply_markup(msg.message.chat.id, msg.message.id)
        bot.send_document(msg.message.chat.id, document=resp_file, visible_file_name='response.txt')
        bot.send_message(msg.message.chat.id, "Menue", reply_markup=markup)
    else:
        bot.send_message(msg.message.chat.id, "Menue", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def messages(msg):
    service_id = IMEI.get_id(msg.text)
    # check whether user wants to check balance or make purchase
    if service_id != 78564:
        bot.send_message(msg.chat.id,
                         "Відправте імеі вашого пристрою та очікуйте перевірка може зайняти до 3ох хвилин.\n"
                         f"Вартість данної послуги складе {IMEI.price_inf(service_id)}",
                         reply_markup=Inline_keyboard_back)
        bot.register_next_step_handler(msg, imei_resp, service_id)
    else:
        # Output balance
        bot.send_message(msg.chat.id, f"Ваш telegram ID: {str(msg.from_user.id)}\n"
                                      f"Ваш баланс: {sh_api.get_balance(str(msg.from_user.id))}$",
                         reply_markup=Inline_keyboard_balance)


def imei_resp(msg, service_id):
    if IMEI.get_id(msg.text) is None:
        global resp_file
        resp = IMEI.user_request(service_id, msg.text, str(msg.from_user.id))  # Get IMEI response
        resp_file = IMEI.response_to_file(resp)

        if isinstance(resp_file, str):
            bot.send_message(msg.chat.id, "Ваш запит було відхилено "
                                          "перевіте правильність введених данних", reply_markup=markup)
        else:
            bot.send_message(msg.chat.id, resp, reply_markup=Inline_keyboard_get_file)


if __name__ == '__main__':
    try:
        bot.infinity_polling()
    except NameError:
        sleep(10)
        bot.infinity_polling()
