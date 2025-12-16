import time
import datetime as dt
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from bot_config import bot_run_time
from db.user import add_user, exist_user
from log.logger import send_log
from log.type import LogTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    userid = user.id
    username = user.username

    if not exist_user(userid):
        add_user(userid, username)

    current_time = dt.datetime.now(dt.timezone.utc)

    uptime = await format_uptime(bot_run_time, current_time)

    start_time = time.time()

    msg = await update.effective_message.reply_text('starting...')

    end_time = time.time()

    await msg.delete()

    ping = (end_time - start_time) * 10

    await update.effective_message.reply_photo(
        'https://i.ibb.co/5W9ybvHf/0e4d41090879.jpg',
        f"Hᴇʏ Usᴇʀ {user.mention_html()}, WᴇʟCᴏᴍᴇ ᴛᴏ AɴɪWɪғᴇPʀᴏᴛᴇᴄᴛBᴏᴛ :)\n"
        "——————————‹ ⁌※⁍ ›——————————\n"
        "Tʜɪs ʙᴏᴛ ᴍᴀᴅᴇ ғᴏʀ AɴɪWɪғᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ.\n"
        "ᴏᴡɴᴇʀ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇʀ ɪs ᴀᴍɪʀʀᴇᴢᴀ(@ManamMadara).\n"
        "——————————‹ ⁌※⁍ ›——————————\n"
        f"ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"ᴘɪɴɢ: {ping: .2f}ᴍs",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("◜Mᴀɪɴ Cʜᴀɴɴᴇʟ◞", url='https://t.me/AniWifeHub'),
                InlineKeyboardButton("◜Mᴀɪɴ Gʀᴏᴜᴘ◞", url='https://t.me/+cz54ZrOgKOpjNmZk')
            ]
        ]),
        parse_mode='HTML'
    )

    await send_log(context, LogTypes.INFO, "Bot", f"Start Command {userid} - {username}")


async def format_uptime(start, end):
    delta_uptime = end - start

    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    if days > 0:
        return f"{days}d {hours}h {minutes}m {seconds}s"
    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"
