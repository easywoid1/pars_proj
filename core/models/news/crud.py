"""Create
Read
Update
Delete"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core import News
from core.models.news.schemas import NewsCreate
from core.models.source.schemas import SourceCreate
from db.models.db_helper import db_helper
from bot.config import logger
from db.models.news_db import News as News_db

from sqlalchemy.exc import SQLAlchemyError

#
# async def get_news(
#     session: AsyncSession = db_helper.session_dependency,
# ) -> list[Source]:
#     try:
#         stmt = select(Source).order_by(Source.id)
#         result: Result = await session.execute(stmt)
#         sources = result.scalars().all()
#         return list(sources)
#     except SQLAlchemyError as e:
#         logger.error(f"Ошибка при выполнении запроса: {e}")
#         raise

#
# async def get_source(session: AsyncSession, news_id: int) -> Source | None:
#     return await session.get(News, news_id)


async def add_news(
    new_in: NewsCreate,
    session: AsyncSession = db_helper.session_dependency,
) -> News_db:
    news = News_db(**new_in.model_dump())
    session.add(news)
    await session.commit()
    await session.refresh(news)
    return news
