import traceback

from command.router import router
from log.logger import send_log
from log.type import LogTypes


async def router_command(update, context):
    try:
        if update.effective_message:
            await router.handle(update, context)
    except Exception as e:
        await send_log(context, LogTypes.WARN, "Bot", f"Critical Error in message_handler: {e}")
        traceback.print_exc()
