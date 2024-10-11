import json

from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.database.queue.get_user_id import get_user_id

from app.keyboards.back_to_main_keyboard import back_to_main_keyboard

MAX_CONTENT_LENGTH = 4096

get_news_last_day_router = Router()


@get_news_last_day_router.callback_query(F.data == 'last_day')
async def get_news_last_hour_callback(message: CallbackQuery):
    with open('app/temp/last_day.json', 'r', encoding='utf-8') as f:
        user_id = await get_user_id(message.from_user.id)
        user_news = [item for item in json.load(f) if item['user_id'] == user_id]

        if not user_news:
            content = 'Пока нет новостей за последние сутки 😿'

            await message.message.edit_text(content, reply_markup=back_to_main_keyboard())
        else:
            for news_item in user_news:
                for news in news_item['news']:
                    content = ''
                    news_content = ''
                    
                    title = news['title']
                    description = news['description']
                    link = news['link']
                    author = news['author']
                    published = news['published']

                    news_content += f'<b>{title}</b>\n' \
                               f'{description}\n' \
                               f'<a href="{link}">Читать подробнее</a>\n' \
                               f'<b>{author}</b>\n' \
                               f'<i>{published}</i>'
                    
                    if len(news_content) + len(content) > MAX_CONTENT_LENGTH:
                        available_space = MAX_CONTENT_LENGTH - len(content)
                        truncated_description = description[:available_space - len(news_content) + len(description)] + '...'

                        content += (
                            f'<b>{title}</b>\n' \
                            f'{truncated_description}\n' \
                            f'<a href="{link}">Читать подробнее</a>\n' \
                            f'<b>{author}</b>\n' \
                            f'<i>{published}</i>' \
                        )

                        break
                    else:
                        content += news_content

                    await message.message.answer(content, reply_markup=back_to_main_keyboard(), parse_mode='HTML')