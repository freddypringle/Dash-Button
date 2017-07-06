import time
import telegram
import requests

from dbhelper import DBHelper
db = DBHelper()
db.setup()

TOKEN = '317000733:AAG0mpZwVgGMwHeMrwqxQ5Te6Cwdmvct17w'
bot = telegram.Bot(token=TOKEN)

from telegram.ext import Updater
updater=Updater(token=TOKEN)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    return reply_markup

def start(bot,update):
    bot.sendMessage(chat_id =update.message.chat_id, text = "I'm a bot, please talk to me!")

def done(bot,update):
    items = db.get_items()
    keyboard = build_keyboard(items)
    bot.sendMessage(chat_id=update.message.chat_id, text = "Select an item to delete", reply_markup=keyboard)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
done_handler = CommandHandler('done', done)
dispatcher.add_handler(done_handler)

def todo(bot,update):
    text = update.message.text
    items = db.get_items()
    if text in items:
        db.delete_item(text)
        items = db.get_items()
    else:
        db.add_item(text)
        items = db.get_items()
    message = "\n".join(items)
    bot.sendMessage(chat_id=update.message.chat_id, text=message)
    


from telegram.ext import MessageHandler, Filters
todo_handler = MessageHandler(Filters.text, todo)
dispatcher.add_handler(todo_handler)

updater.start_polling()