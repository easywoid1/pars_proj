from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from bot.models import Buttons_text

router = Router(name=__name__)



@router.message(Command(Buttons_text.last_day_news, prefix="!/"))
async def halndle_help(message: types.Message):
    news = {"Новость один": 'llalalal',
            "Новость два": 'llalalla'}
    await message.answer(text=f'Новости за последний день: {news}')


@router.message(Command(Buttons_text.last_hour_news, prefix="!/"))
async def halndle_help(message: types.Message):
    news = {"Новость одного часа": 'llalalal',}
    await message.answer(text=f'Новости за последний день: {news}')