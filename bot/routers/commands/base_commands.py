from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.bot_models import Buttons_text

router = Router(name=__name__)


def get_start_keyboard():
    button_hello = KeyboardButton(text=Buttons_text.hello)
    button_help = KeyboardButton(text=Buttons_text.help)
    button_news_day = KeyboardButton(text=Buttons_text.last_day_news)
    button_news_hour = KeyboardButton(text=Buttons_text.last_hour_news)
    button_add_source = KeyboardButton(text=Buttons_text.add_source)
    buttons_first_row = [button_hello, button_add_source]
    buttons_second_row = [button_help]
    buttons_third_row = [button_news_hour]
    buttons_fourth_row = [button_news_day]
    markup = ReplyKeyboardMarkup(
        keyboard=[
            buttons_first_row,
            buttons_second_row,
            buttons_third_row,
            buttons_fourth_row,
        ]
    )
    return markup


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text="Добрый день. Это бот для парсинга новостей.",
        reply_markup=get_start_keyboard(),
    )


@router.message(Command("help", prefix="!/"))
async def halndle_help(message: types.Message):
    await message.answer(
        text=f"Если есть какие-то вопросы по работе бота https://t.me/ALGGAL"
    )
