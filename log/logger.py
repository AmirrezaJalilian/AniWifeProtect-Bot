from telegram.ext import ContextTypes
from bot_config import LOG_GROUP_ID
from log.type import LogTypes


async def send_log(context: ContextTypes.DEFAULT_TYPE, log_type: LogTypes, log_from: str | int, log_text: str):

    await context.bot.send_message(
        LOG_GROUP_ID,
        f"{log_type} - From {log_from}: {log_text}",
        parse_mode='HTML'
    )
