import telebot
from telebot import types
from mozg1 import *

bot = telebot.TeleBot(token = '7066746516:AAHNRpBGzfUILWwMBH-QLbca6WJUqdT_iGs')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    bot.send_message(user_id,'Привет, Добро пожаловать в туристическое агенство' + '\n /help - если нужна помощь')

@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.chat.id
    help_text = 'Выберите действие:'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    button1 = types.KeyboardButton('Информация об отелях')
    button2 = types.KeyboardButton('Билеты')
    button3 = types.KeyboardButton('Контакты нашей компании')

    markup.row(button1)
    markup.row(button2, button3)
    bot.send_message(user_id,help_text,reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def text_message_handler(message):
    user_id = message.chat.id
    text = message.text.lower()

    if text == 'контакты нашей компании':
        bot.send_message(user_id, contacts)
    #elif text == ''

bot.polling(none_stop=True)