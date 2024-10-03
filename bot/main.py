import asyncio

from aiogram import Bot, Dispatcher, types

from config import TOKEN, logger

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def get_message(message: types.Message):
    logger.info(f'message:{message.text}| user_id: {message.from_user.id} | {message.from_user.username}')
    await message.reply(text="Пожалуйста используйте кнопки-команды для управления ботом")


async def main():
    logger.info('bot start')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
