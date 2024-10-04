import asyncio

from aiogram import Bot, Dispatcher

from config import TOKEN, logger
from db.models import db_helper, Base

from routers import router as main_router

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


async def main():
    await init_db()
    logger.info("db is start")
    bot = Bot(token=TOKEN)
    logger.info("bot start")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
