from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

def promote_user(update: Update, context: CallbackContext) -> None:
    if update.message.text == '/okpromotemeidiot':
        user_id = update.message.from_user.id
        context.bot.promote_chat_member(user_id, can_change_info=True, can_invite_users=True)

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.private, promote_user))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
