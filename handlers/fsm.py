from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text

from define import crop_shuffle_list, start_text, error_list


class FSM(StatesGroup):
    start_fsm = State()
    num = State()


N = 0
CSL = 0
BAD = []
VAR = 0
ERR = []
st = start_text()


async def start_message(message: types.Message):
    global BAD, VAR, N, CSL, ERR
    N = 0
    CSL = 0
    BAD = []
    VAR = 0
    ERR = []
    await FSM.start_fsm.set()
    await bot.send_message(message.from_user.id, text=st)


async def choice(message: types.Message):
    global BAD, VAR, N, CSL, ERR
    try:
        if not (1 <= int(message.text.split(' ')[0]) <= 2990):
            await bot.send_message(message.from_user.id, text=st)
        else:
            N = message.text
            CSL = crop_shuffle_list(N)
            await FSM.next()
            await bot.send_message(message.from_user.id, text=f'{len(CSL)}: {CSL[0][0]} {CSL[0][1]}')
    except ValueError:
        await message.answer(st)
        N = 0
        CSL = 0
        BAD = []
        VAR = 0
        ERR = []
        await FSM.start_fsm.set()


async def one_fun(message: types.Message):
    global VAR, BAD, N, CSL, ERR
    if VAR < len(CSL):
        if message.text[0].isdigit():
            N = message.text
            CSL = crop_shuffle_list(N)
            BAD = []
            VAR = 0
            ERR = []
            FSM.num
        elif message.text[0].isalpha() and message.text.replace('Ё', 'е').replace('ё', 'е').lower() not in CSL[VAR][2].replace('Ё', 'е').replace('ё', 'е').split(';'):
            BAD.append(f'{CSL[VAR][0]} => {CSL[VAR][2].replace(";", ",")}  != {message.text}')
            ERR.append(str(CSL[VAR]).replace('[', '').replace(']', '').replace('\'', '').replace(' ', ''))
            VAR += 1
        else:
            VAR += 1
        if VAR != len(CSL):
            FSM.num
            await bot.send_message(message.from_user.id, text=f"{len(CSL) - VAR}: {CSL[VAR][0]} {CSL[VAR][1]}")
        else:
            if BAD:
                error_list(ERR)
                await bot.send_message(message.from_user.id, text=f'W R O N G _ A N S W E R S ({N}):' + '\n' + '_' * 27 + '\n' + "\n".join(str(x) for x in BAD) + '\n' + '_' * 27)
                BAD = []
                ERR = []
                VAR = 0
            else:
                await bot.send_message(message.from_user.id, text=f'👍Красавчик({N})👍'.upper())
                VAR = 0
            await FSM.start_fsm.set()
            await bot.send_message(message.from_user.id, text=st)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'], state='*')
    dp.register_message_handler(start_message, Text(equals='/start', ignore_case=True), state='*')
    dp.register_message_handler(choice, state=FSM.start_fsm)
    dp.register_message_handler(one_fun, state=FSM.num)
