from aiogram.fsm.state import StatesGroup, State
from sqlalchemy.ext.asyncio import AsyncSession

from core import SourceCreate
from core.models.source.crud import add_source


class Buttons_text:
    hello = "Hello"
    help = "Help"
    last_day_news = "Get_news_for_the_day"
    last_hour_news = "Get_news_for_the_hour"
    add_source = "Add_Source"


class FSMFillForm(StatesGroup):
    fill_url = State()  # Состояние ожидания ввода url


async def add_source_to_db(url: str, session: AsyncSession):
    new_source = SourceCreate(url=url)
    await add_source(source_in=new_source, session=session)
