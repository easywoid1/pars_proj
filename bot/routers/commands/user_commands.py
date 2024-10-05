from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from bot.bot_models import Buttons_text, get_news_for_hour, get_news_for_day
from core.models.news.crud import get_news_hour, get_news_day

router = Router(name=__name__)


@router.message(F.text == Buttons_text.last_day_news)
@router.message(Command(Buttons_text.last_day_news))
async def show_news_for_day(message: types.Message):
    news = await get_news_for_day()
    await message.answer(text=f"Новости за последний день: {news}")


@router.message(F.text == Buttons_text.last_hour_news)
@router.message(Command(Buttons_text.last_hour_news))
async def show_news_for_hour(message: types.Message):
    news = await get_news_for_hour()
    await message.answer(text=f"Новости за последний день: {news}")

