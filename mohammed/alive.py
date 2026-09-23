# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

import time

from pyrogram import Client, filters
from info import MOHAMMED_PIC


# ------------------------ #
# ALIVE COMMAND
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.command("alive")
)
async def alive_command(client, message):

    start_time = time.perf_counter()

    try:

        # Send image instead of sticker
        alive_msg = await message.reply_photo(
            photo=MOHAMMED_PIC,
            caption=(
                "<b>✨ Aᴜ Cᴀᴘᴛɪᴏɴ Bᴏᴛ Iꜱ Aʟɪᴠᴇ ✨</b>\n\n"
                "╭──────────────────╮\n"
                "│ ⚡ <b>Sᴛᴀᴛᴜs:</b> Oɴʟɪɴᴇ\n"
                "│ 🤖 <b>Bᴏᴛ:</b> Aᴜᴛᴏ Cᴀᴘᴛɪᴏɴ\n"
                "╰──────────────────╯"
            )
        )

        ping = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        await alive_msg.edit_caption(
            caption=(
                "<b>✨ Aᴜ Cᴀᴘᴛɪᴏɴ Bᴏᴛ Iꜱ Aʟɪᴠᴇ ✨</b>\n\n"
                "╭──────────────────╮\n"
                "│ ⚡ <b>Sᴛᴀᴛᴜs:</b> Oɴʟɪɴᴇ\n"
                f"│ 🏓 <b>Pɪɴɢ:</b> <code>{ping} ms</code>\n"
                "│ 🤖 <b>Bᴏᴛ:</b> Aᴜᴛᴏ Cᴀᴘᴛɪᴏɴ\n"
                "╰──────────────────╯\n\n"
                "<b>🚀 Bᴏᴛ Iꜱ Wᴏʀᴋɪɴɢ Pᴇʀғᴇᴄᴛʟʏ!</b>"
            )
        )

    except Exception as e:

        print(
            f"Alive image error: {e}"
        )

        await message.reply_text(
            f"❌ <b>Aʟɪᴠᴇ Cʜᴇᴄᴋ Fᴀɪʟᴇᴅ</b>\n\n"
            f"<code>{e}</code>"
        )


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #