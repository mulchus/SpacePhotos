import requests
from pathlib import Path
from os import path
from urllib import parse
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")

    year, month, day = input('Введите дату фото Земли (в формате ГГГГ-ММ-ДД): ').split('-')  # date of fotos
    payload = {'api_key': nasa_api_key}
    # payload = {'api_key': '7ye1VhDS57wEwOOyxrz0YfNUYnkPRrOk8VjbSEg6'}
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

    file_path = './Images/NASA/EPIC/'  # for NASA EPIC save
    Path(file_path).mkdir(parents=True, exist_ok=True)

    file_name_pattern = 'nasa_epic_'  # for NASA EPIC save
    file_ext = '.png'  # for NASA EPIC save

    for file_number, file_url in enumerate(images_list):
        file_name = f'{file_name_pattern}{file_number + 1}{file_ext}'

        headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
        response = requests.get(file_url, headers=headers, params=payload)
        response.raise_for_status()

        with open(f'{file_path}{file_name}', 'wb') as file:
            file.write(response.content)

    print(f'Скачивание фото Земли от {day}.{month}.{year} завершено\n')