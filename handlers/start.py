from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>┗┓ Haii {message.from_user.first_name} My Name is TD Music Bot ┏┛\n
Saya Bot Music Group, Yang dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah
Saya Memiliki Banyak Fitur Praktis Seperti :
┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Lagu.
┣• Mencari Lagu Yang ingin di Putar atau di Download.
┗━━━━━━━━━━━━━━
❃ Managed With ☕️ By : [Tofik Denianto](https://t.me/tofik_dn)
━━━━━━━━━━━━━━━
Ingin Menambahkan Saya ke Group Anda? Tambahkan Saya Ke Group Anda!
</b>""",

        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan Ke Group ➕", url="https://t.me/tofikdnbot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                         "📷 Instagram", url="https://www.instagram.com/tofik_dn"
                    ),
                    InlineKeyboardButton(
                        "💾 Project Man", url="https://t.me/Lunatic0de"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Tidak ", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <nama lagu>  - Untuk Memutar lagu yang Anda minta melalui youtube
/dplay <nama lagu>  - Untuk Memutar lagu yang Anda minta melalui deezer
/splay <nama lagu>  - Untuk Memutar lagu yang Anda minta melalui jio saavn
/playlist - Untuk Menampilkan daftar putar Lagu sekarang
/current - Untuk Menunjukkan  Lagu sekarang yang sedang diputar
/song <nama lagu> - Untuk Mendownload lagu dari YouTube 
/search <nama lagu> - Untuk Mencari Video di YouTube dengan detail
/deezer <nama lagu> - Untuk Mendownload lagu dari deezer 
/saavn <nama lagu> - Untuk Mendownload lagu dari website saavn
/video <nama lagu> - Untuk Mendownload Video di YouTube dengan detail
\n*Admins only*
/player - Open music player settings panel
/pause - Untuk Menjeda pemutaran Lagu
/resume - Untuk Melanjutkan pemutaran Lagu yang di pause
/skip - Untuk Menskip pemutaran lagu ke Lagu berikutnya
/end - Untuk Memberhentikan pemutaran Lagu
/userbotjoin - Untuk Mengundang asisten ke obrolan Anda
/admincache - Untuk Merefresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/tofik_dn"
                    ),
                    InlineKeyboardButton(
                        "Project Man", url="https://t.me/Lunatic0de"
                    )
                ]
            ]
        )
    )
