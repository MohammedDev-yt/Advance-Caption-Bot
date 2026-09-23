# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

from pyrogram import Client, filters
from pyrogram.types import Message
from info import OWNER_ID
from .database import banned_users

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
# BAN USER
# OWNER ONLY
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.command("ban") &
    filters.user(OWNER_ID)
)
async def ban_user(client, message):

    user_id = get_user_id(message)

    if not user_id:

        return await message.reply_text(
            "<b>❌ Iɴᴠᴀʟɪᴅ Usᴀɢᴇ</b>\n\n"
            "<code>/ban USER_ID</code>\n\n"
            "Oʀ reply to a user's message with "
            "<code>/ban</code>."
        )

    user_id = int(user_id)

    # Owner cannot be banned
    if user_id == int(OWNER_ID):

        return await message.reply_text(
            "❌ <b>Yᴏᴜ Cᴀɴɴᴏᴛ Bᴀɴ Tʜᴇ Oᴡɴᴇʀ.</b>"
        )

    # Add user to banned collection
    await banned_users.update_one(
        {"_id": user_id},
        {
            "$set": {
                "user_id": user_id
            }
        },
        upsert=True
    )

    await message.reply_text(
        "🚫 <b>Uꜱᴇʀ Bᴀɴɴᴇᴅ Sᴜᴄᴄᴇꜱꜱғᴜʟʟʏ</b>\n\n"
        f"👤 Uꜱᴇʀ ID: <code>{user_id}</code>"
    )

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

# ------------------------ #
# UNBAN USER
# OWNER ONLY
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.command("unban") &
    filters.user(OWNER_ID)
)
async def unban_user(client, message):

    user_id = get_user_id(message)

    if not user_id:

        return await message.reply_text(
            "<b>❌ Iɴᴠᴀʟɪᴅ Usᴀɢᴇ</b>\n\n"
            "<code>/unban USER_ID</code>\n\n"
            "Oʀ reply to a user's message with "
            "<code>/unban</code>."
        )

    user_id = int(user_id)

    result = await banned_users.delete_one(
        {"_id": user_id}
    )

    if result.deleted_count == 0:

        return await message.reply_text(
            "ℹ️ <b>Tʜɪs Uꜱᴇʀ Is Nᴏᴛ Bᴀɴɴᴇᴅ.</b>"
        )

    await message.reply_text(
        "✅ <b>Uꜱᴇʀ Uɴʙᴀɴɴᴇᴅ Sᴜᴄᴄᴇꜱꜱғᴜʟʟʏ</b>\n\n"
        f"👤 Uꜱᴇʀ ID: <code>{user_id}</code>"
    )

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

# ------------------------ #
# BAN LIST
# OWNER ONLY
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.command("banlist") &
    filters.user(OWNER_ID)
)
async def ban_list(client, message):

    users = []

    async for user in banned_users.find({}):

        user_id = user.get("_id")

        if user_id:
            users.append(user_id)

    if not users:

        return await message.reply_text(
            "✅ <b>Bᴀɴ Lɪsᴛ Is Eᴍᴘᴛʏ.</b>"
        )

    text = "<b>🚫 Bᴀɴɴᴇᴅ Uꜱᴇʀs</b>\n\n"

    for index, user_id in enumerate(users, 1):

        text += (
            f"{index}. "
            f"<code>{user_id}</code>\n"
        )

    text += (
        f"\n<b>Tᴏᴛᴀʟ Bᴀɴɴᴇᴅ:</b> "
        f"{len(users)}"
    )

    await message.reply_text(text)


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #