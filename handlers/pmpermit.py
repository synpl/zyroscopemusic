from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Halo, Saya adalah **Layanan Assistant TD Music Bot.**\n\n ❗️ **Rules:**\n   - Jangan Spam Pesan disini\n   - Jangan Spam Lagu Biar Ga Error \n\n 👉 **KIRIM LINK INVITE ATAU USERNAME GROUP, JIKA ASSISTANT TIDAK DAPAT BERGABUNG DENGAN GROUP ANDA.**\n\n **Owner** @tofik_dn**")
  return                        
