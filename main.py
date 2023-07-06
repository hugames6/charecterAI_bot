from aiogram.utils import executor
from bot import dispatch
from database.db import sql_start
from bot import storage
from hendler import user

async def on_start(_):
    print('Бот запущен.')
    await sql_start()

async def on_shut(_):
    await storage.close()

user.reg_hendlers_user(dispatch)
executor.start_polling(dispatch, skip_updates=True, on_startup=on_start, on_shutdown=on_shut)
