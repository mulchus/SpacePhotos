import requests
from pathlib import Path
from os import path
import argparse
import functions


def main():
    parser_spacex = argparse.ArgumentParser(description='Ввод ID запуска для SpaceX (по умолчанию - последний запуск)')
    parser_spacex.add_argument(
        'id',
        nargs='?',
        help='загрузка фото по введенному коду запуска SpaceX'
    )

    id_launch = 'latest' if parser_spacex.parse_args().id is None else parser_spacex.parse_args().id
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id_launch}')
    response.raise_for_status()

    images = response.json()['links']['flickr']['original']

    file_path = f'{path.dirname(__file__)}/Images/SpaceX/'
    Path(file_path).mkdir(parents=True, exist_ok=True)
    file_name_pattern = 'spacex_'

    numbers_of_file = functions.file_save(images, file_path, file_name_pattern)

    print(f'Скачивание запуска ID {id_launch} завершено\n Скачано {numbers_of_file} фото')


if __name__ == '__main__':
    main()
