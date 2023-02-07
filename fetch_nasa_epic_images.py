import requests
from pathlib import Path
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

Path(Path.cwd() / 'Images' / 'NASA' / 'EPIC').mkdir(parents=True, exist_ok=True)
file_path = Path.cwd() / 'Images' / 'NASA' / 'EPIC' / f'nasa_epic_{day}.{month}.{year}_'

numbers_of_file = functions.file_save(images, file_path, payload)

print(f'Скачивание фото Земли от {day}.{month}.{year} завершено. Скачано {numbers_of_file} шт.\n')


if __name__ == '__main__':
    load_dotenv()
