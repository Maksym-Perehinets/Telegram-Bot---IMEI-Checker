from telebot import TeleBot, types
from imei_http_req import ImeiRequests
from config import BOT_TOKEN
from time import sleep
from ReplyKeyboard import markup, markup2

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])  # Start comad hendler
def start_command(msg: types.Message):
    bot.send_message(msg.chat.id, "Привіт я розроблений з метою полегшення перевірки IMEI твого iPhone")
    # Redirecting to the next stage
    bot.register_next_step_handler(msg, buttons)


@bot.message_handler(commands=['button'])  # Defining a function with buttons
def buttons(msg: types.Message):
    bot.send_message(msg.chat.id, 'Доступні опції', reply_markup=markup)
    bot.register_next_step_handler(msg, button_answ)


# Button press handler

def button_answ(msg: types.Message):
    if msg.text == 'Check my imei':  # Case one(checking imei actuality)
        bot.send_message(msg.chat.id, 'Enter your imei:')
    elif msg.text == 'Icloud ON/Of':  # Case two(sending a test request)
        bot.send_message(msg.chat.id, str(ImeiRequests.valid_price_and_balance_check()))
        bot.send_message(msg.chat.id, 'Бажаєте вернутись назад', reply_markup=markup2)
        bot.register_next_step_handler(msg, buttons)  # Returns to menu
    else:
        bot.send_message(msg.chat.id, 'Incorrect command')
        bot.register_next_step_handler(msg, buttons)


if __name__ == '__main__':
    try:
        bot.infinity_polling()
    except NameError:
        sleep(10)
        bot.infinity_polling()
