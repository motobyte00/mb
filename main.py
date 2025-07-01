import os
import telebot
from flask import Flask
import threading

# 🔐 Secure token from environment variable
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I'm MB Bot. I'm 24x7 active 🔥")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, f"You said: {message.text}")

# 🧠 Bot running thread
def run_bot():
    bot.polling()

threading.Thread(target=run_bot).start()

# 🌐 Flask web server to keep Render Web Service alive
app = Flask(__name__)

@app.route('/')
def home():
    return "MB Bot is running! ✅"

# Start Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
