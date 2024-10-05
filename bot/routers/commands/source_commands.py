from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from sqlalchemy.exc import IntegrityError
import aiohttp
from bot.config import logger

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

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()  # Проверка статуса
                await state.update_data(url=url)  # Сохранение URL

                # Сохранение в базу данных
                db_session = db_helper.get_scoped_session()
                try:
                    await add_source_to_db(url=url, session=db_session)
                    await message.answer(text="Спасибо! Ваш URL сохранен.")
                    logger.info(
                        f"User_id {message.from_user.id} | nickname {message.from_user.username} | добавил источник {url}"
                    )
                except IntegrityError:
                    await db_session.rollback()
                    await message.answer(text="Извините! Данный URL уже сохранен в списке источников.")
                finally:
                    await db_session.remove()

                await state.clear()  # Очистка состояния

        except aiohttp.ClientResponseError as e:
            logger.error(f"Неверный URL, ошибка: {e}")
            await message.answer(
                text=f"Не удалось отправить запрос на данный URL, пожалуйста проверьте ссылку. Ошибка: {e}"
            )
        except Exception as e:
            logger.error(f"Ошибка при обработке URL: {e}")
            await message.answer(
                text="Произошла ошибка при обработке вашего запроса. Выйти: /cancel"
            )



@router.message(StateFilter(FSMFillForm.fill_url))
async def warning_not_url(message: types.Message):
    await message.answer(
        text="Пожалуйста, введите корректный URL.\n\n"
        "Если вы хотите прервать процесс, отправьте команду /cancel"
    )
