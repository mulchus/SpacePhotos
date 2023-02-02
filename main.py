import requests
from pathlib import Path


def get_image(urloffile, pathoffile, filename=''):
    Path(pathoffile).mkdir(parents=True, exist_ok=True)
    if not filename:
        filename = urloffile.rsplit('/', 1)[-1]
        print(filename)

    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
    response = requests.get(urloffile, headers=headers)
    response.raise_for_status()

    with open(f'{pathoffile}{filename}', 'wb') as file:
        file.write(response.content)


def takespaceximagelist(urloffile):
    response = requests.get(urloffile)
    response.raise_for_status()

    latestimageslist = response.json()['links']['flickr']['original']
    if latestimageslist:
        return latestimageslist
    else:
        urloffileall = (urloffile.replace('latest', 'past'))  # 'past' outputs all previous launches
        response = requests.get(urloffileall)
        response.raise_for_status()

        # generating a list of photos of all launches, if they are not in the last one
        imagelist = []
        for spacexrecord in response.json():
            if spacexrecord['links']['flickr']['original']:
                imagelist.extend(spacexrecord['links']['flickr']['original'])
        return imagelist


if __name__ == '__main__':
    # file_path = './Images/123/'  # first symbol is '.' if path is project directory continuation
    # file_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

    all_files_url = 'https://api.spacexdata.com/v5/launches/latest'
    spaceximagelist = takespaceximagelist(all_files_url)

    print(len(spaceximagelist))
    firstimage = 100  # from the number of which image we download
    numberimages = 5  # number of downloaded images

    file_path = './Images/SpaceX/'
    file_name = 'spacex'
    # file_name = file_url.split('/')[-1]
    for file_number, file_url in enumerate(spaceximagelist[firstimage-1:firstimage-1+numberimages]):
        file_name = f'spacex_{file_number}.jpg'
        get_image(file_url, file_path, file_name)
