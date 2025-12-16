from telegram import Update, ChatPermissions
from telegram.ext import ContextTypes
from log.logger import send_log
from log.type import LogTypes
from db.user import is_mute, add_mute, is_staff, remove_mute, get_mutes


async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE, args):
    user_id = update.effective_user.id

    if not await is_staff(user_id):
        return
    reply = update.effective_message.reply_to_message

    if not reply:
        await update.effective_message.reply_text(f"Please Reply To An User")
        return

    target = reply.from_user

    target_id = target.id
    target_username = target.username

    if is_mute(target_id):
        await update.effective_message.reply_text(f"User {target_id} Already Is Mute")
        return

    await update.effective_chat.restrict_member(target_id, permissions=ChatPermissions(can_send_messages=False))
    add_mute(target_id)
    await update.effective_message.reply_text(f"User {target_id} Muted")
    await send_log(context, LogTypes.INFO, user_id, f"New Muted User {target_id} - {target_username}")


async def unmute(update: Update, context: ContextTypes.DEFAULT_TYPE, args):
    user_id = update.effective_user.id

    if not await is_staff(user_id):
        return
    reply = update.effective_message.reply_to_message

    if not reply:
        await update.effective_message.reply_text(f"Please Reply To An User")
        return

    target = reply.from_user

    target_id = target.id
    target_username = target.username

    if not is_mute(target_id):
        await update.effective_message.reply_text(f"User {target_id} Is Not Mute")
        return

    await update.effective_chat.restrict_member(target_id, permissions=ChatPermissions(
        can_send_polls=True,
        can_send_audios=True,
        can_send_photos=True,
        can_send_videos=True,
        can_send_documents=True,
        can_send_messages=True,
        can_send_video_notes=True,
        can_send_other_messages=True
    ))
    remove_mute(target_id)
    await update.effective_message.reply_text(f"User {target_id} UnMuted")
    await send_log(context, LogTypes.INFO, user_id, f"New UnMuted User {target_id} - {target_username}")


async def list_mute(update: Update, context: ContextTypes.DEFAULT_TYPE, args):
    user_id = update.effective_user.id

    if not await is_staff(user_id):
        return
    bans = get_mutes()

    if not bans:
        await update.effective_message.reply_text("No Muted Users.")
        return

    ban_count = len(bans)
    text = f"List Mutes From Bot: \nCount: {ban_count}\n\n"

    limit = min(10, len(bans))

    for i, ban in enumerate(bans, start=1):
        if i > limit:
            break
        text += f"{i} - User: {ban}\n"

    if len(bans) > 10:
        text += "..."

    await update.effective_message.reply_text(text)
