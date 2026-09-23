# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

from pyrogram import Client
from info import *


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

class Bot(Client):

    def __init__(self):

        super().__init__(
            name="Auto Cap",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={
                "root": "mohammed"
            },
            sleep_threshold=15,
        )


# ------------------------ #
# START BOT
# ------------------------ #

    async def start(self):

        print("🔌 Loading Telegram Bot...")

        await super().start()

        print("✅ Telegram Client Started")

        me = await self.get_me()

        print(f"🤖 Bot: @{me.username}")
        print(f"🆔 Bot ID: {me.id}")

        self.force_channel = FORCE_SUB

        # ------------------------ #
        # FORCE SUB CHANNEL
        # ------------------------ #

        if FORCE_SUB:

            try:

                link = await self.export_chat_invite_link(
                    FORCE_SUB
                )

                self.invitelink = link

                print(
                    f"✅ Force Subscribe Enabled: {FORCE_SUB}"
                )

            except Exception as e:

                print(
                    f"❌ Force Subscribe Error: {e}"
                )

                print(
                    "⚠️ Make sure the bot is administrator "
                    "in the force-sub channel."
                )

                self.force_channel = None

        else:

            print("ℹ️ Force Subscribe Disabled")

        # ------------------------ #
        # START MESSAGE
        # ------------------------ #

        print(
            f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️"
        )

        try:

            await self.send_message(
                ADMIN,
                f"**{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️**"
            )

        except Exception as e:

            print(
                f"⚠️ Could not send startup message: {e}"
            )


# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates : @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #