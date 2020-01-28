import telebot
from telebot import types

TOKEN = "855474923:AAES5V4roQy8REHoKJthcsZtOGMf2GbQS98"
bot = telebot.TeleBot(TOKEN)

menu_markup = types.InlineKeyboardMarkup(row_width=1)
feedback_button = types.InlineKeyboardButton(text = "Запросить Feedback", callback_data= "feedback")
event_button = types.InlineKeyboardButton(text = "Оповестить о Мероприятии", callback_data= "event")
meeting_button = types.InlineKeyboardButton(text = "Оповестить о Совещании", callback_data= "meeting")
menu_markup.add(feedback_button, event_button, meeting_button)

admin_markup = types.InlineKeyboardMarkup(row_width=2)
employees_list = types.InlineKeyboardButton(text = "Список сотрудников", callback_data= "employees_list")
employee_add = types.InlineKeyboardButton(text = "Добавить сотрудника", callback_data= "employee_add")
employee_delete = types.InlineKeyboardButton(text = "Удалить сотрудника", callback_data= "employee_delete")
exit_button = types.InlineKeyboardButton(text = "Выйти", callback_data= "exit_button")
admin_markup.add(employees_list, employee_add, employee_delete, exit_button)

@bot.message_handler(commands = ["start"])
def start(message):
    registration_markup = types.InlineKeyboardMarkup()
    registration_markup.add(types.InlineKeyboardButton(text ="Зарегестрироваться", callback_data="registration"))
    bot.send_message(message.from_user.id, "Привет, я твой помошник в бизнесе \nЯ помогу в коммуникации с твоей командой \nВот мои умения:\n-\n-\n- ", reply_markup=registration_markup)

@bot.message_handler(commands = ["admin"])
def admin(message):
    if message.text == "/admin adminsuper":
        bot.send_message(message.from_user.id, "Это Меню Админа, здесь мы можете ПОСМОТРЕТЬ всех сотрудников, УДАЛИТЬ или ДОБАВИТЬ новых", reply_markup=admin_markup)
    else:
        bot.send_message(message.from_user.id, "Пароль неверный")

@bot.message_handler(content_types = ["text"])
def text_handler(message):
    bot.send_message(message.from_user.id, "Пожалуйста работайте с меню.")

@bot.callback_query_handler(func=lambda call:True)
def callback_handler(call):
    try:
        if call.message:
            if call.data == "registration":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Поздравляем, вы стали членом нашей дружно команды!\nТеперь вы будете получать уведомления о совещаниях и предстоящих событиях, так же у вас есть возможность самим предупреждать людей и собирать Фидбэки по прошедшим мероприятиям.", reply_markup=menu_markup)
            elif call.data == "feedback":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="good", reply_markup=menu_markup)
            elif call.data == "event":
                pass
            elif call.data == "meeting":
                pass
            elif call.data == "employees_list":
                pass
            elif call.data == "employee_add":
                pass
            elif call.data == "employee_delete":
                pass
    except Exception as e:
        print(repr(e))

bot.polling(True)