import telebot
from telebot import types

TOKEN = ""
bot = telebot.TeleBot(TOKEN)

keybard = types.ReplyKeyboardMarkup()
first_item =

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat_id, "Привет, я твойй помошник в бизнесе \nЯ помогу в коммуникации с твоей командой \nВот мои умения:\n-\n-\n- ")

@bot.message_handler(content_types = ["text"])