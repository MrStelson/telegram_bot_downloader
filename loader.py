from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.bot.api import TelegramAPIServer
from dotenv import load_dotenv, find_dotenv

import os

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')

local_server = TelegramAPIServer.from_base('http://127.0.0.1:80')

# bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML, server=local_server)
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
