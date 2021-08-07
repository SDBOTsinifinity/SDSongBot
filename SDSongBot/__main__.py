from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import bot
from SDSongBot import LOGGER

pm_start_text = """
𝗛𝗲𝘆 𝘁𝗵𝗲𝗿𝗲 [{}](tg://user?id={}), 𝗜'𝗺 𝗦𝗼𝗻𝗴 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿 𝗕𝗼𝘁 🎵
𝗗𝗼 /𝗵𝗲𝗹𝗽 𝗳𝗼𝗿 𝗸𝗻𝗼𝘄 𝗮𝗯𝗼𝘂𝘁 𝗺𝗲 𝗮𝗻𝗱 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀!
𝗠𝗮𝗱𝗲 𝗯𝘆 **@SDBOTsZ**
"""

help_text = """
𝗜 𝗰𝗮𝗻 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗛𝗤 𝘀𝗼𝗻𝗴𝘀 𝗳𝗿𝗼𝗺 𝗬𝗼𝘂𝗧𝘂𝗯𝗲 𝗠𝘂𝘀𝗶𝗰.😊
**Syntax** - `/𝘀𝗼𝗻𝗴 [𝘀𝗼𝗻𝗴 𝗻𝗮𝗺𝗲]`
𝗘𝘅𝗮𝗺𝗽𝗹𝗲:- `/𝘀𝗼𝗻𝗴 𝗳𝗮𝗱𝗲𝗱`

𝗠𝗮𝗱𝗲 𝗯𝘆 **@SDBOTsZ**
"""



@bot.on_message(filters.command("start") & ~filters.edited)
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝗨𝗽𝗱𝗮𝘁𝗲𝘀 📧", url="https://t.me/SDBOTs_inifinity"
                    ),
                    InlineKeyboardButton(
                        text="𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗖𝗵𝗮𝘁 📛", url="https://t.me/SDBOTz"
                    )
                ]
            ]
        )
        await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)
    else:
        start_text = "𝗛𝗲𝘆 𝘁𝗵𝗲𝗿𝗲 [{}](tg://user?id={}), 𝗦𝗼𝗻𝗴 𝗗𝗟 𝗕𝗼𝘁 𝗶𝘀 𝗼𝗻𝗹𝗶𝗻𝗲 😊"
        await message.reply(start_text.format(name, user_id))
    
@bot.on_message(filters.command("help") & ~filters.edited)
async def start(client, message):
    await message.reply(help_text)

bot.start()
LOGGER.info("SDSongBot is online.")
idle()
2021 GitHub, Inc.
 

