import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, StateFilter  # Фильтр для /start, /...
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message  # Тип сообщения

from config import config  # Config
from keyboards.menu import menu

from states.form import FormStatesGroup
from handlers import fill_form, common

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(storage=MemoryStorage())  # Менеджер бота

users_data = {}


@dp.message(Command("edit"))
async def edit_command(message: Message, state: FSMContext):
    await message.answer("Что вы хотите изменить?")



async def main():
    dp.include_routers(fill_form.fill_form_router, common.common)
    try:
        print('Bot Started')
        await dp.start_polling(bot)
        await bot.set_my_commands(menu)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
