from sys import argv
import time
from os import listdir, path
import constants
import telegram_bot
from random import shuffle


directory = argv[1]
pause = int(argv[2])
if not pause:
    pause = 2

onlyfiles = [f for f in listdir(directory) if path.isfile(path.join(directory, f))]

while True:
    for file in onlyfiles:
        telegram_bot.bot_send_photo(constants.chat_id, f'{directory}{file}')
        time.sleep(pause) if pause == constants.pause_beetwen_posts else time.sleep(3)  # хитрые паузы согласно заданию
    shuffle(onlyfiles)
    time.sleep(pause) if pause != constants.pause_beetwen_posts else 0  # хитрые паузы согласно заданию
