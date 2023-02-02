import requests
from pathlib import Path
from os import path
# import os
from urllib import parse


def get_image(urloffile, pathoffile, filename=''):

    Path(pathoffile).mkdir(parents=True, exist_ok=True)

    if not filename:
        filename = parse.unquote(path.split(parse.urlsplit(urloffile).path)[1])

    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
    response = requests.get(urloffile, headers=headers)
    response.raise_for_status()

    with open(f'{pathoffile}{filename}', 'wb') as file:
        file.write(response.content)


def takespaceximagelist(urltojson):
    response = requests.get(urltojson)
    response.raise_for_status()

    latestimageslist = response.json()['links']['flickr']['original']
    if latestimageslist:
        return latestimageslist
    else:
        urlofjsonall = (urltojson.replace('latest', 'past'))  # 'past' outputs all previous launches
        response = requests.get(urlofjsonall)
        response.raise_for_status()

        # generating a list of photos of all launches, if they are not in the last one
        image_list = []
        for spacexrecord in response.json():
            if spacexrecord['links']['flickr']['original']:
                image_list.extend(spacexrecord['links']['flickr']['original'])
        return image_list


def takenasaimagelist(urltodict, payloads):
    response = requests.get(urltodict, params=payloads)
    response.raise_for_status()

    # generating a list of all image
    image_list = []
    for nasarecord in response.json():
        if nasarecord['url']:
            image_list.append(nasarecord['url'])
    return image_list


def ext_extract(file_url_):
    return path.splitext(parse.urlsplit(file_url_).path)[1]


if __name__ == '__main__':
    # file_path = './Images/123/'  # first symbol is '.' if path is project directory continuation
    # file_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

    # file_path = './Images/SpaceX/'
    # file_url = 'https://example.com/txt/hello%20world.txt?v=9#python'
    # get_image(file_url, file_path )
    # exit()

    # all_files_url = 'https://api.spacexdata.com/v5/launches/latest'
    # spaceximagelist = takespaceximagelist(all_files_url)

    nasaapikey = '7ye1VhDS57wEwOOyxrz0YfNUYnkPRrOk8VjbSEg6'
    payload = {'api_key': f'{nasaapikey}', 'start_date': '2023-01-01', 'end_date': ''}
    all_files_url = f'https://api.nasa.gov/planetary/apod'
    imagelist = takenasaimagelist(all_files_url, payload)

    firstimage = 0  # from the number of which image we download (0 - first)
    numberimages = 15  # number of downloaded images

    # file_path = './Images/SpaceX/'  # first symbol is '.' if path is project directory continuation
    # file_name_pattern = 'spacex_'
    file_path = './Images/NASA/'
    file_name_pattern = 'nasa_apod_'

    for file_number, file_url in enumerate(imagelist[firstimage:firstimage+numberimages]):
        file_ext = ext_extract(file_url)
        file_name = f'{file_name_pattern}{file_number+1}{file_ext}'
        print(file_ext)
        print(file_name)
        get_image(file_url, file_path, file_name)
