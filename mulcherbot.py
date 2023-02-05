import telegram
import constants


bot = telegram.Bot(token=constants.bot_token)


def last_chat_id():
    return bot.get_updates()[-1]['message']['chat']['id']


def last_update():
    return bot.get_updates()[-1]

# print(bot.get_me())
# updates = bot.get_updates()
# print(updates[-1])


def bot_send_message(message, tchat_id):
    bot.send_message(text=message, chat_id=tchat_id)
    return

# bot.send_message(text='Ну вот и новый бот родился!', chat_id=-1001585203348)

# bot.send_document(chat_id=-1001778853657, photo=open(f'{constants.work_dir}/Images/SpaceX/spacex_5.jpg', 'rb'))


def bot_send_photo(tchat_id, path_to_file):
    bot.send_photo(tchat_id, photo=open(path_to_file, 'rb'))
    return


def main():
    last_chat_id()


if __name__ == '__main__':
    main()
