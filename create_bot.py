from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()


bot = Bot(token='6092563373:AAHKxGF_GJ911SLecbRth2-grEfbdhYMehM')
dp = Dispatcher(bot, storage=storage)
