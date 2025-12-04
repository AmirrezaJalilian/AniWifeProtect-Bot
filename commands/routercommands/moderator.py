from dbmanagers.staff import add_moderator, remove_moderator, moderator


async def add_moderator_(update, context, args):
    try:
        if args:
            target_id = int(args[0])
        else:
            reply = update.effective_message.reply_to_message
            if not reply:
                await update.effective_message.reply_text("Please Reply Ot Provide ID")
                return
            target_id = reply.from_user.id
        
        if moderator(target_id) is not None:
            await update.effective_message.reply_text("User Already Is Moderator")
            return
        add_moderator(target_id)
        await update.effective_message.reply_text(f"Moderator Added - ID: `{target_id}`", parse_mode="Markdown")
    except ValueError:
        await update.effective_message.reply_text("Invalid ID Format")
    except Exception as e:
        print(f"Error in add_moderator_: {e}")

async def remove_moderator_(update, context, args):
    try:
        if args:
            target_id = int(args[0])
        else:
            reply = update.effective_message.reply_to_message
            if not reply:
                await update.effective_message.reply_text("Please Reply Ot Provide ID")
                return
            target_id = reply.from_user.id
        if moderator(target_id) is None:
            await update.effective_message.reply_text("User Is Not Moderator")
            return
        remove_moderator(target_id)
        await update.effective_message.reply_text(f"Moderator Removed - ID: `{target_id}`", parse_mode="Markdown")
        
    except ValueError:
        await update.effective_message.reply_text("Invalid ID Format")
    except Exception as e:
        print(f"Error in remove_moderator_: {e}")