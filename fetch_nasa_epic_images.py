import requests
from pathlib import Path
import argparse
import datetime
from os import path
import functions
import constants


def main():
    parser_epic = argparse.ArgumentParser(description='Загрузка фото Земли из NASA EPIC по введенной дате')
    parser_epic.add_argument(
        'date_image',
        nargs='?',
        default=datetime.datetime.today().strftime('%d.%m.%Y'),
        help='дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата)'
    )

    day, month, year = parser_epic.parse_args().date_image.split('.')  # date of fotos
    print(day, month, year)
    payload = {'api_key': constants.nasa_api_key}
    all_images_url = f'https://api.nasa.gov/EPIC/api/natural/date/{year}-{month}-{day}'
    response = requests.get(all_images_url, params=payload)
    response.raise_for_status()

    # generating a list of all id of images
    idimages_list = []
    for nasa_record in response.json():
        if nasa_record['image']:
            idimages_list.append(nasa_record['image'])

    images_list = []
    for idimage in idimages_list:
        images_list.append(f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{idimage}.png')

    file_path = f'{path.dirname(__file__)}/Images/NASA/EPIC/'
    Path(file_path).mkdir(parents=True, exist_ok=True)
    file_name_pattern = f'nasa_epic_{day}.{month}.{year}_'

    numbers_of_file = functions.file_save(images_list, file_path, file_name_pattern, payload)

    print(f'Скачивание фото Земли от {day}.{month}.{year} завершено. Скачано {numbers_of_file} шт.\n')


if __name__ == '__main__':
    main()
