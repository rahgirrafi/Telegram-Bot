#a telegram bot to monitor a public cahnnel, detect specific keywords and forwarding them to another channel
from typing import Final
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext

#Bot Information
BOT_TOKEN:Final = "7068464356:AAF8cZjuPk6C2fBcqJMINvVVMGZvqz_nIbM"

#Channel Information
SOURCE_CHANNEL:Final = "@rahgirrafiBotTestingChannel"
DESTINATION_CHANNEL:Final = "@rahgirrafiBotTestingChannelDest"

def send_welcome