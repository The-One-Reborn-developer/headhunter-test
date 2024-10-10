from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.main_keyboard import main_keyboard

from app.database.queue.set_user import set_user


main_router = Router()


@main_router.message(CommandStart())
async def command_start(message: Message):
    await set_user(message.from_user.id)

    content = f'Добрый день, {message.from_user.full_name} 🐱' \
               'Выберите опцию из меню ниже ⏬'
    
    await message.answer(content, reply_markup=main_keyboard())
