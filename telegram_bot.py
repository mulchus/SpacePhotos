import telegram


def send_photo(telegram_bot_token, telegram_chat_id, file_path):
    bot = telegram.Bot(token=telegram_bot_token)
    with open(file_path, 'rb') as file:
        bot.send_photo(telegram_chat_id, photo=file)
