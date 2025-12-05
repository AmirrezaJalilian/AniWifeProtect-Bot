import traceback
from config import TARGET_GROUP_ID, SOURCE_CHANNEL_ID
from commands.commands import router
from dbmanagers.noticechannel import set_message_map, get_group_message_id
from Logger import send_error,send_info,send_notice
from telegram.ext import filters

async def message_handler(update, context):
    try:
        if update.effective_message:
            await router.handle(update, context)
    except Exception as e:
        await send_error(update,context,"Bot",f"Critical Error in message_handler: {e}")
        traceback.print_exc()


class FilterNewChannelPost(filters.UpdateFilter):
    def filter(self, update):
        return bool(update.channel_post)

class FilterEditedChannelPost(filters.UpdateFilter):
    def filter(self, update):
        return bool(update.edited_channel_post)

IS_NEW_POST = FilterNewChannelPost()
IS_EDITED_POST = FilterEditedChannelPost()

async def handle_new_post(update, context):
    msg = update.channel_post
    ch_msg_id = str(msg.message_id) 

    try:
        forwarded_msg = await context.bot.forward_message(
            chat_id=TARGET_GROUP_ID,
            from_chat_id=SOURCE_CHANNEL_ID,
            message_id=msg.message_id
        )
        
        set_message_map(ch_msg_id, forwarded_msg.message_id)
        await send_info(update,context,SOURCE_CHANNEL_ID,"Forwarded New Message From Main Channel")

    except Exception as e:
        await send_error(update,context,"Bot",f"Error forwarding: {e}")

async def handle_edited_post(update, context):
    edited_msg = update.edited_channel_post
    ch_msg_id = str(edited_msg.message_id)

    old_group_msg_id = get_group_message_id(ch_msg_id)

    if old_group_msg_id:
        try:
            await context.bot.delete_message(
                chat_id=TARGET_GROUP_ID,
                message_id=int(old_group_msg_id)
            )
            await send_notice(update,context,"Bot","Deleted Old Message From Main Group")
        except Exception as e:
            await send_error(update,context,"Bot",f"Could not delete old message from main group: {e}")
    else:
        await send_notice(update,context,"Bot", "No old mapping found. It might be a new edit for an unmapped post.")
    
    try:
        new_forwarded_msg = await context.bot.forward_message(
            chat_id=TARGET_GROUP_ID,
            from_chat_id=SOURCE_CHANNEL_ID,
            message_id=edited_msg.message_id
        )
        
        set_message_map(ch_msg_id, new_forwarded_msg.message_id)
        
        await send_info(update,context,"Bot",f"Re-forwarded. New Group ID: {new_forwarded_msg.message_id}")
        
    except Exception as e:
        await send_error(update,context,"Bot",f"Error re-forwarding: {e}")