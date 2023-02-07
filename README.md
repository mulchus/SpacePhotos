# SpacePhotos

1. The project is designed to download photos of space using the SpaceX API of Elon Musk and the NASA website, 
and their publications on the Telegram channel
2. The project publishes in the Telegram channel photos from a given directory with a given frequency or a 
specifically selected photo


### How to install?

Python3 should already be installed.
Then use pip (or pip3, there is a conflict with Python2) to install dependencies.
Open the command line with the Win+R keys and enter:
```
pip install -r requirements.txt
```
It is recommended to use virtualenv/venv to isolate the project.
(https://docs.python.org/3/library/venv.html)


### Setting environment variables

Before starting, you need to create a file ".env" in PATH_TO_THE_FOLDER_WITH_SCRIPT\ 
and configure the environment variables by writing in it:
```
NASA_API_KEY=Your API_KEY
```
received on the site
``
https://api.nasa.gov/#apod

```
TELEGRAM_BOT_TOKEN=Your bot token
```
received in Telegram using @BotFather
```
https://way23.ru/регистрация-бота-в-telegram.html
```
```
CHAT_ID - ID of your Telegram chanel or supergroup
```
How to know? See in 
```
https://101info.ru/kak-uznat-id-kanala-telegram/#ID_канала
```
```
SPECIAL_PAUSE=14400 - A special pause, set in seconds (14400)
```
is applied according to the task when publishing images on the channel


### The command to run the script:
```
python PATH_TO_THE_FOLDER_WITH_SCRIPT\...
```
If you have installed a virtual environment, then the command can be entered without the path to the script
Scripts for downloading photos work separately.
The commands to run them have the following format:
```
python PATH_TO_THE_FOLDER_WITH_SCRIPT\fetch_spacex_images.py [-h] [id]
```
**_fetch_spacex_images.py_** - uploading all photos from the entered SpaceX launch code (by default, the last launch).
Files are saved in the PATH_TO_THE_FOLDER_WITH_SCRIPT/Images/SpaceX/

```
python PATH_TO_THE_FOLDER_WITH_SCRIPT\fetch_nasa_epic_images.py [-h] [date_image]
```
**_fetch_nasa_apod_images.py_** - uploading a photo of the Earth from NASA EPIC by the entered date 
- in the format DD.MM.YYYY (by default - the current date);
Files are saved in the PATH_TO_THE_FOLDER_WITH_SCRIPT/Images/NASA/EPIC/

```
python PATH_TO_THE_FOLDER_WITH_SCRIPT\fetch_nasa_apod_images.py [-h] [start_date] [end_date]
```
**_fetch_nasa_apod_images.py_** - uploading photos from NASA APOD by entered dates from- to-
- start_date - start date in DD.MM.YYYY format (by default - current date);
- end_date - the end date in the format DD.MM.YYYY (by default - the current date);

```
python PATH_TO_THE_FOLDER_WITH_SCRIPT\image_time_post.py [-h] [directory] [pause]
```
**_image_time_post.py_** - a script for publishing photos. Publishes all photos from a given directory every few
hours (1 hour = 3600 sec). 
When all the photos from the directory are published, he begins to publish them again, shuffling the photos 
in random order.
But there is one caveat :)
- by default, the delay is set to 4 hours;
- if you set the publication every 4 hours, the photos will be published once every 4 hours.
The delay is set in the script launch line.
- directory - location of photos (full path);
- pause - the delay between publications in seconds.
A special pause is set in seconds (14400) in the ".env" file.
```
python PATH_TO_THE_FOLDER_WITH_SCRIPT\specified_photo_post.py [-h] [directory]
```
**_specified_photo_post.py_** - a script to publish a photo on a specific path. If the file is not found, a random 
photo is published from all available photos (folder tree, starting with PATH_TO_THE_FOLDER_WITH_SCRIPT\Image\)


### Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org]
(https://dvmn.org/).



# SpacePhotos (фотографии космоса)

1. Проект предназначен для скачивания фотографий космоса по API SpaceX Илона Маска и сайта NASA, а также их публикаций 
на канале Telegram
2. Проект публикует в Telegram-канале фотографии из заданной директории с заданной периодичностью или конкретно 
выбранной фотографии  


### Как установить?

Python3 должен быть уже установлен. 
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей.
Открываем командную строку клавишами Win+R и вводим:
```
pip install -r requirements.txt
```
Рекомендуется использовать virtualenv/venv для изоляции проекта.
(https://docs.python.org/3/library/venv.html)


### Настройка переменных окружения

До запуска необходимо создать файл ".env" в папке ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\
и настроить переменные окружения, прописав в нем:
```
NASA_API_KEY=Ваш API_KEY
```
полученный на сайте
```
https://api.nasa.gov/#apod
```
```
TELEGRAM_BOT_TOKEN=токен Вашего бота
```
полученный в Telegram с помощью @BotFather 
```
https://way23.ru/регистрация-бота-в-telegram.html
```
```
CHAT_ID - ID вашего Telegram канала или чата
```
Как узнать? Смотрите в 
```
https://101info.ru/kak-uznat-id-kanala-telegram/#ID_канала
```
```
SPECIAL_PAUSE=14400 - Специальная пауза, задается в секундах (14400)
```
применяется согласно заданию при публикации изображений на канале


### Команда на запуск скрипта:
```
python ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\...
```
Если вы установили виртуальное окружение, то команду можно вводить без пути к скрипту
Скрипты по скачиванию фотографий работают по отдельности.
Команды на их запуск имеют следующий формат:
```
python ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\fetch_spacex_images.py [-h] [id] 
```
**_fetch_spacex_images.py_** - загрузка всех фото из введенного кода запуска SpaceX (по умолчанию - последний запуск).
Файлы сохраняются в ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ/Images/SpaceX/

```
python ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\fetch_nasa_epic_images.py [-h] [date_image]
```
**_fetch_nasa_apod_images.py_** - загрузка фото Земли из NASA EPIC по введенной дате в формате ДД.ММ.ГГГГ 
(по умолчанию - текущая дата);
Файлы сохраняются в ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ/Images/NASA/EPIC/

```
python ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\fetch_nasa_apod_images.py [-h] [start_date] [end_date]
```
**_fetch_nasa_apod_images.py_** - загрузка фото из NASA APOD по введенным датам с- по-
- start_date - начальная дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата);
- end_date - конечная дата в формате ДД.ММ.ГГГГ (по умолчанию - текущая дата);

```
python ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\image_time_post.py [-h] [directory] [pause]
```
**_image_time_post.py_** - скрипт публикации фотографий. Публикует все фотографии из заданной директории раз в несколько 
часов (1 час = 3600 сек).
Когда все фото из директории опубликованы – он начинает публиковать их заново, перемешав фото в случайном порядке.
Но есть один нюанс :)
- по умолчанию задержка выставлена в 4 часа;
- если задать публикацию раз в 4 часа – фото будут публиковаться по одному раз в 4 часа.
Задержка задается в строке запуска скрипта.
- directory - местоположение фотографий (полный путь);
- pause - задержка между публикациями в секундах.
Специальная пауза задается в секундах (14400) в файлe ".env".

```
python PATH_TO_THE_FOLDER_WITH_SCRIPT\specified_photo_post.py [-h] [directory]
```
**_specified_photo_post.py_** - скрипт для публикации фото по конкретному пути. Если файл не найден - публикуется 
случайное фото из всех имеющихся фотографий (дерево папок, начиная с PATH_TO_THE_FOLDER_WITH_SCRIPT\Image\)


### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

