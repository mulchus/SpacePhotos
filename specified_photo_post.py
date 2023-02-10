import argparse
import os
import functions
import telegram_bot
import random
from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    parser_image = argparse.ArgumentParser(description='Публикация фото по конкретному пути')
    parser_image.add_argument(
        'path',
        nargs='?',
        default=os.path.join(os.getcwd(), 'Images'),
        help='директория с фото (по умолчанию - ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ/Images)'
    )

    path = parser_image.parse_args().path

    if os.path.isfile(path):
        telegram_bot.send_photo(telegram_bot_token, telegram_chat_id, path)
    else:
        random_photo = random.choice(functions.get_paths_of_files(path))
        telegram_bot.send_photo(telegram_bot_token, telegram_chat_id, random_photo)


if __name__ == '__main__':
    main()
