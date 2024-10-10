from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.scripts.get_news_last_hour import get_news_last_hour


get_news_last_hour_router = Router()


@get_news_last_hour_router.callback_query(F.data == 'last_hour')
async def get_news_last_hour_callback(message: CallbackQuery):
    await get_news_last_hour('https://dostup1.ru/rss/')