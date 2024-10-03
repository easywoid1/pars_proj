import asyncio
from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher

from config import TOKEN, logger
from db.models import db_helper, Base

from routers import router as main_router

dp = Dispatcher()
dp.include_router(main_router)


async def init_db():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

async def main():
    await init_db()
    logger.add("db is start", level="info")
    bot = Bot(token=TOKEN)
    logger.info("bot start")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
