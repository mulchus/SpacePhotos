import requests
from pathlib import Path
import argparse
import datetime
import functions
import os
from dotenv import load_dotenv


def get_all_files_info(payload):
    files_info_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(files_info_url, params=payload)
    response.raise_for_status()
    return response


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    apod_parser = argparse.ArgumentParser(description='Загрузка фото из NASA APOD по введенным датам с- по-')
    apod_parser.add_argument(
        'start_date',
        nargs='?',
        default=datetime.datetime.today().strftime('%d.%m.%Y'),
        help='начальная дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата)'
    )
    apod_parser.add_argument(
        'end_date',
        nargs='?',
        default=datetime.datetime.today().strftime('%d.%m.%Y'),
        help='конечная дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата)'
    )

    args = apod_parser.parse_args()
    try:
        functions.format_date(args.start_date)
    except ValueError:
        print('Неверно введена начальная дата')
        exit()
    try:
        functions.format_date(args.end_date)
    except ValueError:
        print('Неверно введена конечная дата')
        exit()

    # date of fotos
    _, start_date, _ = functions.format_date(args.start_date)
    _, end_date, _ = functions.format_date(args.end_date)

    payload = {'api_key': nasa_api_key, 'start_date': start_date, 'end_date': end_date}

    response = get_all_files_info(payload)

    # generating a list of all image
    images = [nasa_record['url'] for nasa_record in response.json() if nasa_record['media_type'] == 'image'
              and nasa_record['url']]

    apod_dir = Path.cwd() / 'Images' / 'NASA' / 'APOD'
    Path(apod_dir).mkdir(parents=True, exist_ok=True)
    file_path = Path.joinpath(apod_dir, 'nasa_apod_')

    files_count = functions.save_file(images, file_path, payload)

    print(f'Скачивание фото с {start_date} по.{end_date} завершено. Скачано {files_count} шт.\n')


if __name__ == '__main__':
    main()
