from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    filters
)

from handler.join import join_handler
from handler.left import left_handler
from handler.anti_link import anti_link
from handler.command_router import router_command
from bot_config import TOKEN
from command.start import start


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(MessageHandler(filters.TEXT, anti_link))
    app.add_handler(MessageHandler(filters.TEXT, router_command))

    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, join_handler))

    app.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, left_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
