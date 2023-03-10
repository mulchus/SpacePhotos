import argparse
import time
from os import listdir, path
import os
import telegram_bot
from random import shuffle
from dotenv import load_dotenv
from telegram.error import NetworkError


def main():
    load_dotenv()
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']

    image_parser = argparse.ArgumentParser(description='Публикация фото из заданной директории по алгоритму')
    image_parser.add_argument(
        'directory',
        nargs='?',
        default=os.path.join(os.getcwd(), 'Images', 'SpaceX'),
        help='директория с фото (по умолчанию - ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ/Images/SpaceX)'
    )
    image_parser.add_argument(
        'pause',
        nargs='?',
        default=14400,
        type=int,
        help='задержка между публикациями в секундах (по умолчанию 14400 сек)'
    )

    args = image_parser.parse_args()
    directory = args.directory
    pause = args.pause

    files = [f for f in listdir(directory) if path.isfile(path.join(directory, f))]

    while True:
        for file in files:
            try:
                telegram_bot.send_photo(telegram_bot_token, telegram_chat_id, os.path.join(directory, file))
            except NetworkError:
                time.sleep(1)
            time.sleep(pause) if pause == 14400 else time.sleep(3)  # хитрые паузы согласно заданию

        shuffle(files)
        time.sleep(pause) if pause != 14400 else 0  # хитрые паузы согласно заданию


if __name__ == '__main__':
    main()
