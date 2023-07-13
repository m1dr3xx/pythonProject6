from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.edit import EditStatesGroup

edits = Router()



@edits.message(Command("edit"))
async def handle_edit(message:Message, state: FSMContext):
    await message.answer("Что вы хотите изменить?")




@edits.message(StateFilter(EditStatesGroup.edit_name))
async def handle_edit_name(message: Message, state: FSMContext):
    name_from_message = message.text
    await state.update_data(name=name_from_message)
    await message.answer('Хорошо. Напишите свое новое имя')



@edits.message(StateFilter(EditStatesGroup.edit_age))
async def handle_get_age(message: Message, state: FSMContext):
    age_from_message = message.text
    if age_from_message.isdigit() and 1 <= int(age_from_message) <= 120:
        await state.update_data(age=age_from_message)
        await message.answer('А теперь укажите свой пол')



@edits.message(StateFilter(EditStatesGroup.edit_gender))
async def handle_get_gender(message: Message, state: FSMContext):
    gender_from_message = message.text
    await state.update_data(gender=gender_from_message)
    await message.answer('Теперь напишите пару слов о себе')



@edits.message(StateFilter(EditStatesGroup.edit_description))
async def handle_get_description(message: Message, state: FSMContext):
    description_from_message = message.text
    await state.update_data(description=description_from_message)
    await message.answer('Теперь покажите свое фото')



@edits.message(StateFilter(EditStatesGroup.edit_photo), F.photo)
async def handle_photo_upload(message: Message, state: FSMContext):
    photo_id = message.photo[0].file_id
    state_data = await state.get_data()


