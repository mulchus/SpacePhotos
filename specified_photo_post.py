from sys import argv
import os
import functions
import constants
import mulcherbot
import random


path = argv[1]
if os.path.isfile(path):
    mulcherbot.bot_send_photo(constants.chat_id, path)
else:
    random_photo = random.choice(functions.path_of_files(f'{constants.work_dir}/Images'))
    mulcherbot.bot_send_photo(constants.chat_id, random_photo)


def main():
    # for i in mulcherbot.bot.get_updates():
    #     print(f'{i}\n')
    pass


if __name__ == '__main__':
    main()
