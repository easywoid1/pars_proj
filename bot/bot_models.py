from aiogram.fsm.state import StatesGroup, State
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from bot.config import logger
from core import SourceCreate
from core.models.news.crud import get_news_hour, get_news_day
from core.models.news.schemas import NewsGet
from core.models.source.crud import add_source
from db.models import db_helper


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


async def get_news_for_hour():
    session = db_helper.get_scoped_session()
    try:
        news = await get_news_hour(session=session)
        news_pydantic = []
        for _ in news:
            new = NewsGet.model_validate(_)
            news_pydantic.append(new)
        return news_pydantic
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при выполнении запроса: {e}")
        raise
    finally:
        await session.close()


async def get_news_for_day():
    session = db_helper.get_scoped_session()
    try:
        news = await get_news_day(session=session)
        if len(news) ==0:
            return []
        news_pydantic = []
        for _ in news:
            new = NewsGet.model_validate(_)
            news_pydantic.append(new)
        return news_pydantic

    except SQLAlchemyError as e:
        logger.error(f"Ошибка при выполнении запроса: {e}")
        raise
    finally:
        await session.close()
