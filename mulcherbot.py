import telegram
import constants


bot = telegram.Bot(token=constants.bot_token)
# print(bot.get_me())

updates = bot.get_updates()
print(updates[-1])

# bot.send_message(text='Ну вот и новый бот родился!', chat_id=-1001585203348)

# bot.send_photo(chat_id=-1001778853657, photo=open(f'{constants.work_dir}/Images/SpaceX/spacex_5.jpg', 'rb'))
bot.send_photo(chat_id=-1001778853657, photo=open(f'{constants.work_dir}/Images/SpaceX/spacex_5.jpg', 'rb'))