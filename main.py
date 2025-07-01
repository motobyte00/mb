import telebot
from flask import Flask
import threading

# Telegram bot
bot = telebot.TeleBot("7749636877:AAEC-6LJNgyDk776bhLsmW7d2pQT1VfQh28")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! I'm your MB Bot, now running 24x7 via Web Service.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "You said: " + message.text)

# Run bot in a separate thread
def run_bot():
    bot.polling()

threading.Thread(target=run_bot).start()

# Dummy web server for Render
app = Flask(__name__)

@app.route('/')
def home():
    return "MB Bot is running!"

# Keep Flask app alive
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
