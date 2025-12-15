from telegram import Update
from telegram.ext import ContextTypes
from func import is_owner_or_admin_or_moderator
from Logger import send_notice, send_info


async def pin(update: Update, context: ContextTypes.DEFAULT_TYPE, message_id=None):

    if message_id is not None:
        await update.effective_chat.pin_message(message_id)
        await send_info(update, context, "Bot", f"pinned message: {message_id}")
        return

    reply = update.effective_message.reply_to_message
    userid = update.effective_user.id

    if not is_owner_or_admin_or_moderator(userid):
        await send_notice(update, context, userid, "Tried To Use Command .pin")
        return

    if not reply:
        await update.effective_message.reply_text('Reply To Message')
        return

    message_id = reply.id
    await update.effective_chat.pin_message(message_id)
    await send_info(update, context, userid, f"pinned message: {message_id}")


async def unpin(update: Update, context: ContextTypes.DEFAULT_TYPE, message_id):

    if message_id is not None:
        await update.effective_chat.pin_message(message_id)
        await send_info(update, context, "Bot", f"unpinned message: {message_id}")
        return

    reply = update.effective_message.reply_to_message
    userid = update.effective_user.id

    if not is_owner_or_admin_or_moderator(userid):
        await send_notice(update, context, userid, "Tried To Use Command .unpin")
        return

    if not reply:
        await update.effective_message.reply_text('Reply To Message')
        return

    message_id = reply.id
    await update.effective_chat.pin_message(message_id)
    await send_info(update, context, userid, f"unpinned message: {message_id}")
