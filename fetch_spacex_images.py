import requests
from pathlib import Path
import argparse
import functions


def main():
    parser_spacex = argparse.ArgumentParser(description='Ввод ID запуска для SpaceX (по умолчанию - последний запуск)')
    parser_spacex.add_argument(
        'id',
        default='latest',
        nargs='?',
        help='загрузка фото по введенному коду запуска SpaceX'
    )

    id_launch = parser_spacex.parse_args().id
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id_launch}')
    response.raise_for_status()

    images = response.json()['links']['flickr']['original']

    Path(Path.cwd() / 'Images' / 'SpaceX').mkdir(parents=True, exist_ok=True)
    file_path = Path.cwd() / 'Images' / 'SpaceX' / 'spacex_'

    numbers_of_file = functions.save_file(images, file_path)

    print(f'Скачивание запуска ID {id_launch} завершено\n Скачано {numbers_of_file} фото')


if __name__ == '__main__':
    main()
