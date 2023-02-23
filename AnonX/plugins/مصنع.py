import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
import random


    

@app.on_message(
    command(["سورس", "ياسورس", "يا سورس", "السورس", "ميكس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1068724d97569bb1a4a35.jpg",
        caption=f"""
[ - 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗦𝗼𝘂𝗿𝗰𝗲 𝗠 𝗜 𝗫 . ](https://t.me/DEV_MIX)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        ". 𝗗𝗲𝘃 𝗦𝗼𝘂𝗿𝗰𝗲 .", url=f"https://t.me/P_T_I"),
                ],[
                    InlineKeyboardButton(
                        ". 𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 .", url=f"https://t.me/DEV_MIX"),
                ],
            ]
        ),
    )




