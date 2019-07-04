from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re

token = '853282382:AAE2hBA9OwU9kkPSq6RpTmpQLRGoETJiui0'

def get_url():
    # contents = requests.get('https://random.dog/woof.json').json()    
    # url = contents['url']
    contents = requests.get('http://aws.random.cat/meow').json()    
    url = contents['file']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def sendMsg(bot, update):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id, text='HI Man')

def main():
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("hi", sendMsg))
    dp.add_handler(MessageHandler(Filters.text,bop))

    updater.start_polling()
    updater.idle()

main()
# if __name__ == '__main__':
#     main()
