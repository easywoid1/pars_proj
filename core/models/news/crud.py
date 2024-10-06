"""Create
Read
Update
Delete"""

from datetime import datetime, timedelta, time

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.news.schemas import NewsCreate, News
from db.models.db_helper import db_helper
from db.models.news_db import News as News_db


#
async def get_news_hour(session: AsyncSession) -> list[News_db]:
    time_now = datetime.now()
    time_hour_ago = time_now - timedelta(hours=1)

    stmt = (
        select(News_db)
        .filter(News_db.created_at.between(time_hour_ago, time_now))
        .order_by(News_db.created_at)
    )

    result: Result = await session.execute(stmt)
    news = result.scalars().all()
    return list(news)


async def get_news_day(session: AsyncSession) -> list[News_db]:
    start_of_day = datetime.combine(datetime.now().date(), time.min)
    print(f"Start of day: {start_of_day}")  # Отладочное сообщение

    stmt = (
        select(News_db)
        .filter(News_db.created_at >= start_of_day)
        .order_by(News_db.created_at)
    )

    result: Result = await session.execute(stmt)
    news = result.scalars().all()
    print(f"Fetched news: {news}")
    print(type(news))
    # Отладочное сообщение
    return list(news)


async def add_news(
    new_in: NewsCreate,
    session: AsyncSession = db_helper.session_dependency,
) -> News_db:
    news = News_db(**new_in.model_dump())
    session.add(news)
    await session.commit()
    await session.refresh(news)
    return news
