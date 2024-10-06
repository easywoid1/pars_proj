import asyncio
import os
import sys

from aiogram import Bot, Dispatcher
from db.models import db_helper, Base
from bot.routers import router as main_router
from monitor.rss_parser import run
from core.config import settings, logger

# Добавляем родительскую директорию в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
    except asyncio.CancelledError:
        logger.info("Parsing end by user")
    except Exception as e:
        logger.error(f"Parsing error: {e}")


async def main():
    await init_db()
    bot = Bot(token=settings.token)
    logger.info("Bot start by button START")

    parsing_task = asyncio.create_task(start_parsing())
    logger.info("Parsing start")

    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError as e:
        logger.info("Bot stop by button STOP")

    except Exception as e:
        logger.error(f"Error {e}")
        parsing_task.cancel()

    parsing_task.cancel()
    await parsing_task


if __name__ == "__main__":
    asyncio.run(main())
