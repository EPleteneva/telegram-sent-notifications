#!/usr/bin/env python
# coding: utf-8
import telepot
import requests

token = '1271969217:AAHewbJIBDTqUhTaxBva6T1ll3qAYIcw8wI'
bot = telepot.Bot(token)


def send_message(chat_id, message, value=""):
    if value !="":
        bot.sendMessage(chat_id, message + str(value))
    else:
        bot.sendMessage(chat_id, message)
    bot.sendPhoto(chat_id=chat_id, photo=get_url())


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
