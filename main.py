import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from app.routers.main import main_router
from app.routers.add_rss import add_rss_router

from app.database.queue.initialize_database import initialize_database


async def main() -> None:
    load_dotenv(find_dotenv())
    
    bot = Bot(token=os.getenv('TOKEN'))
    print(f'Loaded bot {bot.id} with token {bot.token}')
    dp = Dispatcher()
    dp.include_routers(main_router, add_rss_router)

    await initialize_database()
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass