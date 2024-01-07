from pyrogram import Client

a_id = "10187126" # Your Api Id
a_hash = "ff197c0d23d7fe54c89b44ed092c1752" # Your Api Hash 
b_tok = "6957348263:AAH7yp5PMl1pIHhtxRuMbOvnK9FwvKshOuk" # Your Bot Token

SUDO = [5965055071]

bot = Client("PyFly", bot_token=b_tok, api_id=a_id, api_hash=a_hash, plugins=dict(root="root/Properties"))
