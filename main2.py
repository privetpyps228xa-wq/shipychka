import telebot
from telebot import types
import os
from flask import Flask
from threading import Thread

# --- БЛОК ДЛЯ ХОСТИНГА (ЧТОБЫ НЕ ЗАСЫПАЛ) ---
app = Flask('')

@app.route('/')
def home():
    return "Шипучка Бот Жив!"

def run():
    # Render автоматически назначает порт, Flask его подхватит
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- ОСНОВНОЙ КОД БОТА ---

# ЗАМЕНИ НА СВОЙ НОВЫЙ ТОКЕН!
TOKEN = "ТВОЙ_НОВЫЙ_ТОКЕН" 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # Полный список твоих программ
    apps = [
        ("🐱 Поймай ы", "https://iniqkpidjosrpflezxnt.supabase.co/storage/v1/object/sign/apks/_________v1.0.0_1777688055252.apk?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9jM2Q4YWIwMC04MmExLTQyYjMtYWY1My05MDU0YzQwZTVlMmQiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJhcGtzL19fX19fX19fX3YxLjAuMF8xNzc3Njg4MDU1MjUyLmFwayIsImlhdCI6MTc3ODgwMjYxMywiZXhwIjoxODEwMzM4NjEzfQ.1VdyufSCTU83ZtF59E7C3x9cAx4ZMWxPiiLQtHCnfmQ"),
        ("🐱 Поймай ы в2", "https://iniqkpidjosrpflezxnt.supabase.co/storage/v1/object/sign/apks/__________2_v1.0.0_1777686894451.apk?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9jM2Q4YWIwMC04MmExLTQyYjMtYWY1My05MDU0YzQwZTVlMmQiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJhcGtzL19fX19fX19fX18yX3YxLjAuMF8xNzc3Njg2ODk0NDUxLmFwayIsImlhdCI6MTc3ODgwMjY0NCwiZXhwIjoxODEwMzM4NjQ0fQ.2N5Bok7_oRdhfZ2tgu8Yu-PbZEShr-vYXB3SWegZMLc"),
        ("💬 Шипучка Чат", "https://iniqkpidjosrpflezxnt.supabase.co/storage/v1/object/sign/apks/____________v2.0.0_1777715881158.apk?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9jM2Q4YWIwMC04MmExLTQyYjMtYWY1My05MDU0YzQwZTVlMmQiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJhcGtzL19fX19fX19fX19fX3YyLjAuMF8xNzc3NzE1ODgxMTU4LmFwayIsImlhdCI6MTc3ODgwMjY5OCwiZXhwIjoxODEwMzM4Njk4fQ.gF3ijYlqm49rzLNkeZGoOLxxRamhLY31-CbN8T3y68Y"),
        ("🚀 Star Warrior", "https://iniqkpidjosrpflezxnt.supabase.co/storage/v1/object/sign/apks/star%20warrior.apk?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9jM2Q4YWIwMC04MmExLTQyYjMtYWY1My05MDU0YzQwZTVlMmQiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJhcGtzL3N0YXIgd2Fycmlvci5hcGsiLCJpYXQiOjE3Nzg4MDI3MTUsImV4cCI6MTgxMDMzODcxNX0.H4AviLb6Xotj07piPFJtnfuxrmhkPXE4GRfWJzyBMJE"),
        ("📱 Шипучка Грамм", "https://iniqkpidjosrpflezxnt.supabase.co/storage/v1/object/sign/apks/shipychkagram.apk?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9jM2Q4YWIwMC04MmExLTQyYjMtYWY1My05MDU0YzQwZTVlMmQiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJhcGtzL3NoaXB5Y2hrYWdyYW0uYXBrIiwiaWF0IjoxNzc4ODAyNzM1LCJleHAiOjE4MTAzMzg3MzV9.0_2cwHpBaAQL-zxVlSRaGXmj2tCroHg5xDV5-pDg6yE"),
        ("🔢 Шипучка Калькулятор", "https://iniqkpidjosrpflezxnt.supabase.co/storage/v1/object/sign/apks/shipychka%20calculator.apk?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9jM2Q4YWIwMC04MmExLTQyYjMtYWY1My05MDU0YzQwZTVlMmQiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJhcGtzL3NoaXB5Y2hrYSBjYWxjdWxhdG9yLmFwayIsImlhdCI6MTc3ODgwMjc2MiwiZXhwIjoxODEwMzM4NzYyfQ.6BhKYwHPzrEQRzKifsRyr6M7cmijG3S1m-_PvXWvJwg"),
        ("🐶 Mopsogram", "https://iniqkpidjosrpflezxnt.supabase.co/storage/v1/object/sign/apks/mopsogram.apk?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9jM2Q4YWIwMC04MmExLTQyYjMtYWY1My05MDU0YzQwZTVlMmQiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJhcGtzL21vcHNvZ3JhbS5hcGsiLCJpYXQiOjE3Nzg4MDI3ODcsImV4cCI6MTgxMDMzODc4N30.h84oLxkKLznfTOVJcx2CMEL6PsO2mHxiWAKYLE6MiAE"),
        ("🛒 Шипучка Маркет", "https://iniqkpidjosrpflezxnt.supabase.co/storage/v1/object/sign/apks/base.apk?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9jM2Q4YWIwMC04MmExLTQyYjMtYWY1My05MDU0YzQwZTVlMmQiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJhcGtzL2Jhc2UuYXBrIiwiaWF0IjoxNzc4ODAyODMzLCJleHAiOjE4MTAzMzg4MzN9.HhpBRmx7u_uQXhga0VdDPYQ7Qm4GIME0qRakK3KFbTk"),
        ("🕹️ Neon Diver", "https://iniqkpidjosrpflezxnt.supabase.co/storage/v1/object/sign/apks/app-release.apk?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV9jM2Q4YWIwMC04MmExLTQyYjMtYWY1My05MDU0YzQwZTVlMmQiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJhcGtzL2FwcC1yZWxlYXNlLmFwayIsImlhdCI6MTc3ODgwMjg2NCwiZXhwIjoxNzc4ODAyODY0fQ.wJgvQ4C_KHhd8YWcilAiKH51_hueYWGvdtYThKiwtoU")
    ]

    for name, url in apps:
        markup.add(types.InlineKeyboardButton(text=name, url=url))

    bot.send_message(
        message.chat.id, 
        "Здравствуйте! Вы в боте от Шипучки.\nВыберите программу, которую хотите скачать:", 
        reply_markup=markup
    )

if __name__ == "__main__":
    keep_alive() # Запуск веб-сервера
    print("Бот Шипучки запущен и готов к работе!")
    bot.infinity_polling()

