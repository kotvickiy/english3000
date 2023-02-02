from aiogram.utils import executor
from create_bot import dp
from handlers import fsm


fsm.register_handlers(dp)

executor.start_polling(dp, skip_updates=True)
