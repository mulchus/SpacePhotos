from sys import argv
import os
import functions
import telegram_bot
import random
from pathlib import Path


path = argv[1]
if os.path.isfile(path):
    telegram_bot.bot_send_photo(path)
else:
    random_photo = random.choice(functions.path_of_files(Path.cwd() / 'Images'))
    telegram_bot.bot_send_photo(random_photo)
