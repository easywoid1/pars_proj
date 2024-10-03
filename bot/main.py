import asyncio
from contextlib import asynccontextmanager

from aiogram import Bot, Dispatcher

from config import TOKEN, logger


from routers import router as main_router

dp = Dispatcher()
dp.include_router(main_router)


async def main():
    logger.info('bot start')
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
