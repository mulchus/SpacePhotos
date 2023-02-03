import requests
from pathlib import Path
from os import path
from urllib import parse
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")

    start_date = input('С какой даты выгружать? (в формате ГГГГ-ММ-ДД): ')
    end_date = input('По какую дату выгружать? (в формате ГГГГ-ММ-ДД, без даты - это сегодня): ')
    payload = {'api_key': nasa_api_key, 'start_date': start_date, 'end_date': end_date, }
    all_files_url = 'https://api.nasa.gov/planetary/apod'

    response = requests.get(all_files_url, params=payload)
    response.raise_for_status()

    images_list = []  # generating a list of all image
    for nasa_record in response.json():
        if nasa_record['url']:
            images_list.append(nasa_record['url'])

    file_path = './Images/NASA/APOD/'  # for NASA APOD save
    Path(file_path).mkdir(parents=True, exist_ok=True)

    file_name_pattern = 'nasa_apod_'  # for NASA APOD save

    for file_number, file_url in enumerate(images_list):
        file_ext = path.splitext(parse.urlsplit(file_url).path)[1]
        file_name = f'{file_name_pattern}{file_number + 1}{file_ext}'

        headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
        response = requests.get(file_url, headers=headers, params=payload)
        response.raise_for_status()

        with open(f'{file_path}{file_name}', 'wb') as file:
            file.write(response.content)

    print(f'Скачивание фото с {start_date} по.{end_date} завершено\n')