from telegram import Update
from telegram.ext import ContextTypes

from db.user import add_user
from log.logger import send_log
from log.type import LogTypes


async def join_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message

    if message is None:
        return

    if message:
        await message.delete()
    else:
        pass

    for member in message.new_chat_members:

        userid = member.id
        username = member.username

        add_user(userid, username)

        await send_log(context, LogTypes.NOTICE, "Group", f"New User {userid} - {username}")

        await message.chat.send_message(
            f"🎉 <b>Welcome {member.mention_html()}!</b>\n"
            "You have entered the battlefield\n"
            "May your stay be legendary!",
            parse_mode="HTML"
        )
