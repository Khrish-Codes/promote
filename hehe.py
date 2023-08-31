from telegram import Bot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6127225004:AAGmqiJQ92B-W05c-XQRg-708pkfdmL1DaA'

# Replace with the actual user ID and channel ID
USER_ID = 5151264430
CHANNEL_ID = -1001685735199

def main():
    bot = Bot(token=BOT_TOKEN)
    
    try:
        bot.promote_chat_member(CHANNEL_ID, USER_ID, can_change_info=True, can_invite_users=True)
        print(f"User with ID {USER_ID} promoted in channel with ID {CHANNEL_ID}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
