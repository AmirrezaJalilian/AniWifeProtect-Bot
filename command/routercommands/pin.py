from telegram import Update
from telegram.ext import ContextTypes

from db.user import is_staff
from log.logger import send_log
from log.type import LogTypes


async def pin(update: Update, context: ContextTypes.DEFAULT_TYPE, args):

    reply = update.effective_message.reply_to_message
    userid = update.effective_user.id

    if not is_staff(userid):
        return

    if not reply:
        await update.effective_message.reply_text('Reply To Message')
        return

    message_id = reply.id
    await update.effective_chat.pin_message(message_id)
    await update.effective_message.reply_text(
        "Pinned Message",
        reply_to_message_id=message_id
    )
    await send_log(context, LogTypes.INFO, "Group", f"New Pin Message: {message_id}")


async def unpin(update: Update, context: ContextTypes.DEFAULT_TYPE, args):

    reply = update.effective_message.reply_to_message
    userid = update.effective_user.id

    if not is_staff(userid):
        return

    if not reply:
        await update.effective_message.reply_text('Reply To Message')
        return

    message_id = reply.id
    await update.effective_chat.unpin_message(message_id)
    await update.effective_message.reply_text(
        "UnPinned Message",
        reply_to_message_id=message_id
    )
    await send_log(context, LogTypes.INFO, "Group", f"New UnPin Message: {message_id}")
