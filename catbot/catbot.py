# NTUOSS Telegram Bots Workshop
# 22 September 2017
# Speakers: Clarence Castillo & Steve Ye
# Repository: https://github.com/clarencecastillo/NTUOSS-TelegramBotsWorkshop

# ------------------------ WRITE YOUR CODES BELOW THIS LINE ------------------------ #

# import required modules
import time, json, requests, telepot
from telepot.loop import MessageLoop
from cat import Cat
# TODO: Import Keyboards

# TODO: Replace Token
TOKEN = ''

def on_chat_message(msg):
    global cat_bot
    content_type, chat_type, chat_id = telepot.glance(msg)

    # TODO: Create Hello World

def on_callback_query(msg):
    global cat_bot
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    # TODO: Handle Callback Query

    # answer callback query or else telegram will forever wait on this
    bot.answerCallbackQuery(query_id)

# bootstrap the bot and spawn the cat
bot = telepot.Bot(TOKEN)
bot_name = bot.getMe()['first_name']
cat_bot = Cat(bot_name)

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Meow! ' + bot_name + ' at your service...')

# keep the program running
while True: time.sleep(10)

# ------------------------ WRITE YOUR CODES ABOVE THIS LINE ------------------------ #
