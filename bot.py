from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
from config import Token, SOURCE_CHANNEL_ID
from commands.start import start
from handlers import message_handler, handle_new_post, handle_edited_post


class FilterNewChannelPost(filters.UpdateFilter):
    def filter(self, update):
        return bool(update.channel_post)

class FilterEditedChannelPost(filters.UpdateFilter):
    def filter(self, update):
        return bool(update.edited_channel_post)

IS_NEW_POST = FilterNewChannelPost()
IS_EDITED_POST = FilterEditedChannelPost()


def main():
    app = ApplicationBuilder().token(Token).build()
    
    app.add_handler(CommandHandler("start", start))
    
    my_channel = filters.Chat(chat_id=SOURCE_CHANNEL_ID)

    app.add_handler(MessageHandler(my_channel & IS_NEW_POST, handle_new_post))
    
    app.add_handler(MessageHandler(my_channel & IS_EDITED_POST, handle_edited_post))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()