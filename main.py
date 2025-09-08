import os
import yt_dlp
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

8381158775:AAF86MUO6XmUwmOMhpiMcwaN4AFpoVm4CT8

def start(update, context):
    update.message.reply_text("🎶 Привет! Я бот @Vanixswgbot. Напиши название песни — я попробую найти её для тебя!")

def search_music(update, context):
    query = update.message.text
    update.message.reply_text(f"🔍 Ищу: {query}...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)
            filename = ydl.prepare_filename(info['entries'][0]).replace(".webm", ".mp3")

        with open(filename, 'rb') as f:
            update.message.reply_audio(f)

    except Exception as e:
        update.message.reply_text(f"⚠️ Ошибка: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_music))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
