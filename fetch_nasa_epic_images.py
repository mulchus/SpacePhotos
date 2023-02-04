import requests
from pathlib import Path
from dotenv import load_dotenv
import os
import argparse
import datetime
from os import path


def main():
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")

    parser_epic = argparse.ArgumentParser(description='Загрузка фото Земли из NASA EPIC по введенной дате')
    parser_epic.add_argument(
        'date_image',
        nargs='?',
        default=datetime.datetime.today().strftime('%d.%m.%Y'),
        help='дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата)'
    )

    day, month, year = parser_epic.parse_args().date_image.split('.')  # date of fotos
    print(day, month, year)
    payload = {'api_key': nasa_api_key}
    all_images_url = f'https://api.nasa.gov/EPIC/api/natural/date/{year}-{month}-{day}'
    print(all_images_url)
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

    file_path = f'{path.dirname(__file__)}/Images/NASA/EPIC/'  # for NASA EPIC save
    Path(file_path).mkdir(parents=True, exist_ok=True)

    file_name_pattern = f'nasa_epic_{day}.{month}.{year}_'  # for NASA EPIC save
    file_ext = '.png'  # for NASA EPIC save

    numbers_of_file = 0
    for file_number, file_url in enumerate(images_list):
        file_name = f'{file_name_pattern}{file_number + 1}{file_ext}'

        headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
        response = requests.get(file_url, headers=headers, params=payload)
        response.raise_for_status()

        with open(f'{file_path}{file_name}', 'wb') as file:
            file.write(response.content)
            numbers_of_file += 1

    print(f'Скачивание фото Земли от {day}.{month}.{year} завершено. Скачано {numbers_of_file} шт.\n')


if __name__ == '__main__':
    main()
