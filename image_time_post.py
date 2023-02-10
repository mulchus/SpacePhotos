import argparse
import time
from os import listdir, path
import os
import telegram_bot
from random import shuffle
from dotenv import load_dotenv


def main():
    load_dotenv()
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']

    parser_image = argparse.ArgumentParser(description='Публикация фото из заданной директории по алгоритму')
    parser_image.add_argument(
        'directory',
        nargs='?',
        default=os.path.join(os.getcwd(), 'Images', 'SpaceX'),
        help='директория с фото (по умолчанию - ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ/Images/SpaceX)'
    )
    parser_image.add_argument(
        'pause',
        nargs='?',
        default=14400,
        help='задержка между публикациями в секундах (по умолчанию 14400 сек)'
    )

    directory = parser_image.parse_args().directory
    pause = parser_image.parse_args().pause

    onlyfiles = [f for f in listdir(directory) if path.isfile(path.join(directory, f))]

    while True:
        for file in onlyfiles:
            telegram_bot.bot_send_photo(telegram_bot_token, telegram_chat_id, os.path.join(directory, file))
            time.sleep(pause) if pause == 14400 else time.sleep(3)  # хитрые паузы согласно заданию
        shuffle(onlyfiles)
        time.sleep(pause) if pause != 14400 else 0  # хитрые паузы согласно заданию


if __name__ == '__main__':
    main()
