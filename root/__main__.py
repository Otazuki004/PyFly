from root import *
from pyrogram import *
import os
import sys
import io

bot.start()
print("Getting Ready")
print("[INFO] PyFly Started")
print("[INFO] Running Until Disconnected")

@bot.on_message(filters.command("start"))
async def PyFly(_, message):
    getting_ready = await bot.send_message(message.chat.id, "Starting PyFly..")
    
