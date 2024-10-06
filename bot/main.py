import asyncio

from aiogram import Bot, Dispatcher

from config import TOKEN, logger

import sys
import os

# Добавляем родительскую директорию в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.models import db_helper, Base

from routers import router as main_router
from monitor.rss_parser import run

dp = Dispatcher()
dp.include_router(main_router)


async def init_db():
    try:
        async with db_helper.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            logger.info("База данных инициализирована")
    except Exception as e:
        logger.error(f"Ошибка инициализации базы данных: {e}")
        raise


async def start_parsing():
    try:
        while True:
            logger.info("start parsing")
            await run()
            await asyncio.sleep(60)
    except Exception as e:
        logger.error(f"Parsing error: {e}")


async def main():
    await init_db()
    bot = Bot(token=TOKEN)
    logger.info("Bot start by button START")

    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError as e:
        logger.info("Bot stop by button STOP")
    except Exception as e:
        logger.error(f"Error {e}")

    await asyncio.create_task(start_parsing())

    try:
        logger.info("Parsing is starting")
        await run()
    except Exception as e:
        logger.error("Problem with parsing")


if __name__ == "__main__":
    asyncio.run(main())
