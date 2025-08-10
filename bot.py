import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

TOKEN = os.getenv('TELEGRAM_TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bot démarré! Envoyez /like <uid> <server_name>")

def send_like(update: Update, context: CallbackContext) -> None:
    try:
        if len(context.args) < 2:
            update.message.reply_text("Usage: /like <uid> <server_name>")
            return
            
        uid = context.args[0]
        server_name = context.args[1]
        api_url = f"https://fixedapi-lipugaming.vercel.app/like?uid={uid}&server_name={server_name}"
        
        response = requests.get(api_url)
        data = response.json()
        
        reply = (
            f"Résultats:\n"
            f"Level: {data.get('Level', 'N/A')}\n"
            f"Likes: {data.get('LikesGivenByAPI', 'N/A')}\n"
            f"Avant: {data.get('LikesbeforeCommand', 'N/A')}\n"
            f"Après: {data.get('LikesafterCommand', 'N/A')}\n"
            f"Status: {'Succès' if data.get('status', 0) == 1 else 'Échec'}"
        )
        
        update.message.reply_text(reply)
        
    except Exception as e:
        update.message.reply_text(f"Erreur: {str(e)}")

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("like", send_like))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
