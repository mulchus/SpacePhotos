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

    id_launch = parser_spacex.parse_args().id

    if not id_launch:
        response = requests.get('https://api.spacexdata.com/v5/launches/latest')
        response.raise_for_status()
        id_launch = response.json()['id']
    print(id_launch)

    all_images_url = f'https://api.spacexdata.com/v5/launches/{id_launch}'  # 5eb87d42ffd86e000604b384
    response = requests.get(all_images_url)
    response.raise_for_status()

    images_list = response.json()['links']['flickr']['original']

    file_path = f'{path.dirname(__file__)}/Images/SpaceX/'
    Path(file_path).mkdir(parents=True, exist_ok=True)
    file_name_pattern = 'spacex_'

    numbers_of_file = functions.file_save(images_list, file_path, file_name_pattern)

    print(f'Скачивание запуска ID {id_launch} завершено\n Скачано {numbers_of_file} фото')


if __name__ == '__main__':
    main()
