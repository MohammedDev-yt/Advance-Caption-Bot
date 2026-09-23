# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

import asyncio
import threading
import traceback

from flask import Flask

from bot import Bot


app = Flask(__name__)


# ------------------------ #
# HOME
# ------------------------ #

@app.route("/")
def hello_world():
    return "ᴍᴏʜᴀᴍᴍᴇᴅ ᴅᴇᴠᴇʟᴏᴘᴇʀ"


# ------------------------ #
# START TELEGRAM BOT
# ------------------------ #

def start_bot():

    try:

        print("🚀 Starting Telegram Bot...")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        bot = Bot()

        print("🔌 Telegram Bot Instance Created")

        loop.run_until_complete(bot.start())

        print("✅ Telegram Bot Started Successfully")
        print("📡 Waiting for Telegram Updates...")

        loop.run_forever()

    except Exception as e:

        print(f"❌ Telegram Bot Error: {e}")

        traceback.print_exc()


# ------------------------ #
# RUN BOT IN BACKGROUND
# ------------------------ #

bot_thread = threading.Thread(
    target=start_bot,
    daemon=True,
    name="TelegramBotThread"
)

bot_thread.start()


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #