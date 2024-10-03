from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.models import Buttons_text

router = Router(name=__name__)


def get_start_keyboard():
    button_hello = KeyboardButton(text=Buttons_text.hello)
    button_help = KeyboardButton(text=Buttons_text.help)
    buttons_first_row = [button_hello]
    buttons_second_row = [button_help]
    markup = ReplyKeyboardMarkup(keyboard=[buttons_first_row, buttons_second_row])
    return markup


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text="Добрый день. Это бот для парсинга новостей.",
                         reply_markup=get_start_keyboard())


@router.message(Command('help', prefix="!/"))
async def halndle_help(message: types.Message):
    await message.answer(text=f'Если есть какие-то вопросы по работе бота https://t.me/ALGGAL')
