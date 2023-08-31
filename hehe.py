import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6286222522:AAGDmZF5xdpakB8_4-SpmATSjerBVG4iohs'

# Replace 'TARGET_USERNAME' with the username of the user to be promoted
TARGET_USERNAME = '@Harima_Nagar_1'

# Configure logging
logging.basicConfig(filename='bot.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

CHANNEL_ID = 0  # Global variable to store the channel ID

# Conversation states
CHOOSE_CHANNEL = range(1)

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Send me the channel ID where you want to be promoted.")
    return CHOOSE_CHANNEL

def choose_channel(update: Update, context: CallbackContext) -> None:
    global CHANNEL_ID
    CHANNEL_ID = int(update.message.text)

    user_id = update.message.from_user.id
    user_username = update.message.from_user.username
    
    # Check if the user is authorized
    if user_username == TARGET_USERNAME:
        context.bot.promote_chat_member(CHANNEL_ID, user_id, can_change_info=True, can_invite_users=True)
        update.message.reply_text("You've been promoted! 🎉")
    else:
        update.message.reply_text("You are not authorized for promotion.")
    
    return ConversationHandler.END

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Create a conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('okpromoteme', start)],
        states={
            CHOOSE_CHANNEL: [MessageHandler(Filters.text, choose_channel)],
        },
        fallbacks=[],
    )
    
    dispatcher.add_handler(conv_handler)

    # Log all errors to a file
    dispatcher.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()

def error_handler(update: Update, context: CallbackContext):
    """Log the error caused by an update."""
    logging.error(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    main()
