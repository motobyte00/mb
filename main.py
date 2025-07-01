import telebot

bot = telebot.TeleBot("7749636877:AAEC-6LJNgyDk776bhLsmW7d2pQT1VfQh28")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello! I'm your MB Bot, ready to serve.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "You said: " + message.text)

bot.polling()
