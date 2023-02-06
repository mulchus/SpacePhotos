import requests
from pathlib import Path
from os import path
import argparse
import datetime
import functions
import constants
from dotenv import load_dotenv


parser_epic = argparse.ArgumentParser(description='Загрузка фото Земли из NASA EPIC по введенной дате')
parser_epic.add_argument(
    'date_image',
    nargs='?',
    default=datetime.datetime.today().strftime('%d.%m.%Y'),
    help='дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата)'
)

try:
    print(datetime.datetime.strptime(parser_epic.parse_args().date_image, "%d.%m.%Y").date())
except ValueError:
    print('Неверно введена дата')
    exit()

date = datetime.datetime.strptime(parser_epic.parse_args().date_image, "%d.%m.%Y").date()
payload = {'api_key': constants.nasa_api_key}
all_images_url = f'https://api.nasa.gov/EPIC/api/natural/date/{date.strftime("%Y-%m-%d")}'
response = requests.get(all_images_url, params=payload)
response.raise_for_status()

# generating a list of all id of images
idimages = []
for nasa_record in response.json():
    if nasa_record['image']:
        idimages.append(nasa_record['image'])

images = []
for idimage in idimages:
    images.append(f'https://api.nasa.gov/EPIC/archive/natural/{date.strftime("%Y/%m/%d")}/png/{idimage}.png')

year, month, day = date.strftime("%Y/%m/%d").split('/')
file_path = f'{path.dirname(__file__)}/Images/NASA/EPIC/'
Path(file_path).mkdir(parents=True, exist_ok=True)
file_name_pattern = f'nasa_epic_{day}.{month}.{year}_'

numbers_of_file = functions.file_save(images, file_path, file_name_pattern, payload)

print(f'Скачивание фото Земли от {day}.{month}.{year} завершено. Скачано {numbers_of_file} шт.\n')


if __name__ == '__main__':
    load_dotenv()
