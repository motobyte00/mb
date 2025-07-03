import telebot
from datetime import datetime
from gtts import gTTS
import os

# ✅ Telegram Bot Token (use environment variable for security)
import os
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# ✅ Generate Dummy Titles (optional future use)
def generate_titles(topic):
    topic = topic.title()
    return [
        f"{topic} – Full Review & Features Explained!",
        f"Why {topic} Is Creating Buzz in 2024!",
        f"Top 5 Reasons to Consider {topic} – Must Watch!"
    ]

# ✅ Generate Voice-over in Hindi (for future real use)
def generate_voice(text, filename='voice.mp3'):
    tts = gTTS(text=text, lang='hi', slow=False)
    tts.save(filename)
    return filename

# ✅ Processing Message
def send_processing_message(chat_id):
    bot.send_message(chat_id, "⏳ Processing your request... Please wait 30–60 seconds...")

# ✅ Message Handler (Super Smart Handler)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_msg = message.text.lower()
    chat_id = message.chat.id

    if "video chahiye" in user_msg:
        send_processing_message(chat_id)

        # Split multiple requests by "aur" or "and"
        requests = user_msg.replace(" and ", " aur ").split("aur")
        for req in requests:
            req = req.strip()

            # Extract topic
            words = req.split("pe") if "pe" in req else req.split("on")
            topic = words[1].split("chahiye")[0].strip().title() if len(words) > 1 else "Your Topic"

            # Extract duration
            if "second" in req:
                duration = req.split("second")[0].split()[-1]
                duration_type = "seconds"
            elif "min" in req or "minute" in req:
                duration = req.split("min")[0].split()[-1]
                duration_type = "minutes"
            else:
                duration = "1"
                duration_type = "minute"

            # Detect Features (super smart detection)
            want_voice = "voice" in req or "voice-over" in req or "vlog" in req
            want_music = "background sound" in req or "music" in req
            want_thumb = "thumbnail" in req or "photo" in req or "image" in req

            msg = f"✅ Video for *{topic}* ({duration} {duration_type}) is ready!\n"
            if want_music:
                msg += "🎵 Background sound added\n"
            if want_voice:
                msg += "🎙️ Voice-over added with vlog-style explanation\n"
            if want_thumb:
                msg += "🖼️ Thumbnail created\n"

            msg += "\n📅 Files generation is simulated. Full video support coming soon."

            bot.send_message(chat_id, msg, parse_mode="Markdown")

    else:
        bot.send_message(chat_id, """
👋 MB Bot ready hai. Tum mujhe normal message mein bolo jaise:

• "Mujhe Tata Safari pe 3 min ka video chahiye with background sound, vlog-style voice-over, and thumbnail."
• "Mujhe bike review ka video chahiye voice-over aur music ke sath"
        """, parse_mode="Markdown")

# ✅ Start polling
bot.polling()
