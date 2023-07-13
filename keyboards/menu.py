from aiogram.types import BotCommand

menu = [
    BotCommand(command="/start", description="Запустить/Перезапустить бота"),
    BotCommand(command="/fillform", description="Заполнить анкету"),
    BotCommand(command="/show", description="Посмотреть анкету")
]