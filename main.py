import fetch_nasa_epic_images
import fetch_spacex_images
import fetch_nasa_apod_images
import argparse


if __name__ == '__main__':
    while True:
        parser_main = argparse.ArgumentParser(description='Загрузка снимков космоса')
        parser_main.add_argument(
            'source_of_images',
            help='ввод источника снимков космоса: (SpaceX or APOD or EPIC)'
        )

        source_input = parser_main.parse_args().source_of_images
        print(source_input)

        if source_input == 'SpaceX':
            fetch_spacex_images.main()

        elif source_input == 'APOD':
            fetch_nasa_apod_images.main()

        elif source_input == 'EPIC':
            fetch_nasa_epic_images.main()

        else:
            print('Не ясен ответ! Повторите.')
