from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.keyboards.back_to_main_keyboard import back_to_main_keyboard

from app.scripts.check_url import check_url

from app.database.queue.set_rss_source import set_rss_source
from app.database.queue.get_user_id import get_user_id
from app.database.queue.check_rss_source import check_rss_source


class AddRss(StatesGroup):
    rss_url = State()


add_rss_router = Router()


@add_rss_router.callback_query(F.data == 'add_rss')
async def add_rss(message: CallbackQuery, state: FSMContext):
    await state.set_state(AddRss.rss_url)

    content = 'Пожалуйста, предоставьте валидный URL RSS источника 😸'

    await message.message.edit_text(content, reply_markup=back_to_main_keyboard())


@add_rss_router.message(AddRss.rss_url)
async def add_rss_url(message: Message, state: FSMContext):
    is_valid_url = await check_url(message.text)

    if not is_valid_url:
        content = 'Предоставленный Вами URL RSS некорректный, либо произошла ошибка 😿\n' \
                  'Попробуйте ещё раз.'

        await message.answer(content, reply_markup=back_to_main_keyboard())
    else:
        rss_exists = await check_rss_source(message.text)

        if rss_exists:
            content = 'Вы уже добавляли этот RSS источник 😼'

            await message.answer(content, reply_markup=back_to_main_keyboard())
            return

        user_id = await get_user_id(message.from_user.id)
        await set_rss_source(message.text, user_id)

        await state.clear()

        content = 'RSS источник успешно добавлен 😻'

        await message.answer(content, reply_markup=back_to_main_keyboard())