import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SeiraRobot.events import register as MEMEK
from SeiraRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/51c4e8b6b40cd0cb66cea.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Holla I'm Seira!** \n\n"
  LUNA += "ð **I'm Working Properly** \n\n"
  LUNA += "ð **My Master : [ê±á´á´Êâ](https://t.me/xyzsethhh)** \n\n"
  LUNA += f"ð **Telethon Version : {tlhver}** \n\n"
  LUNA += f"ð **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Terima kasih sudah menambahkan Seira ð**"
  BUTTON = [[Button.url("Êá´Êá´", "https://t.me/SeiraXRobot?start=help"), Button.url("sá´á´á´á´Êá´", "https://t.me/seirasupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

