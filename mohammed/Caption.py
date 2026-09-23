# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

import asyncio
import os
import re
import sys

from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from info import *
from .database import (
    insert,
    total_user,
    getid,
    delete,
    addCap,
    updateCap,
    chnl_ids,
    addRemWords,
    getRemWords,
    get_replacements,
)


# ------------------------ #
# TEXTS
# ------------------------ #

START_TXT = """
<b>Hᴇʟʟᴏ {}</b>

I ᴀᴍ Aᴜᴛᴏ Cᴀᴘᴛɪᴏɴ Bᴏᴛ Wɪᴛʜ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.

Pʀᴇss Tʜᴇ Hᴇʟᴘ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Uꜱᴇ Mᴇ.
"""

HELP_TXT = """
<b>📚 Hᴏᴡ Tᴏ Uꜱᴇ Mᴇ</b>

<b>Channel Commands:</b>

<code>/set_cap Your Caption</code>
➜ Set a custom caption.

<code>/del_cap</code>
➜ Delete your custom caption.

<code>/rem_words word1 word2</code>
➜ Remove words from file names.

<code>/del_words word1 word2</code>
➜ Add words to remove from file names.

<code>/del_rem_words</code>
➜ Delete all remove words.

<code>/replace_word old new</code>
➜ Replace words in file names.

<code>/replace_words old new</code>
➜ Replace words in file names.

<code>/del_replace_words</code>
➜ Delete all replacement words.

<b>Admin Commands:</b>

<code>/total_users</code>
➜ Show total users.

<code>/broadcast</code>
➜ Broadcast a replied message.

<code>/restart</code>
➜ Restart the bot.
"""

ABOUT_TXT = """
<b>✨ Aʙᴏᴜᴛ Mᴇ</b>

I ᴀᴍ Aᴜᴛᴏ Cᴀᴘᴛɪᴏɴ Bᴏᴛ.

I Cᴀɴ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Aᴅᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴs Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Fɪʟᴇs.

<b>Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ:</b>
<a href="https://t.me/Mr_Mohammed_29">Mᴏʜᴀᴍᴍᴇᴅ</a>
"""


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #


# ------------------------ #
# START COMMAND
# ------------------------ #

@Client.on_message(
    filters.command("start") &
    filters.private
)
async def strtCap(client, message):

    user_id = int(message.from_user.id)

    await insert(user_id)

    # ------------------------ #
    # START ANIMATION
    # ------------------------ #

    try:

        m = await message.reply_text(
            "Sʜᴀᴅᴏᴡ Oғ Mᴏɴᴀʀᴄʜ. . ."
        )

        await asyncio.sleep(0.5)

        await m.edit_text("⚡️")

        await asyncio.sleep(0.5)

        await m.edit_text("🐈‍⬛️")

        await asyncio.sleep(0.5)

        await m.edit_text(
            "Yᴏʀᴜɪᴄʜɪ Sʜɪʜōɪɴ ✨"
        )

        await asyncio.sleep(0.5)

        await m.delete()

    except Exception as e:

        print(
            f"Start animation error: {e}"
        )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️",
                    url="https://t.me/AU_Caption_bot?startchannel=true"
                )
            ],
            [
                InlineKeyboardButton(
                    "• Hᴇʟᴘ •",
                    callback_data="help"
                ),
                InlineKeyboardButton(
                    "• Aʙᴏᴜᴛ •",
                    callback_data="about"
                )
            ],
            [
                InlineKeyboardButton(
                    "• Uᴘᴅᴀᴛᴇ •",
                    url="https://t.me/Aero_Unity"
                ),
                InlineKeyboardButton(
                    "• Sᴜᴘᴘᴏʀᴛ •",
                    url="https://t.me/Coders_Grp"
                )
            ]
        ]
    )

    await message.reply_photo(
        photo=MOHAMMED_PIC,

        caption=(
            f"<b>Hᴇʟʟᴏ {message.from_user.mention}\n\n"
            f"ɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n\n"
            f"Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴄʟɪᴄᴋ ᴏɴ "
            f"ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.\n\n"
            f"Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ » "
            f"<a href='https://t.me/Mr_Mohammed_29'>ᴍᴏʜᴀᴍᴍᴇᴅ</a></b>"
        ),

        reply_markup=keyboard
    )


# ------------------------ #
# TOTAL USERS
# OWNER/ADMIN
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.user(ADMIN) &
    filters.command("total_users")
)
async def all_db_users_here(client, message):

    mohammed = await message.reply_text(
        "Pʟᴇᴀsᴇ Wᴀɪᴛ...."
    )

    mohammed_botz = await total_user()

    await mohammed.edit(
        f"Tᴏᴛᴀʟ Usᴇʀs :- `{mohammed_botz}`"
    )


# ------------------------ #
# BROADCAST
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.user(ADMIN) &
    filters.command("broadcast")
)
async def broadcast(client, message):

    if not message.reply_to_message:

        return await message.reply_text(
            "Rᴇᴘʟʏ Tᴏ A Mᴇssᴀɢᴇ Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ."
        )

    status = await message.reply_text(
        "Gᴇᴛᴛɪɴɢ Aʟʟ Usᴇʀ IDs Fʀᴏᴍ Dᴀᴛᴀʙᴀsᴇ...\n\n"
        "Pʟᴇᴀsᴇ Wᴀɪᴛ..."
    )

    all_users = await getid()

    tot = await total_user()

    success = 0
    failed = 0
    deactivated = 0
    blocked = 0

    async for user in all_users:

        user_id = user.get("_id")

        try:

            await message.reply_to_message.copy(
                user_id
            )

            success += 1

            await asyncio.sleep(0.05)

        except FloodWait as e:

            await asyncio.sleep(
                e.value
            )

            try:

                await message.reply_to_message.copy(
                    user_id
                )

                success += 1

            except Exception:

                failed += 1

        except Exception as e:

            error_name = type(e).__name__

            if error_name == "InputUserDeactivated":

                deactivated += 1

                await delete(
                    {"_id": user_id}
                )

            elif error_name == "UserIsBlocked":

                blocked += 1

                await delete(
                    {"_id": user_id}
                )

            else:

                failed += 1

    await status.edit(
        "<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u>\n\n"
        f"• Tᴏᴛᴀʟ Usᴇʀs: {tot}\n"
        f"• Sᴜᴄᴄᴇssғᴜʟ: {success}\n"
        f"• Bʟᴏᴄᴋᴇᴅ Usᴇʀs: {blocked}\n"
        f"• Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ: {deactivated}\n"
        f"• Fᴀɪʟᴇᴅ: {failed}"
    )


# ------------------------ #
# RESTART
# ------------------------ #

@Client.on_message(
    filters.private &
    filters.user(ADMIN) &
    filters.command("restart")
)
async def restart_bot(client, message):

    mohammed = await message.reply_text(
        "**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. "
        "𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**"
    )

    await asyncio.sleep(3)

    await mohammed.edit(
        "**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. "
        "𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**"
    )

    os.execl(
        sys.executable,
        sys.executable,
        *sys.argv
    )


# ------------------------ #
# SET CAPTION
# CHANNEL
# ------------------------ #

@Client.on_message(
    filters.command("set_cap") &
    filters.channel
)
async def setCap(client, message):

    if len(message.command) < 2:

        return await message.reply(
            "Usᴀɢᴇ:\n\n"
            "<code>/set_cap Your Caption</code>\n\n"
            "Use <code>{file_name}</code> "
            "to show file name.\n\n"
            "Use <code>{file_size}</code> "
            "to show file size.\n\n"
            "Use <code>{default_caption}</code> "
            "to show original caption.\n\n"
            "Use <code>{language}</code> "
            "to show language.\n\n"
            "Use <code>{year}</code> "
            "to show year.\n\n"
            "Use <code>{duration}</code> "
            "to show duration.\n\n"
            "Use <code>{height}</code> "
            "to show video height.\n\n"
            "Use <code>{width}</code> "
            "to show video width."
        )

    chnl_id = message.chat.id

    caption = message.text.split(
        " ",
        1
    )[1].strip()

    chkData = await chnl_ids.find_one(
        {"chnl_id": chnl_id}
    )

    if chkData:

        await updateCap(
            chnl_id,
            caption
        )

    else:

        await addCap(
            chnl_id,
            caption
        )

    await message.reply(
        f"Yᴏᴜʀ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Is:\n\n{caption}"
    )


# ------------------------ #
# REPLACE WORD
# ------------------------ #

@Client.on_message(
    filters.command(
        ["replace_word", "replace_words"]
    ) &
    filters.channel
)
async def replace_word(client, message):

    if len(message.command) < 2:

        return await message.reply(
            "Usage:\n"
            "<code>/replace_word old new</code>\n\n"
            "or\n\n"
            "<code>/replace_words old new</code>\n\n"
            "Multiple pairs:\n"
            "<code>/replace_word old new, old2 new2</code>"
        )

    chnl_id = message.chat.id

    replacements = message.text.split(
        " ",
        1
    )[1]

    replacement_list = []

    for replacement_pair in replacements.split(","):

        parts = replacement_pair.strip().split()

        if len(parts) < 2:
            continue

        original_word = parts[0]

        replacement_word = " ".join(
            parts[1:]
        )

        replacement_list.append(
            {
                "original": original_word,
                "replacement": replacement_word
            }
        )

    if not replacement_list:

        return await message.reply(
            "❌ Nᴏ Vᴀʟɪᴅ Rᴇᴘʟᴀᴄᴇᴍᴇɴᴛ Fᴏᴜɴᴅ."
        )

    await chnl_ids.update_one(
        {"chnl_id": chnl_id},
        {
            "$push": {
                "replacements": {
                    "$each": replacement_list
                }
            }
        },
        upsert=True
    )

    await message.reply(
        "**ʀᴇᴘʟᴀᴄᴇᴍᴇɴᴛ ᴡᴏʀᴅs ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.** ✅"
    )


# ------------------------ #
# DELETE REPLACE WORDS
# ------------------------ #

@Client.on_message(
    filters.command("del_replace_words") &
    filters.channel
)
async def del_replace_words(client, message):

    chnl_id = message.chat.id

    channel_data = await chnl_ids.find_one(
        {"chnl_id": chnl_id}
    )

    if channel_data and "replacements" in channel_data:

        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {
                "$unset": {
                    "replacements": ""
                }
            }
        )

        await message.reply(
            "**ᴀʟʟ ʀᴇᴘʟᴀᴄᴇᴍᴇɴᴛ ᴡᴏʀᴅs "
            "ʜᴀᴠᴇ ʙᴇᴇɴ ᴅᴇʟᴇᴛᴇᴅ.**"
        )

    else:

        await message.reply(
            "**ɴᴏ ʀᴇᴘʟᴀᴄᴇᴍᴇɴᴛ ᴡᴏʀᴅs ғᴏᴜɴᴅ.**"
        )


# ------------------------ #
# ADD REMOVE WORDS
# ------------------------ #

@Client.on_message(
    filters.command(
        ["rem_words", "del_words"]
    ) &
    filters.channel
)
async def setRemWords(client, message):

    if len(message.command) < 2:

        return await message.reply(
            "Usage:\n"
            "<code>/rem_words word1 word2 word3</code>\n\n"
            "or\n\n"
            "<code>/del_words word1 word2 word3</code>"
        )

    chnl_id = message.chat.id

    words = message.command[1:]

    await addRemWords(
        chnl_id,
        words
    )

    await message.reply(
        f"Added words to remove:\n"
        f"{', '.join(words)}"
    )


# ------------------------ #
# DELETE REMOVE WORDS
# ------------------------ #

@Client.on_message(
    filters.command("del_rem_words") &
    filters.channel
)
async def delRemWords(client, message):

    chnl_id = message.chat.id

    channel_data = await chnl_ids.find_one(
        {"chnl_id": chnl_id}
    )

    if channel_data and "rem_words" in channel_data:

        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {
                "$unset": {
                    "rem_words": ""
                }
            }
        )

        await message.reply(
            "**ᴀʟʟ ʀᴇᴍᴏᴠᴇ ᴡᴏʀᴅs "
            "ʜᴀᴠᴇ ʙᴇᴇɴ ᴅᴇʟᴇᴛᴇᴅ.**"
        )

    else:

        await message.reply(
            "**ɴᴏ ʀᴇᴍᴏᴠᴇ ᴡᴏʀᴅs ғᴏᴜɴᴅ.**"
        )


# ------------------------ #
# DELETE CAPTION
# ------------------------ #

@Client.on_message(
    filters.command("del_cap") &
    filters.channel
)
async def delCap(client, message):

    chnl_id = message.chat.id

    try:

        # Only remove the custom caption.
        # Do NOT delete the complete channel document,
        # otherwise remove_words and replacements are also lost.

        result = await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {
                "$unset": {
                    "caption": ""
                }
            }
        )

        if result.modified_count:

            return await message.reply(
                "<b><i>✓ Sᴜᴄᴄᴇssғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ "
                "Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ.\n\n"
                "Nᴏᴡ I Aᴍ Usɪɴɢ Mʏ Dᴇғᴀᴜʟᴛ Cᴀᴘᴛɪᴏɴ.</i></b>"
            )

        return await message.reply(
            "❌ Nᴏ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ Fᴏᴜɴᴅ."
        )

    except Exception as e:

        error_message = await message.reply(
            f"ERR I GOT: <code>{e}</code>"
        )

        await asyncio.sleep(5)

        try:
            await error_message.delete()
        except Exception:
            pass


# ------------------------ #
# LANGUAGE
# ------------------------ #

def extract_language(default_caption):

    if not default_caption:

        return "Hindi-English"

    language_pattern = (
        r"\b(Hindi|English|Tamil|Telugu|Malayalam|"
        r"Kannada|Hin)\b"
    )

    languages = set(
        re.findall(
            language_pattern,
            default_caption,
            re.IGNORECASE
        )
    )

    if not languages:

        return "Hindi-English"

    return ", ".join(
        sorted(
            languages,
            key=str.lower
        )
    )


# ------------------------ #
# YEAR
# ------------------------ #

def extract_year(default_caption):

    if not default_caption:

        return None

    match = re.search(
        r"\b(19\d{2}|20\d{2})\b",
        default_caption
    )

    return match.group(1) if match else None


# ------------------------ #
# WORD REPLACEMENTS
# ------------------------ #

def apply_word_replacements(
    file_name,
    replacements
):

    for item in replacements:

        original = item.get(
            "original",
            ""
        )

        replacement = item.get(
            "replacement",
            ""
        )

        if not original:
            continue

        file_name = re.sub(
            rf"\b{re.escape(original)}\b",
            replacement,
            file_name,
            flags=re.IGNORECASE
        )

    return file_name


# ------------------------ #
# DURATION
# ------------------------ #

def format_duration(duration):

    if not duration:

        return "N/A"

    hours = duration // 3600

    minutes = (
        duration % 3600
    ) // 60

    seconds = duration % 60

    formatted_duration = ""

    if hours > 0:

        formatted_duration += (
            f"{hours}H-"
        )

    if minutes > 0:

        formatted_duration += (
            f"{minutes}M-"
        )

    formatted_duration += (
        f"{seconds:02}Sec"
    )

    return formatted_duration


# ------------------------ #
# SIZE
# ------------------------ #

def get_size(size):

    units = [
        "Bytes",
        "Kʙ",
        "Mʙ",
        "Gʙ",
        "Tʙ",
        "Pʙ",
        "Eʙ"
    ]

    size = float(size)

    i = 0

    while (
        size >= 1024.0
        and i < len(units) - 1
    ):

        i += 1
        size /= 1024.0

    return "%.2f %s" % (
        size,
        units[i]
    )


# ------------------------ #
# AUTO CAPTION
# ------------------------ #

@Client.on_message(
    filters.channel &
    filters.media
)
async def reCap(client, message):

    chnl_id = message.chat.id

    default_caption = (
        message.caption or ""
    )

    if not message.media:
        return

    file_obj = None

    for file_type in (
        "video",
        "audio",
        "document",
        "voice"
    ):

        obj = getattr(
            message,
            file_type,
            None
        )

        if obj:

            file_obj = obj
            break

    if not file_obj:
        return

    file_name = getattr(
        file_obj,
        "file_name",
        None
    )

    file_size = getattr(
        file_obj,
        "file_size",
        0
    )

    duration = getattr(
        file_obj,
        "duration",
        None
    )

    height = getattr(
        file_obj,
        "height",
        None
    )

    width = getattr(
        file_obj,
        "width",
        None
    )

    if not file_name:

        return

    language = extract_language(
        default_caption
    )

    year = extract_year(
        default_caption
    )

    formatted_duration = format_duration(
        duration
    )

    height = height or "N/A"
    width = width or "N/A"

    file_name = (
        re.sub(
            r"@\w+\s*",
            "",
            file_name
        )
        .replace("_", " ")
        .replace(".", " ")
    )

    # ------------------------ #
    # REPLACEMENTS
    # ------------------------ #

    replacements = await get_replacements(
        chnl_id
    )

    file_name = apply_word_replacements(
        file_name,
        replacements
    )

    # ------------------------ #
    # REMOVE WORDS
    # ------------------------ #

    rem_words = await getRemWords(
        chnl_id
    )

    for word in rem_words:

        file_name = re.sub(
            rf"\b{re.escape(word)}\b",
            "",
            file_name,
            flags=re.IGNORECASE
        )

    file_name = re.sub(
        r"\s+",
        " ",
        file_name
    ).strip()

    # ------------------------ #
    # GET CAPTION
    # ------------------------ #

    cap_dets = await chnl_ids.find_one(
        {"chnl_id": chnl_id}
    )

    try:

        if cap_dets and cap_dets.get(
            "caption"
        ):

            cap = cap_dets["caption"]

        else:

            cap = DEF_CAP

        replaced_caption = cap.format(
            file_name=file_name,
            file_size=get_size(file_size),
            default_caption=default_caption,
            language=language,
            year=year,
            duration=formatted_duration,
            height=height,
            width=width
        )

        await message.edit_caption(
            caption=replaced_caption
        )

    except FloodWait as e:

        await asyncio.sleep(
            e.value
        )

        try:

            await message.edit_caption(
                caption=replaced_caption
            )

        except Exception as retry_error:

            print(
                f"Caption retry error: {retry_error}"
            )

    except Exception as e:

        print(
            f"Caption processing error: {e}"
        )


# ------------------------ #
# START CALLBACK
# ------------------------ #

@Client.on_callback_query(
    filters.regex(r"^start")
)
async def start(client, query):

    await query.answer()

    await query.message.edit_text(

        text=START_TXT.format(
            query.from_user.mention
        ),

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️",
                        url="https://t.me/AU_Caption_bot?startchannel=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• Hᴇʟᴘ •",
                        callback_data="help"
                    ),
                    InlineKeyboardButton(
                        "• Aʙᴏᴜᴛ •",
                        callback_data="about"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• Uᴘᴅᴀᴛᴇ •",
                        url="https://t.me/Aero_Unity"
                    ),
                    InlineKeyboardButton(
                        "• Sᴜᴘᴘᴏʀᴛ •",
                        url="https://t.me/Coders_Grp"
                    )
                ]
            ]
        ),

        disable_web_page_preview=True
    )


# ------------------------ #
# HELP CALLBACK
# ------------------------ #

@Client.on_callback_query(
    filters.regex(r"^help")
)
async def help(client, query):

    await query.answer()

    await query.message.edit_text(

        text=HELP_TXT,

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Aʙᴏᴜᴛ •",
                        callback_data="about"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ʙᴀᴄᴋ •",
                        callback_data="start"
                    )
                ]
            ]
        ),

        disable_web_page_preview=True
    )


# ------------------------ #
# ABOUT CALLBACK
# ------------------------ #

@Client.on_callback_query(
    filters.regex(r"^about")
)
async def about(client, query):

    await query.answer()

    await query.message.edit_text(

        text=ABOUT_TXT,

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʜᴏᴡ ᴛᴏ ᴜsᴇ Mᴇ ❓",
                        callback_data="help"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "• ʙᴀᴄᴋ •",
                        callback_data="start"
                    )
                ]
            ]
        ),

        disable_web_page_preview=True
    )


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #