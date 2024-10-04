from aiogram import Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from bot.bot_models import Buttons_text, FSMFillForm

router = Router(name=__name__)


@router.message(Command(Buttons_text.add_source, prefix="!/"))
async def add_source(message: types.Message):
    await message.answer(text="Чтобы добавить URL, отправьте команду /fillurl")


@router.message(Command(commands="cancel"), StateFilter(default_state))
async def process_cancel_command(message: types.Message):
    await message.answer(
        text="Отменять нечего. Вы вне машины состояний\n\n"
        "Чтобы перейти к заполнению URL - "
        "отправьте команду /fillurl"
    )


@router.message(Command(commands="cancel"), ~StateFilter(default_state))
async def process_cancel_command_state(message: types.Message, state: FSMContext):
    await message.answer(
        text="Вы вышли из машины состояний\n\n"
        "Чтобы снова перейти к заполнению URL - "
        "отправьте команду /fillurl"
    )
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()


@router.message(Command(commands="fillurl"), StateFilter(default_state))
async def process_fillurl_command(message: types.Message, state: FSMContext):
    await message.answer(text="Пожалуйста, введите URL источника")
    # Устанавливаем состояние ожидания ввода URL
    await state.set_state(FSMFillForm.fill_url)


@router.message(StateFilter(FSMFillForm.fill_url))
async def process_url_sent(message: types.Message, state: FSMContext):
    url = message.text.strip()
    # Здесь можно добавить проверку на корректность URL
    if url.startswith("http://") or url.startswith("https://"):
        # Сохраняем URL в "базу данных" или в контексте
        await state.update_data(url=url)
        await message.answer(text="Спасибо! Ваш URL сохранен.")
        # Завершаем машину состояний
        await state.clear()
    else:
        await message.answer(
            text="Пожалуйста, введите корректный URL, начинающийся с http:// или https://"
        )


@router.message(StateFilter(FSMFillForm.fill_url))
async def warning_not_url(message: types.Message):
    await message.answer(
        text="Пожалуйста, введите корректный URL.\n\n"
        "Если вы хотите прервать процесс, отправьте команду /cancel"
    )
