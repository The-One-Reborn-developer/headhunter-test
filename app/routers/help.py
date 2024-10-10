from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.back_to_main_keyboard import back_to_main_keyboard


help_router = Router()


@help_router.callback_query(F.data == 'help')
async def command_start(message: CallbackQuery):
    content = '😺 Чтобы добавить новый RSS источник, выберите соответствующую кнопку в главном меню.\n' \
              '😺 Далее, предоставьте валидный URL.\n' \
              '😺 Для получения новостей за последний час, выберите соответствующую кнопку в главном меню.\n' \
              '😺 Для получения новостей за последний сутки, выберите соответствующую кнопку в главном меню.\n'
    
    await message.message.edit_text(content, reply_markup=back_to_main_keyboard())