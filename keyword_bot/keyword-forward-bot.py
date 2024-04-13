#a telegram bot to monitor a public cahnnel, detect specific keywords and forwarding them to another channel
import os
from typing import Final
from telegram import Update
from telegram.ext import (
    CommandHandler, 
    MessageHandler, 
    filters, 
    ContextTypes, 
    CallbackContext, 
    Application
)

#Bot Information
BOT_TOKEN:Final = os.environ.get("BOT_TOKEN")

#Channel Information
SOURCE_CHANNEL:Final = "@rahgirrafiBotTestingChannel"
DESTINATION_CHANNEL:Final = "@rahgirrafiBotTestingChannelDest"

#keyword to monitor
KEYWORDS = ["python", "java", "c++", "javascript"]

#bot command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am a bot to monitor a public channel and forward messages containing specific keywords to another channel")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I am a bot to monitor a public channel and forward messages containing specific keywords to another channel. I am still under development")

#function to handle incoming messages
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    message:str = update.channel_post.text.lower()
    for keyword in KEYWORDS:
        if keyword in message:
            await context.bot.forward_message(chat_id=DESTINATION_CHANNEL, from_chat_id=update.channel_post.chat_id, message_id=update.channel_post.message_id)
            break

#error handlers
async def error_handler(update: Update, context: CallbackContext) -> None:
    #send what error occured
    print(f"An error occured: {context.error}")
#main function

def main() -> None:
    print("Bot is running")
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    
    # Message Handler
    app.add_handler(MessageHandler(filters.TEXT, message_handler))
    
    # Error Handler
    app.add_error_handler(error_handler)
    
    print("Polling....")
    app.run_polling(poll_interval=5)
    
    
if __name__ == "__main__":
    main()

