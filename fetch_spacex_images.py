import requests
from pathlib import Path
from os import path
from urllib import parse


def main():
    id_of_launch = input('Введите ID запуска: ')
    all_images_url = f'https://api.spacexdata.com/v5/launches/{id_of_launch}'  # 5eb87d42ffd86e000604b384
    response = requests.get(all_images_url)
    response.raise_for_status()

    images_list = response.json()['links']['flickr']['original']

    file_path = './Images/SpaceX/'  # first symbol is '.' if path is project directory continuation
    Path(file_path).mkdir(parents=True, exist_ok=True)

    file_name_pattern = 'spacex_'

    for file_number, file_url in enumerate(images_list):
        file_ext = path.splitext(parse.urlsplit(file_url).path)[1]
        file_name = f'{file_name_pattern}{file_number + 1}{file_ext}'

        headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
        response = requests.get(file_url, headers=headers)
        response.raise_for_status()

        with open(f'{file_path}{file_name}', 'wb') as file:
            file.write(response.content)

    print(f'Скачивание запуска ID {id_of_launch} завершено\n')
