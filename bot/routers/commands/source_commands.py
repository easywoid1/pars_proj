from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
#
from bot.bot_models import Buttons_text, FSMFillForm, add_source_to_db
from db.models import db_helper

router = Router(name=__name__)


@router.message(F.text == Buttons_text.add_source)
@router.message(Command(Buttons_text.add_source))
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
    await state.clear()


@router.message(Command(commands="fillurl"), StateFilter(default_state))
async def process_fillurl_command(message: types.Message, state: FSMContext):
    await message.answer(text="Пожалуйста, введите URL источника")
    await state.set_state(FSMFillForm.fill_url)


@router.message(StateFilter(FSMFillForm.fill_url))
async def process_url_sent(message: types.Message, state: FSMContext):
    url = message.text.strip()
    if url.startswith("http://") or url.startswith("https://"):
        http_ok = True
    else:
        http_ok = False
        await message.answer(
            text="Пожалуйста, введите корректный URL, начинающийся с http:// или https://"
        )
    if url.find(".") != -1:
        dot_ok = True
    else:
        dot_ok = False
        await message.answer(
            text='Пожалуйста, введите корректный URL, имеющий точку перед доменом, например ".com"'
        )
    if http_ok and dot_ok:
        await state.update_data(url=url)
        await message.answer(text="Спасибо! Ваш URL сохранен.")

        session = db_helper.get_scoped_session()
        try:
            await add_source_to_db(url=url, session=session)
        finally:
            await session.remove()

        await state.clear()


@router.message(StateFilter(FSMFillForm.fill_url))
async def warning_not_url(message: types.Message):
    await message.answer(
        text="Пожалуйста, введите корректный URL.\n\n"
        "Если вы хотите прервать процесс, отправьте команду /cancel"
    )
