from telebot import TeleBot, types
from imei_http_req import ImeiRequests
from config import BOT_TOKEN
from time import sleep
from ReplyKeyboard import markup

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])  # Start comad hendler
def start_command(msg: types.Message):
    bot.send_message(msg.chat.id, "Привіт тепер ти можеш мене використовувати!")
    # Redirecting to the next stage
    bot.register_next_step_handler(msg, buttons)


@bot.message_handler(commands=['button'])  # Defining a function with buttons
def buttons(msg: types.Message):
    bot.send_message(msg.chat.id, 'Menu', reply_markup=markup)


@bot.message_handler(content_types=['text'])  # Button press handler
def button_answ(msg: types.Message):
    if msg.text == 'Check my imei':  # Case one(checking imei actuality)
        bot.send_message(msg.chat.id, 'Enter your imei:')
        bot.register_next_step_handler(msg, imei_cheak)
    elif msg.text == 'Test api req':  # Case two(sending a test request)
        bot.send_message(msg.chat.id, str(ImeziRequests.test_request()))
        bot.register_next_step_handler(msg, buttons)
    bot.register_next_step_handler(msg, buttons)  # Returns to options


def imei_cheak(msg: types.Message):  # Doing shit and lie =)
    bot.send_message(msg.chat.id, f"imei {msg.text} is valid")
    bot.register_next_step_handler(msg, buttons)


if __name__ == '__main__':
    try:
        bot.infinity_polling()
    except NameError:
        sleep(10)
        bot.infinity_polling()
