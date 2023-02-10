import telegram


def send_photo(telegram_bot_token, telegram_chat_id, path_to_file):
    bot = telegram.Bot(token=telegram_bot_token)
    with open(path_to_file, 'rb') as file:
        bot.send_photo(telegram_chat_id, photo=file)
