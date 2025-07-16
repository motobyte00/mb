import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

# Token Railway se milega
TOKEN = os.getenv("TOKEN")

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Copyright-free resources
MUSIC_LINKS = [
    "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Komiku/Komiku_-_Its_time_for_adventure/Komiku_-_15_-_Level_Up.mp3",
    "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Monplaisir/Monplaisir_2/Monplaisir_-_06_-_Rainbow.mp3"
]

VIDEO_LINKS = [
    "https://samplelib.com/lib/preview/mp4/sample-5s.mp4",
    "https://samplelib.com/lib/preview/mp4/sample-10s.mp4"
]

SCRIPTS = [
    "📜 Script: Review of top 3 budget-friendly tech gadgets under ₹1500.",
    "📜 Script: Complete overview of the latest 2025 electric bike features."
]

# Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to MB Bot!\nUse /music, /video or /script.")

async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = random.choice(MUSIC_LINKS)
    await update.message.reply_audio(audio=url, title="Free Background Music")

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = random.choice(VIDEO_LINKS)
    await update.message.reply_video(video=url, caption="Downloadable Stock Video")

async def script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = random.choice(SCRIPTS)
    await update.message.reply_text(text)

# Main function
async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("music", music))
    app.add_handler(CommandHandler("video", video))
    app.add_handler(CommandHandler("script", script))
    await app.run_polling()

# Run
if _name_ == "_main_":
    import asyncio
    asyncio.run(main())
