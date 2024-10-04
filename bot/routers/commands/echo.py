from aiogram import Router, types
from loguru import logger

router = Router(name=__name__)


@router.message()
async def echo_message(message: types.Message):
    logger.info(
        f"message:{message.text}| user_id: {message.from_user.id} | {message.from_user.username}"
    )
    await message.reply(
        text="Пожалуйста используйте кнопки-команды для управления ботом"
    )
