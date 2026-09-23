# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

import time

from pyrogram import Client, filters


ALIVE_STICKER = "CgACAgQAAxkBAAIOpmqwBoY0C00jo6t2rIxYpUICEqeTAAItCgACvoykUDAPxxyDdh_CHgQ"


# ------------------------ #
# ALIVE
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.command("alive")
)
async def alive_command(client, message):

    start_time = time.perf_counter()

    try:
        await message.reply_animation(
            animation=ALIVE_STICKER
        )

    except Exception as e:
        print(f"Alive animation error: {e}")

    ping = round(
        (time.perf_counter() - start_time) * 1000,
        2
    )

    await message.reply_text(
        "<b>╭━━━━━━━━━━━━━━━━━━╮\n"
        "      🤖 Bᴏᴛ Is Aʟɪᴠᴇ!\n"
        "╰━━━━━━━━━━━━━━━━━━╯</b>\n\n"
        f"⚡ <b>Pɪɴɢ:</b> <code>{ping} ms</code>\n"
        "🟢 <b>Sᴛᴀᴛᴜs:</b> Oɴʟɪɴᴇ\n"
        "🚀 <b>Sᴇʀᴠᴇʀ:</b> Rᴜɴɴɪɴɢ\n\n"
        "<b>Yᴏᴜ ᴀʀᴇ ᴠᴇʀʏ ʟᴜᴄᴋʏ 🤞 "
        "I ᴀᴍ ᴀʟɪᴠᴇ ❤️\n\n"
        "Pʀᴇss /start ᴛᴏ ᴜsᴇ ᴍᴇ</b>"
    )


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #