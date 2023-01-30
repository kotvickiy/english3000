from aiogram import types, Dispatcher
from create_bot import dp, bot


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'TEST')
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_start, commands=['test'])
