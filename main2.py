import telebot
from telebot import types
import os
from flask import Flask
from threading import Thread

# Настройка веб-сервера для Render
app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Твой бот
TOKEN = "8817308182:AAHkidg_jVmrsIK2RrQjkbPXXiBAjXlZCes" # Сюда токен!
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    apps = [
        ("🐱 Поймай ы", "https://iniqkpidjosrpflezxnt.supabase.co/..."), # Вставь полные ссылки
        ("🚀 Star Warrior", "https://iniqkpidjosrpflezxnt.supabase.co/..."),
        ("📱 Шипучка Грамм", "https://iniqkpidjosrpflezxnt.supabase.co/..."),
        ("🛒 Шипучка Маркет", "https://iniqkpidjosrpflezxnt.supabase.co/...")
    ]

    for name, url in apps:
        markup.add(types.InlineKeyboardButton(text=name, url=url))

    bot.send_message(message.chat.id, "Здравствуйте! Вы в боте от Шипучки.\nВыберите программу:", reply_markup=markup)

if __name__ == "__main__":
    keep_alive() # Запускаем сервер "оживлялку"
    print("Бот запущен!")
    bot.infinity_polling()
