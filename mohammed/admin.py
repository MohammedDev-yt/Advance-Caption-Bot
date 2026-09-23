# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

from pyrogram import Client, filters
from pyrogram.types import Message
from info import OWNER_ID
from .database import bot_admins

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

# ------------------------ #
# Get User ID
# ------------------------ #

def get_user_id(message: Message):

    # If command is used by replying to a user
    if message.reply_to_message:

        if message.reply_to_message.from_user:
            return message.reply_to_message.from_user.id

    # If command contains USER_ID
    if len(message.command) > 1:

        try:
            return int(message.command[1])

        except (ValueError, TypeError):
            return None

    return None

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

# ------------------------ #
# ADD ADMIN
# OWNER ONLY
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.command("addadmin") &
    filters.user(OWNER_ID)
)
async def add_admin(client, message):

    user_id = get_user_id(message)

    if not user_id:

        return await message.reply_text(
            "<b>❌ Iɴᴠᴀʟɪᴅ Usᴀɢᴇ</b>\n\n"
            "<code>/addadmin USER_ID</code>\n\n"
            "Oʀ reply to a user's message with "
            "<code>/addadmin</code>."
        )

    user_id = int(user_id)

    # Owner doesn't need to be added as admin
    if user_id == int(OWNER_ID):

        return await message.reply_text(
            "ℹ️ <b>Tʜɪs Uꜱᴇʀ Is Aʟʀᴇᴀᴅʏ Tʜᴇ Oᴡɴᴇʀ.</b>"
        )

    await bot_admins.update_one(
        {"_id": user_id},
        {
            "$set": {
                "user_id": user_id
            }
        },
        upsert=True
    )

    await message.reply_text(
        "👑 <b>Aᴅᴍɪɴ Aᴅᴅᴇᴅ Sᴜᴄᴄᴇꜱꜱғᴜʟʟʏ</b>\n\n"
        f"👤 Uꜱᴇʀ ID: <code>{user_id}</code>"
    )

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

# ------------------------ #
# REMOVE ADMIN
# OWNER ONLY
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.command("removeadmin") &
    filters.user(OWNER_ID)
)
async def remove_admin(client, message):

    user_id = get_user_id(message)

    if not user_id:

        return await message.reply_text(
            "<b>❌ Iɴᴠᴀʟɪᴅ Usᴀɢᴇ</b>\n\n"
            "<code>/removeadmin USER_ID</code>"
        )

    user_id = int(user_id)

    # Owner cannot be removed
    if user_id == int(OWNER_ID):

        return await message.reply_text(
            "❌ <b>Yᴏᴜ Cᴀɴɴᴏᴛ Rᴇᴍᴏᴠᴇ Tʜᴇ Oᴡɴᴇʀ.</b>"
        )

    result = await bot_admins.delete_one(
        {"_id": user_id}
    )

    if result.deleted_count == 0:

        return await message.reply_text(
            "ℹ️ <b>Tʜɪs Uꜱᴇʀ Is Nᴏᴛ Aɴ Aᴅᴍɪɴ.</b>"
        )

    await message.reply_text(
        "✅ <b>Aᴅᴍɪɴ Rᴇᴍᴏᴠᴇᴅ Sᴜᴄᴄᴇꜱꜱғᴜʟʟʏ</b>\n\n"
        f"👤 Uꜱᴇʀ ID: <code>{user_id}</code>"
    )

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

# ------------------------ #
# ADMIN LIST
# OWNER ONLY
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.command("adminlist") &
    filters.user(OWNER_ID)
)
async def admin_list(client, message):

    admins = []

    async for admin in bot_admins.find({}):

        user_id = admin.get("_id")

        if user_id:
            admins.append(user_id)

    text = "<b>👑 Bᴏᴛ Aᴅᴍɪɴs</b>\n\n"

    # Always show owner
    text += (
        f"1. Oᴡɴᴇʀ — "
        f"<code>{OWNER_ID}</code>\n"
    )

    number = 2

    for user_id in admins:

        text += (
            f"{number}. "
            f"<code>{user_id}</code>\n"
        )

        number += 1

    text += (
        f"\n<b>Tᴏᴛᴀʟ Aᴅᴍɪɴs:</b> "
        f"{len(admins) + 1}"
    )

    await message.reply_text(text)

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #