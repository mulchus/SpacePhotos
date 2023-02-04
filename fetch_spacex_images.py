import requests
from pathlib import Path
from os import path
from urllib import parse
import argparse


def main():
    parserSpaceX = argparse.ArgumentParser(description='Ввод ID запуска для SpaceX (по умолчанию - последний запуск)')
    parserSpaceX.add_argument(
        'id',
        nargs='?',
        help='загрузка фото по введенному коду запуска SpaceX'
    )

    id_launch = parserSpaceX.parse_args().id

    if not id_launch:
        response = requests.get('https://api.spacexdata.com/v5/launches/latest')
        response.raise_for_status()
        id_launch = response.json()['id']
    print(id_launch)

    all_images_url = f'https://api.spacexdata.com/v5/launches/{id_launch}'  # 5eb87d42ffd86e000604b384
    response = requests.get(all_images_url)
    response.raise_for_status()

    images_list = response.json()['links']['flickr']['original']

    file_path = f'{path.dirname(__file__)}/Images/SpaceX/'  # first symbol is '.' if path is project directory continuation
    Path(file_path).mkdir(parents=True, exist_ok=True)

    file_name_pattern = 'spacex_'
    numbers_of_file = 0
    for file_number, file_url in enumerate(images_list):
        file_ext = path.splitext(parse.urlsplit(file_url).path)[1]
        file_name = f'{file_name_pattern}{file_number + 1}{file_ext}'

        headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
        response = requests.get(file_url, headers=headers)
        response.raise_for_status()

        with open(f'{file_path}{file_name}', 'wb') as file:
            file.write(response.content)
        numbers_of_file += 1

    print(f'Скачивание запуска ID {id_launch} завершено\n Скачано {numbers_of_file} фото')


if __name__ == '__main__':
    main()
