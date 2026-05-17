import os
import sys

# Пробуем импортировать библиотеки и запустить сервер
try:
    import telebot
    from openai import OpenAI
    from threading import Thread
    from flask import Flask

    app = Flask('')

    @app.route('/')
    def home():
        return "НейроХам живой!"

    def run_web_server():
        port = int(os.environ.get("PORT", 8080))
        app.run(host='0.0.0.0', port=port)

    # Проверяем, передал ли Render ключи
    TELEGRAM_TOKEN = os.getenv('8847569761:AAHpePATl8IZmthR4wtswzWO4K3cBYPzCFY')
    OPENROUTER_API_KEY = os.getenv('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')

    if not TELEGRAM_TOKEN or not OPENROUTER_API_KEY:
        print("КРИТИЧЕСКАЯ ОШИБКА: Забыл добавить TELEGRAM_TOKEN или OPENROUTER_API_KEY в Environment Variables на Render!")
        sys.exit(1)

    bot = telebot.TeleBot(TELEGRAM_TOKEN)
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )

    @bot.message_handler(func=lambda message: True)
    def handle_ai_chat(message):
        try:
            response = client.chat.completions.create(
                model="meta-llama/llama-3-8b-instruct:free",
                messages=[{"role": "user", "content": message.text}]
            )
            bot.reply_to(message, response.choices[0].message.content)
        except Exception as e:
            bot.reply_to(message, f"Ошибка ИИ: {e}")

    if __name__ == "__main__":
        t = Thread(target=run_web_server)
        t.start()
        print("Бот-невидимка успешно стартовал...")
        bot.polling(none_stop=True)

except Exception as main_error:
    print(f"СКРИПТ УПАЛ ПРИ СТАРТЕ: {main_error}")
    sys.exit(1)
