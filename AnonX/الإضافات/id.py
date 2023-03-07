import re
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus

PyroHub = Client("PyroHub - Pyrogram",
api_id=5019636942, 
api_hash="3bb0fb9e679abb72dfa0c2e1ae7d1b5f", 
bot_token="5906747194:AAH3QE3b_R0GUwQUZ6Pmx3EPOiD_-StbuEo")

#Commands in *Tag .
@PyroHub.on_message(filters.regex("^حظر .*$") & filters.group)
async def ban(_, message):
    User = re.match("حظر @(.*)", message.text).group(1)
    stas = (await PyroHub.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth:
    	await message.chat.ban_member(User)
    	await message.reply_text("- تم حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
@PyroHub.on_message(filters.regex("^الغاء حظر .*$") & filters.group)
async def unban(_, message):
    User = re.match("الغاء حظر @(.*)", message.text).group(1)
    stas = (await PyroHub.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth:
    	await message.chat.unban_member(User)
    	await message.reply_text("- تم الغاء حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
#Commands in *reply .
@PyroHub.on_message(filters.regex("^حظر$") & filters.group)
async def ban2(_, message):
    user =message.reply_to_message.from_user.id
    stas = (await PyroHub.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth:
    	await PyroHub.ban_chat_member(message.chat.id,user)
    	await message.reply_text("- تم حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
@PyroHub.on_message(filters.regex("^الغاء حظر$") & filters.group)
async def ban3(_, message):
    user =message.reply_to_message.from_user.id
    stas = (await PyroHub.get_chat_member(message.chat.id, message.from_user.id)).status
    auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
    if stas in auth:
    	await PyroHub.unban_chat_member(message.chat.id,user)
    	await message.reply_text("- تم الغاء حظره من المجموعة .")
    else:
            await message.reply("- هذا الأمر يخص مشرفين المجموعة .")
            
print ("- Done Upload Telegram Bot .\n- Can You Used Bot Now!")
PyroHub.run()
