# NTUOSS Telegram Bots Workshop
# 22 September 2017
# Speakers: Clarence Castillo & Steve Ye
# Repository: https://github.com/clarencecastillo/NTUOSS-TelegramBotsWorkshop

# ------------------------ WRITE YOUR CODES BELOW THIS LINE ------------------------ #

import time
import requests
import random
import random
from bs4 import BeautifulSoup

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.delegate import pave_event_space, per_chat_id, create_open

from cat import Cat


eng_badlist = ['Hitler', 'Donald Trump', 'human suffering', 'dogs', 'rats', 'insurance fraud', 'the police']
ger_badlist = ['Hitler', 'Donald Trump', 'diktaturen', 'hund', 'ratten', 'versicherungsbetrug']
spa_badlist = ['Hitler', 'Donald Trump', 'muerte', 'perros', 'ratas', 'fraude de seguro', 'los policia']

eng_mehlist = ['homeless people', 'true love', 'pants', 'rain', 'vegans', 'Swedish people']
ger_mehlist = ['liebe', 'Donald Trump', 'ein schone frau', 'dogs', 'rats', 'insurance fraud']
spa_mehlist = ['amor', 'veganos', 'pantalones', 'dogs', 'illuvia', 'carteles de drogas']

eng_goodlist = ['cats', 'the Simpsons', 'flamingoes', 'drug money', 'fire', 'death', 'Tom Cruise', 'burritos']
ger_goodlist = ['weiss bier', 'der Simpsons', 'sorgfaltig gefertigte witze', 'fussball', 'schnitzel', 'feuer', 'Tom Cruise']
spa_goodlist = ['gato', 'pollos', 'fuego', 'el jefe', 'flamencos', 'biblioteca', 'los Simpsons', 'Tom Cruise']

englist = [eng_goodlist,eng_mehlist,eng_badlist]
spalist = [spa_goodlist,spa_mehlist,spa_badlist]
gerlist = [ger_goodlist,ger_mehlist,ger_badlist]

eng_prompt = ["Very good! Let's see... What do you think of ",
                "Excellent. Now, what do you say about ",
                "That is well. Come, let's hear your thoughts on ",
                "Indeed. May I ask for your opinion on "]
spa_prompt = ["Salud! Que piensas de ",
                "Buenos dias! Quiero tu opinion sobre ",
                "Que bueno oirlo! Cuales son tus pensamientos sobre ",
                "Y lo que piensas sobre "]
ger_prompt = ["Und was du denkst uber ",
                "Guten tag! Ich mochte deine Meinung zu ",
                "Bitte, ich möchte deine Gedanken hören ",
                "Jetzt, was sagst du über "]

eng_goodresp = ["Impeccable",
                "Couldn't say it better meself.",
                "That's right!",
                "Yes, I have finally found someone who thinks the way I do.",
                "Couldn't agree more.",
                "My whiskers are twitching in vehemont agreement."]
ger_goodresp = ["Ach, das ist gut.",
                "Ja, das ist richtig,"
                "Mein gott! Ich zustimmen.",
                "Du sprichst die Wahrheit."]
spa_goodresp = ["Oh, eso es bueno,"
                "Sí, eso es correcto"
                "Dios mío, estoy de acuerdo.",
                "Hablas la verdad."]

eng_badresp = ["You disgust me.",
                "Now even I wouldn't stoop so low",
                "You disappoint me.",
                "If I had never felt shame before, I'm sure I do now.",
                "You're a SOB."
                "You're a POS."
                ]
ger_badresp = ["Du widerst mich an.",
                 "Jetzt würde ich auch nicht so tief bücken",
                 "Du enttäuschst mich.",
                 "Wenn ich noch nie Schande gehabt hätte, bin ich mir sicher, dass ich es jetzt mache.",
                 "Du bist ein hurensohn."
                 "Du bist scheisse."
                 ]
spa_badresp = ["Me das asco.",
                 "Ahora ni siquiera me inclinaría tan bajo",
                 "Me decepcionas.",
                 "Si nunca antes había sentido vergüenza, estoy seguro de que lo haré ahora.",
                 "Eres un hijo de puta."
                 "Eres un cagada."
                 ]

class MessageCounter(telepot.helper.ChatHandler):


   def __init__(self, *args, **kwargs):
      super(MessageCounter, self).__init__(*args, **kwargs)
      self.state = 0
      self.language = ''
      self.feel = 0
      self.ans = 0


   # TODO: Paste functions here (make sure the indentations are right)
   #-------------- Insert catboy functions in between ---------------#
   def get_random_cat_fact(self):
      return

   def get_random_cat_image_url(self):
      return

   def on_chat_message(self, msg):
      return

   def on_callback_query(self, msg):
      return
   #-----------------------------------------------------------------#


# TODO: Insert own API token here
TOKEN = ''
bot = telepot.DelegatorBot(TOKEN,
                           [pave_event_space()
                            (per_chat_id(),
                             create_open,
                             MessageCounter,
                             timeout=100),])



bot_name = bot.getMe()['first_name']
cat_bot = Cat(bot_name)

MessageLoop(bot).run_as_thread()

print('Meow! ' + bot_name + ' at your service...')

# keep the program running and simulate cat life
cat_last_update = time.time()
while True:
    print('yes')
    time.sleep(10)
    # update cat every 6 hours
    if (time.time() - cat_last_update > 24/4*60*60):
        cat_bot.on_update()
        cat_last_update = time.time()
