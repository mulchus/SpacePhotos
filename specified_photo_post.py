from sys import argv
import os
import constants
import functions
import telegram_bot
import random
from dotenv import load_dotenv
from pathlib import Path


path = argv[1]
if os.path.isfile(path):
    telegram_bot.bot_send_photo(constants.chat_id, path)
else:
    random_photo = random.choice(functions.path_of_files(Path.cwd() / 'Images'))
    telegram_bot.bot_send_photo(constants.chat_id, random_photo)


if __name__ == '__main__':
    load_dotenv()
