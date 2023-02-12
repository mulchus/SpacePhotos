import requests
from pathlib import Path
import argparse
import functions


def get_all_images_urls(id_launch, ):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id_launch}')
    response.raise_for_status()
    images_urls = response.json()['links']['flickr']['original']
    return images_urls


def main():
    parser_spacex = argparse.ArgumentParser(description='Ввод ID запуска для SpaceX (по умолчанию - последний запуск)')
    parser_spacex.add_argument(
        'id',
        default='latest',
        nargs='?',
        help='загрузка фото по введенному коду запуска SpaceX'
    )

    id_launch = parser_spacex.parse_args().id
    images_urls = get_all_images_urls(id_launch)

    images_dir = Path.cwd() / 'Images' / 'SpaceX'
    Path(images_dir).mkdir(parents=True, exist_ok=True)
    file_path = Path.joinpath(images_dir, 'spacex_')

    numbers_of_file = functions.save_file(images_urls, file_path)

    print(f'Скачивание запуска ID {id_launch} завершено\n Скачано {numbers_of_file} фото')


if __name__ == '__main__':
    main()
