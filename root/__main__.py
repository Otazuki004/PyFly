from root import *
from pyrogram import *
import os
import sys
import io
from ACCESS import rootsys, rootuser, admin, data


bot.start()
print("Getting Ready")
print("[INFO] PyFly Started")
print("[INFO] Running Until Disconnected")

@bot.on_message(filters.command("start"))
async def PyFly(_, message):
    getting_ready = await bot.send_message(message.chat.id, "Starting PyFly..")
    
@bot.on_message(filters.command(['run', 'bash', 'sh', 'shell']))
async def PyFly(_, message):
    try:
        Run_Txt = await message.reply_text("`....`")
    except Exception as e:
        await message.reply_text(f"**Error**: {e}")
