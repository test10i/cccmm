
import asyncio

import os
import config
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint
@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/7031365c0ba236dd7ef28.jpg",
        caption=f""". 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗦𝗼𝘂𝗿𝗰𝗲 𝗠𝗶𝘅 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ꪑꪗ ᦔꫀꪜ", url=f"https://t.me/P_T_I"), 
                
                    InlineKeyboardButton(
                        "ᧁ𝘳ꪮꪊρ ᥴ𝘳", url=f"https://t.me/C_5_N"),
                ],[
                    InlineKeyboardButton(
                        "⌞ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗠𝗶𝘅 ⌝", url=f"https://t.me/C_5_N"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption=". تـم اختيـار الاغـنـية لـك -",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



