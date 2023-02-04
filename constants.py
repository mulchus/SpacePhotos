from dotenv import load_dotenv
import os
from os import path


load_dotenv()
nasa_api_key = os.getenv('NASA_API_KEY')
bot_token = os.getenv('MULCHERBOT')

chat_id = -1001778853657

work_dir = path.dirname(__file__)

pause_beetwen_posts = 14400  # pause for post images in chanel
