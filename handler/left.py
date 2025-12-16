from telegram import Update
from telegram.ext import ContextTypes

from log.logger import send_log
from log.type import LogTypes
from db.user import remove_user


async def left_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if message is None or message.left_chat_member is None:
        return

    if message:
        await message.delete()
    else:
        pass

    member = message.left_chat_member
    userid = member.id
    username = member.username

    if username:
        remove_user(username)

    await send_log(context, LogTypes.NOTICE, "Group", f"Left User {userid} - {username}")

    await message.chat.send_message(
        f"💀 <b>{member.full_name}</b> is officially dead…\n"
        "They have left the arena. Rest in peace 🕊️",
        parse_mode="HTML"
    )
