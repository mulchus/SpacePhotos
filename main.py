import requests
from pathlib import Path


def get_image(urloffile, pathoffile):
    Path(pathoffile).mkdir(parents=True, exist_ok=True)
    file_name = urloffile.split('/')[-1]

    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
    response = requests.get(urloffile, headers=headers)
    response.raise_for_status()

    with open(f'{pathoffile}{file_name}', 'wb') as file:
        file.write(response.content)


def takespaceximagelist(urloffile):
    response = requests.get(urloffile)
    response.raise_for_status()

    latestimageslist = response.json()['links']['flickr']['original']
    if latestimageslist:
        return latestimageslist
    else:
        urloffileall = (urloffile.replace('latest', 'past')) # past по API выдает все предыдущие запуски
        response = requests.get(urloffileall)
        response.raise_for_status()

        # формирование списка фото всех запусков, если их нет в последнем
        imagelist = []
        for spacexrecord in response.json():
            if spacexrecord['links']['flickr']['original']:
                imagelist.extend(spacexrecord['links']['flickr']['original'])
        return imagelist


if __name__ == '__main__':
    # file_path = './Images/123/'  # first symbol is '.' if path is project directory continuation
    # file_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    file_path = './Images/SpaceX/'
    file_url = 'https://api.spacexdata.com/v5/launches/latest'
    spaceximagelist =takespaceximagelist(file_url)

    for file_url in spaceximagelist[:3]:
        get_image(file_url, file_path)
