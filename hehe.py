from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6286222522:AAGDmZF5xdpakB8_4-SpmATSjerBVG4iohs'

# Replace 'CHANNEL_ID' with the actual channel ID
CHANNEL_ID = -1001626206283  # Replace with the channel ID

def promote_specific_user(update: Update, context: CallbackContext) -> None:
    username_to_promote = "@Harima_Nagar_1"  # Replace with the specific username
    user = context.bot.get_chat_member(CHANNEL_ID, username_to_promote).user
    context.bot.promote_chat_member(CHANNEL_ID, user.id, can_change_info=True, can_invite_users=True)

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('promote_specific_user', promote_specific_user))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
