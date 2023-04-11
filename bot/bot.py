from telebot import TeleBot, types

from config import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)
r = 0

huylo = 5
users = {} 


@bot.message_handler(commands=['start'])
def start_command(msg: types.Message):
    bot.send_message(msg.chat.id, 'Enter your name:')
    bot.register_next_step_handler(msg, get_user_name)

def get_user_name(msg: types.Message):
    name = msg.text
    users[msg.from_user.id] = {'name': msg.text}
    bot.send_message(msg.chat.id, f'Hi {name}, how old  are you ')
    bot.register_next_step_handler(msg, get_user_age)

def get_user_age(msg: types.Message):
    age = msg.text
    try:
        age = int(age)
    except ValueError:
        bot.send_message(msg.chat.id, 'Enter a number')
        bot.register_next_step_handler(msg, get_user_age)
        return

    user = users[msg.from_user.id]
    user['age'] = age

    bot.send_message(msg.chat.id, f'great! {user["name"]} Now enter your gender (M or F)')
    bot.register_next_step_handler(msg, get_user_gender)

def get_user_gender(msg: types.Message):
    user = users[msg.from_user.id]
    gender = msg.text
    if gender not in ('M', 'F'):
        bot.send_message(msg.chat.id, 'something went wrong ')
        bot.register_next_step_handler(msg, get_user_gender)
        return
    user = users[msg.from_user.id]
    user['gender'] = gender

    bot.send_message(msg.chat.id, f'Uhu your name:{user["name"]}\n your age {user["age"]}\n your gender {user["gender"]}',
    )





bot.infinity_polling()
