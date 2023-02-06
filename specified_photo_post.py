from sys import argv
import os
import constants
import functions
import mulcherbot
import random
from dotenv import load_dotenv


path = argv[1]
if os.path.isfile(path):
    mulcherbot.bot_send_photo(constants.chat_id, path)
else:
    random_photo = random.choice(functions.path_of_files(f'{constants.work_dir}/Images'))
    mulcherbot.bot_send_photo(constants.chat_id, random_photo)


if __name__ == '__main__':
    load_dotenv()
