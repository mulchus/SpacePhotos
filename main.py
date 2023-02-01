import requests
from pathlib import Path


if __name__ == '__main__':

    directory = './Images/123'
    Path(directory).mkdir(parents=True, exist_ok=True)
    filename = f'{directory}/hubble.jpeg'

    headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)
