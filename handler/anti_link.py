import re

from telegram import Update
from telegram.ext import ContextTypes

from db.user import is_staff, get_users_username
from bot_config import LINK_REGEX
from log.logger import send_log
from log.type import LogTypes


async def anti_link(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message

    if not message:
        return

    if is_staff(update.effective_user.id):
        return

    text = message.text or ""
    matches = re.findall(LINK_REGEX, text)
    found_usernames = [u1 or u2 for u1, u2 in matches]

    if not found_usernames:
        return

    chat = message.chat

    for username in found_usernames:
        if username in get_users_username():
            continue

        try:
            await message.delete()
        except Exception as e:
            await send_log(
                context,
                LogTypes.ERROR,
                "Bot",
                f"DELETE ERROR: {e}"
            )

        try:
            await send_log(
                context,
                LogTypes.WARN,
                update.effective_user.id,
                f"Anti-Link: {text}"
            )
        except Exception as e:
            await send_log(context, LogTypes.ERROR, "Bot", f"SEND_WARN ERROR: {e}")

        try:
            await chat.send_message(
                f"Heyyyyy!!! <b>{message.from_user.mention_html()}</b>\n"
                f"Links are forbidden here!\n"
                f"Please don’t summon forbidden portals again",
                parse_mode="HTML"
            )
        except Exception as e:
            await send_log(context, LogTypes.ERROR, "Bot", f"MAIN GROUP SEND ERROR: {e}")

        return
