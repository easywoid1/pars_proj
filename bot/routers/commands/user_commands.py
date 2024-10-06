from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from bot.bot_models import Buttons_text, get_news_for_hour, get_news_for_day

router = Router(name=__name__)


@router.message(F.text == Buttons_text.last_day_news)
@router.message(Command(Buttons_text.last_day_news))
async def show_news_for_day(message: types.Message):
    news = await get_news_for_day()
    await message.answer(text=f"Количество новостей: {len(news)}")
    for new in news:
        await message.answer(text=f"{new.created_at} | {new.name} | {new.url}")


@router.message(F.text == Buttons_text.last_hour_news)
@router.message(Command(Buttons_text.last_hour_news))
async def show_news_for_hour(message: types.Message):
    news = await get_news_for_hour()
    if not news:
        await message.answer(text=f'За последний час новостей нет')
    else:
        await message.answer(text=f"Новости за последний день: {news}")

