from sys import argv
import os
import functions
import telegram_bot
import random
from pathlib import Path
from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    try:
        path = argv[1]
    except IndexError:
        print('Не указан путь к папке с файлами!')
        exit()
    if os.path.isfile(path):
        telegram_bot.bot_send_photo(telegram_bot_token, telegram_chat_id, path)
    else:
        random_photo = random.choice(functions.get_paths_of_files(Path.cwd() / 'Images'))
        telegram_bot.bot_send_photo(telegram_bot_token, telegram_chat_id, random_photo)


if __name__ == '__main__':
    main()
