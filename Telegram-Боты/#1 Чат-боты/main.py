# Импортируем библиотеки
import telebot
import time
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📄 Заполнить анкету")

    markup.add(item1)

    bot.send_message(message.chat.id, "👋 Привет! Я тестовый Бот для статьи Дзен.", reply_markup=markup) # Сообщение от бота с созданием клавиатуры
    bot.register_next_step_handler(message, name_user1) # Переход к следующей функции после сообщения
def name_user1(message):
    if message.text == '📄 Заполнить анкету':
        bot.send_message(message.chat.id, "✏️ Введите Ваше Имя:") # Запрос на ввод имени
        bot.register_next_step_handler(message, age_user) # Переход к следующей функции после ввода
    if message.text == '🏠 Домой':
        bot.register_next_step_handler(message, start_message) # Переход к начальной функции после нажатии на кнопку
def name_user2(message):
    bot.send_message(message.chat.id, "✏️ Введите Ваше Имя:") # Запрос на ввод имени
    bot.register_next_step_handler(message, age_user) # Переход к следующей функции после ввода
def age_user(message):
    global name # Объявляем переменную глобальной
    name = message.text # Ответ пользователя записываем в переменную
    bot.send_message(message.chat.id, "✏️ Введите ваш возраст:") # Запрос на ввод возраста
    bot.register_next_step_handler(message, next_age) # Переход к следующей функции после ввода
def next_age(message):
    global age # Объявляем переменную глобальной
    age = message.text # Ответ пользователя записываем в переменную

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🏠 Домой")

    markup.add(item1)

    bot.send_message(message.chat.id, f"Я немного о тебе узнал\nВаше имя: {name}\nВаш возраст: {age}", reply_markup=markup) # Выводим данные о пользователя и создаём клавиатуру
    bot.register_next_step_handler(message, name_user1)

bot.polling(none_stop=True)
