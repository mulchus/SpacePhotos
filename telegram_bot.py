import telegram


def bot_send_photo(telegram_bot_token, telegram_chat_id, path_to_file):
    bot = telegram.Bot(token=telegram_bot_token)
    bot.send_photo(telegram_chat_id, photo=open(path_to_file, 'rb'))
    return
