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


if __name__ == '__main__':
    file_path = './Images/123/'  # first symbol is '.' if path is project directory continuation
    file_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    get_image(file_url, file_path)
