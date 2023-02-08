import requests
from pathlib import Path
import argparse
import datetime
import functions
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    parser_apod = argparse.ArgumentParser(description='Загрузка фото из NASA APOD по введенным датам с- по-')
    parser_apod.add_argument(
        'start_date',
        nargs='?',
        default=datetime.datetime.today().strftime('%d.%m.%Y'),
        help='начальная дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата)'
    )
    parser_apod.add_argument(
        'end_date',
        nargs='?',
        default=datetime.datetime.today().strftime('%d.%m.%Y'),
        help='конечная дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата)'
    )

    try:
        print(datetime.datetime.strptime(parser_apod.parse_args().start_date, "%d.%m.%Y").date())
    except ValueError:
        print('Неверно введена начальная дата')
        exit()
    try:
        print(datetime.datetime.strptime(parser_apod.parse_args().end_date, "%d.%m.%Y").date())
    except ValueError:
        print('Неверно введена конечная дата')
        exit()

    # date of fotos
    start_date = datetime.datetime.strptime(parser_apod.parse_args().start_date, "%d.%m.%Y").date().strftime("%Y-%m-%d")
    end_date = datetime.datetime.strptime(parser_apod.parse_args().end_date, "%d.%m.%Y").date().strftime("%Y-%m-%d")

    payload = {'api_key': nasa_api_key, 'start_date': start_date, 'end_date': end_date}
    all_files_url = 'https://api.nasa.gov/planetary/apod'

    response = requests.get(all_files_url, params=payload)
    response.raise_for_status()

    # generating a list of all image
    images = []
    for nasa_record in response.json():
        if nasa_record['media_type'] == 'image' and nasa_record['url']:
            images.append(nasa_record['url'])

    Path(Path.cwd() / 'Images' / 'NASA' / 'APOD').mkdir(parents=True, exist_ok=True)
    file_path = Path.cwd() / 'Images' / 'NASA' / 'APOD' / 'nasa_apod_'

    numbers_of_file = functions.save_file(images, file_path, payload)

    print(f'Скачивание фото с {start_date} по.{end_date} завершено. Скачано {numbers_of_file} шт.\n')


if __name__ == '__main__':
    main()
