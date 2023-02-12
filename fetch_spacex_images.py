import requests
from pathlib import Path
import argparse
import functions


def get_all_images_urls(launch_id):
    try:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
        response.raise_for_status()
        images_urls = response.json()['links']['flickr']['original']
        return images_urls
    except requests.exceptions.HTTPError as e:
        print(f'Указан неверный ID запуска.\nОшибка {e}')
        exit()


def main():
    spacex_parser = argparse.ArgumentParser(description='Ввод ID запуска для SpaceX (по умолчанию - последний запуск)')
    spacex_parser.add_argument(
        'id',
        default='latest',
        nargs='?',
        help='загрузка фото по введенному коду запуска SpaceX'
    )

    launch_id = spacex_parser.parse_args().id
    images_urls = get_all_images_urls(launch_id)

    images_dir = Path.cwd() / 'Images' / 'SpaceX'
    Path(images_dir).mkdir(parents=True, exist_ok=True)
    file_path = Path.joinpath(images_dir, 'spacex_')

    files_count = functions.save_file(images_urls, file_path)

    print(f'Скачивание запуска ID {launch_id} завершено\n Скачано {files_count} фото')


if __name__ == '__main__':
    main()
