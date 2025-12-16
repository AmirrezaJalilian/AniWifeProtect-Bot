from telegram import Update
from telegram.ext import ContextTypes

from db.user import is_owner, is_admin, set_role
from log.logger import send_log
from log.type import LogTypes


async def add_admin(update: Update, context: ContextTypes.DEFAULT_TYPE, args):
    userid = update.effective_user.id
    try:
        reply = update.effective_message.reply_to_message

        if not is_owner(userid):
            await send_log(context, LogTypes.NOTICE, userid, "Tried To Use .add.admin Command")
            return

        if not reply:
            await update.effective_message.reply_text("Please Reply To A User Message")
            return
        target = reply.from_user
        target_id = target.id
        target_username = target.username

        if is_admin(target_id) is not None:
            await update.effective_message.reply_text("User Already Is Admin")
            return
        set_role(target_id, 'admin')
        await update.effective_message.reply_text(f"Admin Added - ID: <code>{target_id}</code>", parse_mode="HTML")
        await send_log(context, LogTypes.INFO, userid, f"New Admin {target_id} - {target_username}")
    except Exception as e:
        await send_log(context, LogTypes.ERROR, userid, f"Error in add_admin: {e}")


async def remove_admin(update: Update, context: ContextTypes, args):
    user_id = update.effective_user.id
    try:
        reply = update.effective_message.reply_to_message
        if not is_owner(user_id):
            await send_log(context, LogTypes.NOTICE, user_id, "Tried To Use .remove.admin Command")
            return

        if not reply:
            await update.effective_message.reply_text("Please Reply To An User")
            return

        target = reply.from_user
        target_id = target.id
        target_username = target.username

        if is_admin(target_id) is None:
            await update.effective_message.reply_text("User Is Not Admin")
            return
        set_role(target_id)
        await update.effective_message.reply_text(f"Admin Removed - ID: <code>{target_id}</code>", parse_mode="HTML")
        await send_log(context, LogTypes.INFO, user_id, f"Removed Admin {target_id} - {target_username}")
    except Exception as e:
        await send_log(context, LogTypes.ERROR, user_id, f"Error in remove_admin: {e}")
