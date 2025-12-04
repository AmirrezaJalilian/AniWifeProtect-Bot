from telegram import Update
from telegram.ext import ContextTypes

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    
    await update.effective_message.reply_text("Start")