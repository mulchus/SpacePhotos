import requests
from pathlib import Path
import argparse
import datetime
import functions
import os
from dotenv import load_dotenv


def get_all_images_url(payload, date):
    all_images_url = f'https://api.nasa.gov/EPIC/api/natural/date/{date}'
    response = requests.get(all_images_url, params=payload)
    response.raise_for_status()
    return response


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser_epic = argparse.ArgumentParser(description='Загрузка фото Земли из NASA EPIC по введенной дате')
    parser_epic.add_argument(
        'date_image',
        nargs='?',
        default=datetime.datetime.today().strftime('%d.%m.%Y'),
        help='дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата)'
    )

    args = parser_epic.parse_args()
    try:
        functions.format_date(args.date_image)
    except ValueError:
        print('Неверно введена дата')
        exit()

    _, date, date_ = functions.format_date(args.date_image)

    # generating a list of all id of images
    payload = {'api_key': nasa_api_key}
    idimages = [nasa_record['image'] for nasa_record in get_all_images_url(payload, date).json() if nasa_record['image']]
    images = [f'https://api.nasa.gov/EPIC/archive/natural/{date_}/png/{idimage}.png' for idimage in idimages]

    year, month, day = date_.split('/')

    Path(Path.cwd() / 'Images' / 'NASA' / 'EPIC').mkdir(parents=True, exist_ok=True)
    file_path = Path.cwd() / 'Images' / 'NASA' / 'EPIC' / f'nasa_epic_{day}.{month}.{year}_'

    numbers_of_file = functions.save_file(images, file_path, payload)

    print(f'Скачивание фото Земли от {day}.{month}.{year} завершено. Скачано {numbers_of_file} шт.\n')


if __name__ == '__main__':
    main()
