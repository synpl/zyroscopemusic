from .ping import uptime as tedeuptime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>┗┓ Hi {message.from_user.first_name} My Name is {BOT_NAME} ┏┛\n
Saya Bot Music Group, Yang dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah
Saya Memiliki Banyak Fitur Praktis Seperti:
┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Lagu.
┣• Mencari Lagu Yang ingin di Putar atau di Download.
┗━━━━━━━━━━━━━━
Ketik » /help « Untuk Melihat Daftar Perintah!
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan Ke Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                         "🤖 Assistant", url=f"https://t.me/{ASSISTANT_NAME}"
                    ),
                    InlineKeyboardButton(
                        "🛠 Repo", url="https://github.com/tofikdn/TDMusicBot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(command(["start", "start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_text(
        f"""I'm online!\n<b>Up since:</b> {tedeuptime}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Repo", url="https://github.com/tofikdn/TDMusicBot"
                    ),
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/tedesupport"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play (judul lagu) - Untuk Memutar lagu yang Anda minta melalui YouTube
/playlist - Untuk Menampilkan daftar putar Lagu sekarang
/current - Untuk Menunjukkan  Lagu sekarang yang sedang diputar
/song (judul lagu) - Untuk Mendownload lagu dari YouTube 
/search (judul video) - Untuk Mencari Video di YouTube dengan detail
/video (judul video) - Untuk Mendownload Video di YouTube dengan detail
\n**Admins Only:**
/player - Open music player settings panel
/pause - Untuk Menjeda pemutaran Lagu
/resume - Untuk Melanjutkan pemutaran Lagu yang di pause
/skip - Untuk Menskip pemutaran lagu ke Lagu berikutnya
/end - Untuk Memberhentikan pemutaran Lagu
/userbotjoin - Untuk Mengundang asisten ke obrolan Anda
/reload - Untuk Merefresh admin list
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/tedesupport"
                    ),
                    InlineKeyboardButton(
                        "Tede", url="https://t.me/tdtapibot"
                    )
                ]
            ]
        )
    )
