import telebot
from telebot import types

TOKEN = "855474923:AAES5V4roQy8REHoKJthcsZtOGMf2GbQS98"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["start"])
def start(message):
    registration_markup = types.InlineKeyboardMarkup()
    registration_markup.add(types.InlineKeyboardButton(text ="Зарегестрироваться", callback_data="registration"))
    bot.send_message(message.from_user.id, "Привет, я твой помошник в бизнесе \nЯ помогу в коммуникации с твоей командой \nВот мои умения:\n-\n-\n- ", reply_markup=markup)

@bot.message_handler(content_types = ["text"])
def text_handler(message):
    bot.send_message(message.from_user.id, "Пожалуйста работайте с меню.")

bot.polling(True)