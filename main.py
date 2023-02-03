import os
from dotenv import load_dotenv
import fetch_nasa_epic_images
import fetch_spacex_images
import fetch_nasa_apod_images


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")

    while True:
        image_type = input('Какие фото скачиваем? (SpaceX or APOD or EPIC): ')

        if image_type == 'SpaceX':
            fetch_spacex_images.main()

        elif image_type == 'APOD':
            fetch_nasa_apod_images.main()

        elif image_type == 'EPIC':
            fetch_nasa_epic_images.main()

        else:
            print('Не ясен ответ! Повторите.')
