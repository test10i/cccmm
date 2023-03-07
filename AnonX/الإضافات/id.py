from pyrogram import Client , filters
from pyrogram.enums import ChatMemberStatus
PyroHub = Client("PyroHub - Pyrogram",
api_id=
api_hash=""
bot_token="")

@PyroHub.on_message(filters.regex("^ايدي$"))
async def myid(_,message):
   user = await message.chat.get_member(message.from_user.id)
   if user.status == ChatMemberStatus.OWNER:
      status = "المالك"
   elif user.status == ChatMemberStatus.ADMINISTRATOR:
      status = "المشرف"
   elif user.status == ChatMemberStatus.MEMBER:
      status = "العضو"
   a = await PyroHub.get_chat(message.from_user.id)
   usr = await PyroHub.get_chat(message.from_user.id)
   name = message.from_user.mention
   if message.from_user.username == None:
         user = "لايوجد"
   else:
         user = message.from_user.username
   id = message.from_user.id
   bio = a.bio
   caption = "اسمك : {}\nمعرفك : @{}\nايديك : `{}`\nرتبتك : {}\n- {}"
   if a.photo:
      async for photo in PyroHub.get_chat_photos(message.from_user.id, limit=1):
         await message.reply_photo(
            photo.file_id,
            caption=caption.format(name,user,id,status,bio)
         )
   else:
      await message.reply(caption.format(name,user,id,status,bio))
 
@PyroHub.on_message(filters.regex("^ايديه$"))
async def herid(_, message):
   user = await message.chat.get_member(message.reply_to_message.from_user.id)
   if user.status == ChatMemberStatus.OWNER:
      status = "المالك"
   elif user.status == ChatMemberStatus.ADMINISTRATOR:
      status = "المشرف"
   elif user.status == ChatMemberStatus.MEMBER:
      status = "العضو"
   a = await PyroHub.get_chat(message.reply_to_message.from_user.id)
   usr = await PyroHub.get_chat(message.from_user.id)
   name = message.reply_to_message.from_user.first_name
   if message.from_user.username == None:
         user = "لايوجد"
   else:
         user = message.reply_to_message.from_user.username
         id = message.reply_to_message.from_user.id
   bio = a.bio
   caption = "اسمه : {}\nمعرفه : @{}\nايديه : `{}`\nرتبته : {}\n- {}"
   if a.photo:
      async for photo in PyroHub.get_chat_photos(message.reply_to_message.from_user.id, limit=1):
         await message.reply_photo(
            photo.file_id,
            caption=caption.format(name,user,id,status,bio)
         )
   else:
      await message.reply(caption.format(name,user,id,status,bio))
            
print ("- Done Upload Telegram Bot .\n- Can You Used Bot Now!")
PyroHub.run()
