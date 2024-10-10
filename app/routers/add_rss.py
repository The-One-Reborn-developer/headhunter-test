from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.keyboards.back_to_main_keyboard import back_to_main_keyboard


class AddRss(StatesGroup):
    rss_url = State()


add_rss_router = Router()


@add_rss_router.callback_query(F.data == 'add_rss')
async def add_rss(message: CallbackQuery, state: FSMContext):
    await state.set_state(AddRss.rss_url)

    content = 'Пожалуйста, предоставьте валидный URL RSS источника 😸'

    await message.message.edit_text(content, reply_markup=back_to_main_keyboard())