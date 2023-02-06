import telegram
import constants


bot = telegram.Bot(token=constants.telegram_bot_token)


def bot_send_photo(tchat_id, path_to_file):
    bot.send_photo(tchat_id, photo=open(path_to_file, 'rb'))
    return
