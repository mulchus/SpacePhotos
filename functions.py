from os import path
import requests
from urllib import parse
import os


def file_save(images_list, file_path, file_name_pattern, payload=''):
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


def path_of_files(start_dir):  # make a list of paths for all files in start directory
    file_paths = []
    for folder, _, files in os.walk(start_dir):
        for filename in files:
            file_paths.append(os.path.abspath(os.path.join(folder, filename)))
    return file_paths


def path_of_files_in_dir(directory):  # make a list of paths for all files in directory
    # onlyfiles = []
    # for (dirpath, dirnames, filenames) in os.walk(directory):
    #     for filename in filenames:
    #         onlyfiles.append(f'{directory}{filename}')

    onlyfiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return onlyfiles


def main():
    # print(path_of_files(f'{path.dirname(__file__)}/Images/'))
    print(path_of_files_in_dir(f'{path.dirname(__file__)}/Images/SpaceX'))
    print(os.listdir(f'{path.dirname(__file__)}/Images/NASA'))


if __name__ == '__main__':
    main()
