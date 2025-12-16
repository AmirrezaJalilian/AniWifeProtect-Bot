import traceback

from command.router import router
from log.logger import send_log
from log.type import LogTypes
from handler.anti_link import anti_link


async def message_handler(update, context):
    try:
        if update.effective_message:
            await router.handle(update, context)
    except Exception as e:
        await send_log(context, LogTypes.WARN, "Bot", f"Critical Error in message_handler: {e}")
        traceback.print_exc()
    try:
        await anti_link(update, context)
    except:
        pass
