# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

import motor.motor_asyncio
from info import *

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
db = client.captions_with_chnl
chnl_ids = db.chnl_ids
users = db.users
banned_users = db.banned_users
bot_admins = db.bot_admins

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

async def addCap(chnl_id, caption):
    dets = {"chnl_id": chnl_id, "caption": caption}
    await chnl_ids.insert_one(dets)

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

async def updateCap(chnl_id, caption):
    await chnl_ids.update_one({"chnl_id": chnl_id}, {"$set": {"caption": caption}})

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

async def insert(user_id):
    user_det = {"_id": user_id}
    try:
        await users.insert_one(user_det)
    except:
        pass

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

async def total_user():
    user = await users.count_documents({})
    return user

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

async def getid():
    all_users = users.find({})
    return all_users

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

async def delete(id):
    await users.delete_one(id)

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

async def addRemWords(chnl_id, words):
    await chnl_ids.update_one(
        {"chnl_id": chnl_id},
        {"$addToSet": {"rem_words": {"$each": words}}},
        upsert=True)

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

async def getRemWords(chnl_id):
    data = await chnl_ids.find_one({"chnl_id": chnl_id})
    return data.get("rem_words", []) if data else []

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #

async def get_replacements(chnl_id):
    data = await chnl_ids.find_one({"chnl_id": chnl_id})
    return data.get("replacements", []) if data else []

# ------------------------ #
# Don't Remove My Credits
# Owner: @Mr_Mohammed_29
# Updates: @Aero_Unity 
# Support : @Coders_Grp 
# ------------------------ #