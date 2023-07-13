from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from callbackes.form import GenderCallbackData
from data import users_data
from keyboards.inline import gender_inline_keyboard
from states.form import FormStatesGroup

fill_form_router = Router()


@fill_form_router.message(Command('fillform'))
async def handle_fillform(message: Message, state: FSMContext):
    await message.answer('Вы начали заполнение анкеты. Для начала введите имя')
    await state.set_state(FormStatesGroup.fill_name)


@fill_form_router.message(StateFilter(FormStatesGroup.fill_name))
async def handle_get_name(message: Message, state: FSMContext):
    name_from_message = message.text
    await state.update_data(name=name_from_message)  # {'name': name_from_message}
    await message.answer('Хорошо. А теперь напишите ваш возраст')
    await state.set_state(FormStatesGroup.fill_age)


@fill_form_router.message(StateFilter(FormStatesGroup.fill_age))
async def handle_get_age(message: Message, state: FSMContext):
    age_from_message = message.text
    if age_from_message.isdigit() and 1 <= int(age_from_message) <= 120:
        await state.update_data(age=age_from_message)
        await message.answer('А теперь укажите свой пол', reply_markup=gender_inline_keyboard)
        await state.set_state(FormStatesGroup.fill_gender)


@fill_form_router.callback_query(StateFilter(FormStatesGroup.fill_gender), GenderCallbackData.filter())
async def handle_get_gender(query: CallbackQuery, callback_data: GenderCallbackData, state: FSMContext):
    is_male = callback_data.is_male
    await state.update_data(is_male=is_male)
    await query.message.answer('А теперь немного расскажите о себе')
    await state.set_state(FormStatesGroup.fill_description)
    await query.answer()  # Убираем часики


@fill_form_router.message(StateFilter(FormStatesGroup.fill_description))
async def handle_get_description(message: Message, state: FSMContext):
    description_from_message = message.text
    await state.update_data(description=description_from_message)
    await message.answer('Теперь покажите свое фото')
    await state.set_state(FormStatesGroup.upload_photo)


@fill_form_router.message(StateFilter(FormStatesGroup.upload_photo), F.photo)
async def handle_photo_upload(message: Message, state: FSMContext):
    photo_id = message.photo[0].file_id
    state_data = await state.get_data()
    name = state_data['name']
    age = int(state_data['age'])
    gender = state_data["gender"]
    description = state_data["description"]
    users_data[message.from_user.id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "description": description,
        "photo": photo_id
    }




