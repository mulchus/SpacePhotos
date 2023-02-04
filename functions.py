from pathlib import Path
from os import path
import requests
from urllib import parse


def file_save(images_list, file_path, file_name_pattern, payload):
    numbers_of_file = 0
    for file_number, file_url in enumerate(images_list):
        file_ext = path.splitext(parse.urlsplit(file_url).path)[1]
        file_name = f'{file_name_pattern}{file_number + 1}{file_ext}'

        headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
        response = requests.get(file_url, headers=headers, params=payload)
        response.raise_for_status()

        with open(f'{file_path}{file_name}', 'wb') as file:
            file.write(response.content)
            numbers_of_file += 1

    return numbers_of_file