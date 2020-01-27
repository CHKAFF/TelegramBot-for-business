import telebot
from telebot import types

TOKEN = "855474923:AAES5V4roQy8REHoKJthcsZtOGMf2GbQS98"
bot = telebot.TeleBot(TOKEN)

menu_markup = types.InlineKeyboardMarkup(row_width=1)
feedback_button = types.InlineKeyboardButton(text = "Запросить Feedback", callback_data= "feedback")
event_button = types.InlineKeyboardButton(text = "Оповестить о Мероприятии", callback_data= "event")
meeting_button = types.InlineKeyboardButton(text = "Оповестить о Совещании", callback_data= "meeting")
menu_markup.add(feedback_button, event_button, menu_markup)

@bot.message_handler(commands = ["start"])
def start(message):
    registration_markup = types.InlineKeyboardMarkup()
    registration_markup.add(types.InlineKeyboardButton(text ="Зарегестрироваться", callback_data="registration"))
    bot.send_message(message.from_user.id, "Привет, я твой помошник в бизнесе \nЯ помогу в коммуникации с твоей командой \nВот мои умения:\n-\n-\n- ", reply_markup=registration_markup)

@bot.message_handler(content_types = ["text"])
def text_handler(message):
    bot.send_message(message.from_user.id, "Пожалуйста работайте с меню.")

@bot.callback_query_handler(func=lambda call:True)
def callback_handler(call):
    try:
        if call.message:
            if call.data == "registration":
                bot.send_message(call.from_user.id, "Поздравляем, вы стали членом нашей дружно команды!\nТеперь вы будете получать уведомления о совещаниях и предстоящих событиях, так же у вас есть возможность самим предупреждать людей и собирать Фидбэки по прошедшим мероприятиям.")
    except Exception as e:
        print(repr(e))
bot.polling(True)