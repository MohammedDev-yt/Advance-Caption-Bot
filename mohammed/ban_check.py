# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

from pyrogram import Client, filters
from pyrogram.enums import ChatType
from info import OWNER_ID
from .database import banned_users

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

# ------------------------ #
# Check Banned User
# ------------------------ #

async def is_banned(user_id):

    if not user_id:
        return False

    if int(user_id) == int(OWNER_ID):
        return False

    user = await banned_users.find_one(
        {"_id": int(user_id)}
    )

    return user is not None

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

# ------------------------ #
# BLOCK BANNED USERS
# ------------------------ #

@Client.on_message(
    filters.private
)
async def check_banned_user(client, message):

    if not message.from_user:
        return

    if await is_banned(message.from_user.id):

        try:
            await message.delete()
        except Exception:
            pass

        return


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #