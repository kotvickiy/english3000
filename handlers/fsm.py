from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text

from define import crop_shuffle_list, start_text


class FSM(StatesGroup):
    start_fsm = State()
    num = State()


N = 0
CSL = 0
BAD = []
VAR = 0
st = start_text()


async def start_message(message: types.Message):
    global BAD, VAR, N, CSL
    N = 0
    CSL = 0
    BAD = []
    VAR = 0
    await FSM.start_fsm.set()
    await bot.send_message(message.from_user.id, text=st)


async def choice(message: types.Message):
    global BAD, VAR, N, CSL
    try:
        if not (1 <= int(message.text) <= 2990):
            await bot.send_message(message.from_user.id, text=st)
        else:
            N = int(message.text)
            CSL = crop_shuffle_list(N)
            await FSM.next()
            await bot.send_message(message.from_user.id, text=f'{CSL[0][0]} {CSL[0][1]}')
    except ValueError:
        await message.answer(st)
        N = 0
        CSL = 0
        BAD = []
        VAR = 0
        await FSM.start_fsm.set()


async def one_fun(message: types.Message):
    global VAR, BAD, N, CSL
    if VAR < 10:
        if message.text.isdigit():
            N = int(message.text)
            CSL = crop_shuffle_list(N)
            BAD = []
            VAR = 0
            FSM.num
        elif message.text[0].isalpha() and message.text.replace('Ё', 'е').replace('ё', 'е').lower() not in CSL[VAR][2].replace('Ё', 'е').replace('ё', 'е').split(';'):
            BAD.append(f'{CSL[VAR][0]} => {CSL[VAR][2].replace(";", ",")}')
            VAR += 1
        else:
            VAR += 1
        if VAR != 10:
            FSM.num
            await bot.send_message(message.from_user.id, text=f"{CSL[VAR][0]} {CSL[VAR][1]}")
        else:
            if BAD:
                await bot.send_message(message.from_user.id, text='W R O N G _ A N S W E R S :' + '\n' + '_' * 27 + '\n' + "\n".join(str(x) for x in BAD) + '\n' + '_' * 27)
                BAD = []
                VAR = 0
            else:
                await bot.send_message(message.from_user.id, text='👍Красавчик!👍'.upper())
                VAR = 0
            await FSM.start_fsm.set()
            await bot.send_message(message.from_user.id, text=st)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'], state='*')
    dp.register_message_handler(start_message, Text(equals='/start', ignore_case=True), state='*')
    dp.register_message_handler(choice, state=FSM.start_fsm)
    dp.register_message_handler(one_fun, state=FSM.num)
