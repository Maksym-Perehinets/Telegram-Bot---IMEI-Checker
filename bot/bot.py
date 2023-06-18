from telebot import TeleBot, types
from imei_http_req import ImeiRequests
from config import BOT_TOKEN
from time import sleep
from Inline_keyboard import Inline_keyboard_one, Inline_keyboard_two
from ReplyKeyboard import markup, markup2

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])  # Start comad hendler
def start_command(msg: types.Message):
    # Redirecting to the next stage
    bot.send_message(msg.chat.id, "Привіт я розроблений з метою полегшення перевірки IMEI твого iPhone. "
                                  "Коротнка інформація. Для поповнення балансу напишіть @user", reply_markup=Inline_keyboard_one)


@bot.callback_query_handler(func=lambda msg: True)
def response(msg):
    if msg.data == "Main_Func":
        ImeiRequests.geting_valid_price_information()
        bot.send_message(msg.message.chat.id, "Menue", reply_markup=markup)
@bot.message_handler(content_types=["text"])
def buttons(msg):
    if msg.text == "Icloud ON/Of":
        bot.send_message(msg.chat.id, )
if __name__ == '__main__':
    try:
        bot.infinity_polling()
    except NameError:
        sleep(10)
        bot.infinity_polling()