from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from engine import english_word, transcription_word, russian_word


class FSMAdmin(StatesGroup):
    name = State()


async def cm_start(message: types.Message):
    await FSMAdmin.name.set()
    await message.answer(f'{english_word} {transcription_word}')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text


    async with state.proxy() as data:
        if data['name'] in russian_word:
            await message.answer('ok')
    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['load'], state=None)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
