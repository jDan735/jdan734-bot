import logging
import sqlite3
import json

from os import environ
from datetime import datetime
from aiogram import Bot, Dispatcher


if "TOKEN" in environ:
    TOKEN = environ["TOKEN"]
    heroku = True

else:
    with open("token.json") as file:
        token = json.loads(file.read())
        TOKEN = token["token"]

        conn = sqlite3.connect("jdanbot.db")

        try:
            bot_status = token["status"]
        except KeyError:
            print("Enter status of bot in token.json")
            bot_status = "unknown"

        heroku = False

start_time = datetime.now()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
