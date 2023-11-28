import telebot
from telebot import types

bot_token = "6801426896:AAEe_QBTudQG2xBjR408CTgKjemgsYdIJ2g"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Написать боту", url="https://t.me/begemot_robot")
    markup.add(button)

    bot.reply_to(message, "Привет! Я бот. Как дела?", reply_markup=markup)

def run_bot():
    try:
        bot.polling()
    except Exception as e:
        print(f"An error occurred: {e}")

run_bot()
