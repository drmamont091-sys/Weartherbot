from telegram import Update 
from telegram.ext import Application, CommandHandler, ContextTypes
TOKEN = "9131187558:AAGFll0Y-edU7OjS9SWRVf-Qyy1N2BT3PqM"
 
async def start (update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я погодный бот Краснодара!")

app = Application.builder().token(TOKEN).build() 
app.add_handler(CommandHandler ("start", start))
app.run_polling()