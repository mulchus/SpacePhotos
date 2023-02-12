import requests
from pathlib import Path
import argparse
import datetime
import functions
import os
from dotenv import load_dotenv


def get_all_images_url(payload, date):
    images_url = f'https://api.nasa.gov/EPIC/api/natural/date/{date}'
    response = requests.get(images_url, params=payload)
    response.raise_for_status()
    return response


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    epic_parser = argparse.ArgumentParser(description='Загрузка фото Земли из NASA EPIC по введенной дате')
    epic_parser.add_argument(
        'image_date',
        nargs='?',
        default=datetime.datetime.today().strftime('%d.%m.%Y'),
        help='дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата)'
    )

    args = epic_parser.parse_args()
    try:
        functions.format_date(args.image_date)
    except ValueError:
        print('Неверно введена дата')
        exit()

    _, date, date_ = functions.format_date(args.image_date)

    # generating a list of all id of images
    payload = {'api_key': nasa_api_key}
    images_id = [nasa_record['image'] for nasa_record in get_all_images_url(payload, date).json()
                 if nasa_record['image']]
    images = [f'https://api.nasa.gov/EPIC/archive/natural/{date_}/png/{image_id}.png' for image_id in images_id]

    year, month, day = date_.split('/')

    epic_dir = Path.cwd() / 'Images' / 'NASA' / 'EPIC'
    Path(epic_dir).mkdir(parents=True, exist_ok=True)
    file_path = Path.joinpath(epic_dir, f'nasa_epic_{day}.{month}.{year}_')

    files_count = functions.save_file(images, file_path, payload)

    print(f'Скачивание фото Земли от {day}.{month}.{year} завершено. Скачано {files_count} шт.\n')


if __name__ == '__main__':
    main()
