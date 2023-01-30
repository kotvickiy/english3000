from aiogram import types, Dispatcher
from create_bot import dp, bot


async def send(message : types.Message):    
    if message.text == "menu":
        await bot.send_message(message.from_user.id, "menu, please!")
        await message.delete()
    elif message.text == "Stop lesson":
        await bot.send_message(message.from_user.id, "lesson is stop!")
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(send)
