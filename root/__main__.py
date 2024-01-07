from root import *
from pyrogram import *
import os
import sys
import io
from root import bot
from root import *
import asyncio

print("Getting Ready")
print("[INFO] PyFly Started")
print("[INFO] Running Until Disconnected")

@bot.on_message(filters.command("start"))
async def PyFly(_, message):
    getting_ready = await bot.send_message(message.chat.id, "Starting PyFly..")
    await asyncio.sleep(2)
    await getting_ready.edit("PyFly Has Stated")

@bot.on_message(filters.command(['run', 'bash', 'sh', 'shell']))
async def PyFly(_, message):
    try:
        Run_Txt = await message.reply_text("`....`")
        await asyncio.sleep(2.5) #Server Maintenance
        await Run_Txt.edit("???")
    except Exception as e:
        await message.reply_text(f"**Error**: {e}")

bot.run()
print("[INFO] PyFly Has Stoped")
exit()
