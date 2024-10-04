from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from bot.bot_models import Buttons_text

router = Router(name=__name__)


@router.message(F.text == Buttons_text.last_day_news)
@router.message(Command(Buttons_text.last_day_news))
async def halndle_help(message: types.Message):
    news = {"Новость один": "llalalal", "Новость два": "llalalla"}
    await message.answer(text=f"Новости за последний день: {news}")


@router.message(F.text == Buttons_text.last_hour_news)
@router.message(Command(Buttons_text.last_hour_news))
async def halndle_help(message: types.Message):
    news = {
        "Новость одного часа": "llalalal",
    }
    await message.answer(text=f"Новости за последний день: {news}")
