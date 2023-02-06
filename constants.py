import os
from dotenv import load_dotenv
from os import path


load_dotenv()
pause_beetwen_posts = 14400  # pause for post images in chanel
work_dir = path.dirname(__file__)

telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
nasa_api_key = os.environ.get('NASA_API_KEY')
chat_id = os.environ.get('CHAT_ID')
