import telebot
from telebot import types
from datetime import datetime
import random

# ✅ Telegram Bot Token
BOT_TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(BOT_TOKEN)

# ✅ Utility: Generate Dummy Titles
def generate_titles(topic):
    topic = topic.title()
    return [
        f"{topic} – Full Review & Features Explained!",
        f"Why {topic} Is Creating Buzz in 2024!",
        f"Top 5 Reasons to Consider {topic} – Must Watch!"
    ]

# ✅ Utility: Send Loading Message
def send_processing_message(chat_id):
    bot.send_message(chat_id, "⏳ Processing your request...\nPlease wait 30–60 seconds...")

# ✅ Message Handler
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_msg = message.text.lower()
    chat_id = message.chat.id

    # Trigger words
    if "video chahiye" in user_msg:
        send_processing_message(chat_id)

        # Extract topic
        words = user_msg.split("pe") if "pe" in user_msg else user_msg.split("on")
        topic = words[1].split("chahiye")[0].strip().title() if len(words) > 1 else "Your Topic"

        # Extract duration
        if "second" in user_msg:
            duration = user_msg.split("second")[0].split()[-1]
            duration_type = "seconds"
        elif "min" in user_msg or "minute" in user_msg:
            duration = user_msg.split("min")[0].split()[-1]
            duration_type = "minutes"
        else:
            duration = "1"
            duration_type = "minute"

        # Check extras
        want_voice = "voice" in user_msg or "voice-over" in user_msg
        want_music = "music" in user_msg
        want_thumb = "thumbnail" in user_msg
        want_titles = "title" in user_msg or "3 titles" in user_msg

        # Generate Fake Output
        msg = f"✅ Video for *{topic}* ({duration} {duration_type}) is ready!\n"
        if want_voice:
            msg += "🎙️ Voice-over added\n"
        if want_music:
            msg += "🎧 Background music included\n"
        if want_thumb:
            msg += "🖼️ Thumbnail created\n"
        if want_titles:
            titles = generate_titles(topic)
            msg += "\n🏷️ *Suggested Titles:*\n"
            for t in titles:
                msg += f"• {t}\n"

        msg += "\n📥 All files are being prepared. You will get downloadable links soon."

        bot.send_message(chat_id, msg, parse_mode="Markdown")

    elif "thumbnail" in user_msg:
        bot.send_message(chat_id, "🖼️ Thumbnail is being generated... (future AI integration here)")

    elif "titles" in user_msg or "title" in user_msg:
        bot.send_message(chat_id, "🏷️ Send me the topic, I'll give you 3 catchy YouTube titles.")

    elif "help" in user_msg:
        bot.send_message(chat_id, """
🤖 *MB Bot Help Menu*:
Just send messages like:

• "Mujhe Tata Safari pe 2 min ka video chahiye with voice + music + thumbnail + titles"
• "Thumbnail dedo"
• "3 video titles chahiye iPhone 16 Pro pe"
        """, parse_mode="Markdown")

    else:
        bot.send_message(chat_id, "👋 Hi! MB Bot ready hai. Message me likho kya banana hai, jaise:\n'Mujhe 1 min ka video chahiye Tata Curvv pe with voice'")

# ✅ Start polling
bot.polling()
