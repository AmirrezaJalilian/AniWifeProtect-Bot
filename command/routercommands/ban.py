from telegram import Update
from telegram.ext import ContextTypes
from db.user import add_ban, remove_ban, get_bans, is_staff
from log.logger import send_log
from log.type import LogTypes


async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE, args):
    user_id = update.effective_user.id

    if not is_staff(user_id):
        return

    reply = update.effective_message.reply_to_message

    if not reply:
        await update.effective_message.reply_text("Please Reply To An User.")
        return

    target = reply.from_user
    target_id = target.id
    target_username = target.username

    chat = update.effective_chat

    await chat.ban_member(target_id)
    add_ban(target_id)
    await update.effective_message.reply_text(f"User <code>{target_id}</code> Banned!")
    await send_log(context, LogTypes.INFO, "Group", f"Banned User {target_id} - {target_username}")


async def unban(update: Update, context: ContextTypes.DEFAULT_TYPE, args):
    user_id = update.effective_user.id

    if not await is_staff(user_id):
        return
    reply = update.effective_message.reply_to_message

    if not reply:
        await update.effective_message.reply_text("Please Reply To An User.")
        return

    target = reply.from_user
    target_id = target.id
    target_username = target.username

    chat = update.effective_chat

    await chat.unban_member(target_id)
    remove_ban(target_id)
    await update.effective_message.reply_text(f"User <code>{target_id}</code> UnBanned!")
    await send_log(context, LogTypes.INFO, "Group", f"UnBanned User {user_id} - {target_username}")


async def list_ban(update: Update, context: ContextTypes.DEFAULT_TYPE, args):
    user_id = update.effective_user.id

    if not await is_staff(user_id):
        return

    bans = get_bans()

    if not bans:
        await update.effective_message.reply_text("No Baned Users.")
        return

    text = f"List Bans From Bot: \nCount: {len(bans)}\n\n"

    limit = min(10, len(bans))

    for i, ban in enumerate(bans, start=1):
        if i > limit:
            break
        text += f"{i} - User: <code>{ban}</code>\n"

    if len(bans) > 10:
        text += "..."

    await update.effective_message.reply_text(text)
