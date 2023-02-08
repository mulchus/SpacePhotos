from sys import argv
import time
from os import listdir, path
import os
import telegram_bot
from random import shuffle
from dotenv import load_dotenv


def main():
    load_dotenv()
    special_pause = int(os.environ['SPECIAL_PAUSE'])
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    try:
        directory = argv[1] if argv[1] else os.getcwd()
    except IndexError:
        directory = ''
        print('Не указан путь к папке с файлами!')
        exit()
    try:
        pause = int(argv[2])
    except IndexError:
        print(f'По умолчанию задана пауза = {special_pause}!')
        pause = special_pause

    onlyfiles = [f for f in listdir(directory) if path.isfile(path.join(directory, f))]

    while True:
        for file in onlyfiles:
            print(directory)
            telegram_bot.bot_send_photo(telegram_bot_token, telegram_chat_id, f'{directory}{file}')
            time.sleep(pause) if pause == special_pause else time.sleep(3)  # хитрые паузы согласно заданию
        shuffle(onlyfiles)
        time.sleep(pause) if pause != special_pause else 0  # хитрые паузы согласно заданию


if __name__ == '__main__':
    main()
