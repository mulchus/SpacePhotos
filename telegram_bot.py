import telegram
from dotenv import load_dotenv
import os


def bot_send_photo(path_to_file):
    bot.send_photo(chat_id, photo=open(path_to_file, 'rb'))
    return


if __name__ == '__main__':
    pass
else:
    load_dotenv()
    telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('CHAT_ID')
    bot = telegram.Bot(token=telegram_bot_token)
