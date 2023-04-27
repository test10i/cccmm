import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message
from AnonX import app

@app.on_message(command(["الرابط","/link"]) & ~filters.bot & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("قم برفعي مسؤول في المجموعة أولا ؟")
    await message.reply_text(f"**تم إنشاء رابط الدعوة بنجاح :**\n {invitelink}")

 @app.on_message(
    command(["سورس", "ياسورس", "يا سورس", "السورس", "ميكس"])
    & ~filters.edited
)
async def ahmed(client: Client, message: Message):
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


@app.on_message(
    command(["المطور", "مطور البوت", "مطور السورس", "مبرمج السورس", "ميكس"])
    & ~filters.edited
)
async def madison(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/585bf8e7e61498fbc857b.jpg",
        caption=f"""
• Developer bot .
---------------------------

• Dev Name : [مڪس م فايق .](https://t.me/P_T_I)
• Dev User : @P_T_I .
• Dev Bio : - I'm in the lead : @W_4_M - @C_5_N .
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مڪس م فايق .", url=f"https://t.me/P_T_I"),
                ],[
                    InlineKeyboardButton(
                        "• Source Mix .", url=f"https://t.me/W_4_M"),
                ],
            ]
        ),
    )


   
