from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from create_bot import dp, bot
from engine import english_word, transcription_word, russian_word


async def send(message : types.Message):    
    if message.text == "begin":
        await bot.send_message(message.from_user.id, f'{english_word} {transcription_word}', reply_markup=ReplyKeyboardRemove())
        await message.delete()
    print(message.text)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(send)
