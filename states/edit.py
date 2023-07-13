from aiogram import Router
from aiogram.fsm.state import StatesGroup, State



class EditStatesGroup(StatesGroup):
    edit_name = State()
    edit_age = State()
    edit_gender = State()
    edit_description = State()
    edit_photo = State()
