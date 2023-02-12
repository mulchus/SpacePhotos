import argparse
import os
import telegram_bot
import random
from dotenv import load_dotenv


def get_paths_of_files(start_dir):  # make a list of paths for all files in start directory
    file_paths = [os.path.abspath(os.path.join(folder, filename)) for folder, _, files in os.walk(start_dir)
                  for filename in files]
    return file_paths


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
    elif os.path.isdir(path):
        try:
            random_photo = random.choice(get_paths_of_files(path))
            telegram_bot.send_photo(telegram_bot_token, telegram_chat_id, random_photo)
        except (IndexError, NameError) as error:
            print(f'Неверно указан путь к файлу или директории.\nОшибка: {error}')
    else:
        print('Неверно указан путь к файлу или директории')


if __name__ == '__main__':
    main()
