# ✅ MB Bot Full Smart Code (main.py)
# Handles: Video request (simulated), Voice generation (Hindi-English), Thumbnail, Titles

import telebot
from telebot import types
from datetime import datetime
from gtts import gTTS
import os

# ✅ Telegram Bot Token
BOT_TOKEN = "7749636877:AAEC-6LJNgyDk776bhLsmW7d2pQT1VfQh28"
bot = telebot.TeleBot(BOT_TOKEN)

# ✅ Generate Dummy Titles
def generate_titles(topic):
    topic = topic.title()
    return [
        f"{topic} – Full Review & Features Explained!",
        f"Why {topic} Is Creating Buzz in 2024!",
        f"Top 5 Reasons to Consider {topic} – Must Watch!"
    ]

# ✅ Generate Voice-over in Hindi-English
def generate_voice(text, filename='voice.mp3'):
    tts = gTTS(text=text, lang='hi', slow=False)
    tts.save(filename)
    return filename

# ✅ Processing Message
def send_processing_message(chat_id):
    bot.send_message(chat_id, "⏳ Processing your request... Please wait 30–60 seconds...")

# ✅ Message Handler
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_msg = message.text.lower()
    chat_id = message.chat.id

    # Trigger: Video Request
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

        want_voice = "voice" in user_msg or "voice-over" in user_msg
        want_music = "music" in user_msg
        want_thumb = "thumbnail" in user_msg
        want_titles = "title" in user_msg or "3 titles" in user_msg

        msg = f"✅ Video for *{topic}* ({duration} {duration_type}) is ready!\n"
        if want_voice:
            script = f"Yeh hai {topic}, jisme milta hai advanced design, modern features aur zabardast performance."
            voice_file = generate_voice(script)
            with open(voice_file, 'rb') as audio:
                bot.send_audio(chat_id, audio)
            msg += "🎙️ Voice-over added\n"
            os.remove(voice_file)
        if want_music:
            msg += "🎵 Background music included\n"
        if want_thumb:
            msg += "🖼️ Thumbnail created\n"
        if want_titles:
            titles = generate_titles(topic)
            msg += "\n🏷️ *Suggested Titles:*\n"
            for t in titles:
                msg += f"\u2022 {t}\n"

        msg += "\n📅 Files generation is simulated. Full video support coming soon."
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
        bot.send_message(chat_id, "👋 MB Bot ready hai. Likho: 'mujhe [topic] pe [duration] ka video chahiye voice/music/thumbnail ke sath'")

# ✅ Start polling
bot.polling()
