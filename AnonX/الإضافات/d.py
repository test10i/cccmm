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
    fgj = random.choice(txtf)
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1068724d97569bb1a4a35.jpg",
        caption=f"""
[- Welcome to Source M I X .](https://t.me/DEV_MIX)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        ". Dev Source .", url=f"https://t.me/P_T_I"),
                ],[
                    InlineKeyboardButton(
                        ". Dev Source .", url=f"https://t.me/DEV_MIX"),
                ],
            ]
        ),
    )




