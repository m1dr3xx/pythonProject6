from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from data import users_data

common = Router()

@common.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer(text='Этот бот демонстрирует работу FSM\n\n'
                              'Чтобы перейти к заполнению анкеты - '
                              'отправьте команду /fillform')



@common.message(Command('show'))
async def handle_show(message: Message, state: FSMContext):
    user = users_data[message.from_user.id]
    name = user["name"]
    age = user["age"]
    is_male = user["is_male"]
    description = user["description"]
    photo_id = user["photo"]

    await message.answer_photo(photo_id,
                               caption=f"Имя: {name}\nВозраст:{age}  лет\nпол: {is_male}\nО себе:{description}")
    await state.clear()
