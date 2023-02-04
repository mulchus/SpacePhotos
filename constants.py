from dotenv import load_dotenv
import os
from os import path


load_dotenv()
nasa_api_key = os.getenv('NASA_API_KEY')
bot_token = os.getenv('MULCHERBOT')

work_dir = path.dirname(__file__)
