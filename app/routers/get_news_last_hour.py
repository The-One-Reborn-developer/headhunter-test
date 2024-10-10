import json

from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.scripts.get_news_last_hour import get_news_last_hour


get_news_last_hour_router = Router()


@get_news_last_hour_router.callback_query(F.data == 'last_hour')
async def get_news_last_hour_callback(message: CallbackQuery):
    with open('app/temp/last_hour.json', 'r', encoding='utf-8') as f:
        news = json.load(f)

        if news:
            for item in news:
                await message.message.answer(f"<b>Заголовок:</b> {item['title']}\n" \
                                             f"<b>Описание:</b> {item['description']}\n" \
                                             f"<b>Ссылка:</b> {item['link']}\n" \
                                             f"<b>Автор:</b> {item['author']}\n" \
                                             f"<b>Дата публикации:</b> {item['published']}", parse_mode='HTML')