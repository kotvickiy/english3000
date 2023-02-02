from random import shuffle
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State


def lst_word():
    res = []
    with open('words3000.csv', encoding='utf-8', newline='') as file:
        for i in [i for i in file.readlines()]:
            res.append(i.strip().split(','))
    return res


def crop_shuffle_list(x):
    res = lst_word()[x - 1:x + 9]
    shuffle(res)
    return res


class FSM(StatesGroup):
    start_fsm = State()
    num = State()


N = 0
CSL = 0
BAD = []
VAR = 0


async def start_message(message: types.Message):
    await FSM.start_fsm.set()
    await bot.send_message(message.from_user.id, text='Введи число от 1 до 2990')


async def choice(message: types.Message):
    try:
        if not (1 <= int(message.text) <= 2990):
            await bot.send_message(message.from_user.id, text='Введи число от 1 до 2990')
        else:
            global N, CSL
            N = int(message.text)
            CSL = crop_shuffle_list(N)
            await FSM.next()
            await bot.send_message(message.from_user.id, text=f'{CSL[0][0]} {CSL[0][1]}')
    except ValueError:
        await message.answer('Введи число от 1 до 2990')


async def one_fun(message: types.Message):
    global VAR
    if VAR < 10:
        if message.text.replace('Ё', 'е').replace('ё', 'е').lower() not in CSL[VAR][2].replace('Ё', 'е').replace('ё', 'е').split(';'):
            global BAD
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
            await bot.send_message(message.from_user.id, text='Введи число от 1 до 2990')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'], state=None)
    dp.register_message_handler(choice, state=FSM.start_fsm)
    dp.register_message_handler(one_fun, state=FSM.num)
