from os import path
import requests
from urllib import parse
import os
from datetime import datetime


def save_file(images, file_path, payload=''):
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


def get_paths_of_files(start_dir):  # make a list of paths for all files in start directory
    file_paths = []
    for folder, _, files in os.walk(start_dir):
        for filename in files:
            file_paths.append(os.path.abspath(os.path.join(folder, filename)))
    return file_paths


def format_date(date_in_string):
    date_ = datetime.strptime(date_in_string, "%d.%m.%Y").date()
    return date_, date_.strftime("%Y-%m-%d"), date_.strftime("%Y/%m/%d")
