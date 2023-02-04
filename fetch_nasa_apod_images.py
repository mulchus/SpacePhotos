import requests
from pathlib import Path
from os import path
import argparse
import datetime
import functions
import constants


def main():
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

    s_day, s_month, s_year = parser_apod.parse_args().start_date.split('.')
    e_day, e_month, e_year = parser_apod.parse_args().end_date.split('.')

    # date of fotos
    print(f'{s_year}-{s_month}-{s_day}', f'{e_year}-{e_month}-{e_day}')

    start_date = f'{s_year}-{s_month}-{s_day}'
    end_date = f'{e_year}-{e_month}-{e_day}'

    payload = {'api_key': constants.nasa_api_key, 'start_date': start_date, 'end_date': end_date}
    all_files_url = 'https://api.nasa.gov/planetary/apod'

    response = requests.get(all_files_url, params=payload)
    response.raise_for_status()

    # generating a list of all image
    images_list = []
    for nasa_record in response.json():
        if nasa_record['url']:
            images_list.append(nasa_record['url'])

    file_path = f'{path.dirname(__file__)}/Images/NASA/APOD/'
    Path(file_path).mkdir(parents=True, exist_ok=True)
    file_name_pattern = 'nasa_apod_'  # for NASA APOD save

    numbers_of_file = functions.file_save(images_list, file_path, file_name_pattern, payload)

    print(f'Скачивание фото с {start_date} по.{end_date} завершено. Скачано {numbers_of_file} шт.\n')


if __name__ == '__main__':
    main()
