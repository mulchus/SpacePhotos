from os import path
import requests
from urllib import parse
from datetime import datetime


def save_file(images, file_path, payload=None):
    numbers_of_file = 0
    for file_number, file_url in enumerate(images, start=1):
        file_ext = path.splitext(parse.urlsplit(file_url).path)[1]
        file_name = f'{file_number}{file_ext}'
        response = requests.get(file_url, params=payload)
        response.raise_for_status()

        with open(f'{file_path}{file_name}', 'wb') as file:
            file.write(response.content)
            numbers_of_file += 1
    return numbers_of_file


def format_date(date_in_string):
    date_ = datetime.strptime(date_in_string, "%d.%m.%Y").date()
    return date_, date_.strftime("%Y-%m-%d"), date_.strftime("%Y/%m/%d")
