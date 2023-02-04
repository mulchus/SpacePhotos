import telegram
import constants


bot = telegram.Bot(token=constants.bot_token)
print(bot.get_me())

updates = bot.get_updates()
print(updates[0])

bot.send_message(text='Ну вот и новый бот родился!', chat_id=-1001585203348)