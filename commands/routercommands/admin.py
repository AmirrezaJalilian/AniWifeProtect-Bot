from dbmanagers.staff import add_admin, remove_admin, admin


async def add_admin_(update, context, args):
    try:
        if args:
            target_id = int(args[0])
        else:
            reply = update.effective_message.reply_to_message
            if not reply:
                await update.effective_message.reply_text("Please Reply Ot Provide ID")
                return
            target_id = reply.from_user.id
        
        if admin(target_id) is not None:
            await update.effective_message.reply_text("User Already Is Admin")
            return
        add_admin(target_id)
        await update.effective_message.reply_text(f"Admin Added - ID: `{target_id}`", parse_mode="Markdown")
    except ValueError:
        await update.effective_message.reply_text("Invalid ID Format")
    except Exception as e:
        print(f"Error in add_admin_: {e}")

async def remove_admin_(update, context, args):
    try:
        if args:
            target_id = int(args[0])
        else:
            reply = update.effective_message.reply_to_message
            if not reply:
                await update.effective_message.reply_text("Please Reply Ot Provide ID")
                return
            target_id = reply.from_user.id
        if admin(target_id) is None:
            await update.effective_message.reply_text("User Is Not Admin")
            return
        remove_admin(target_id)
        await update.effective_message.reply_text(f"Admin Removed - ID: `{target_id}`", parse_mode="Markdown")
        
    except ValueError:
        await update.effective_message.reply_text("Invalid ID Format")
    except Exception as e:
        print(f"Error in remove_admin_: {e}")