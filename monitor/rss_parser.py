from datetime import datetime
from email.utils import parsedate_to_datetime
import aiohttp
import feedparser
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from core.models.news.crud import add_news
from core.models.news.schemas import NewsCreate
from core.models.source.crud import get_sources
from db.models import db_helper
from utils import get_response, parse_response
from core.models import News
from bot.config import logger


async def get_dict_with_sources() -> dict:
    session = db_helper.get_scoped_session()
    try:
        sources = await get_sources(session=session)
        # print(sources)
        sources_dict: dict = {source.id: source.url for source in sources}
        # todo разобрать эту магию
        # print(sources)
        return sources_dict
    except Exception as e:
        print(f"Ошибка при получении источников: {e}")
        return {}
    finally:
        await session.close()


async def add_news_to_db(new_in: NewsCreate):
    db_session = db_helper.get_scoped_session()
    try:
        await add_news(session=db_session, new_in=new_in)
    except Exception as e:
        logger.error(f"Ошибка при обработке URL: {e}")
    finally:
        await db_session.close()


async def str_time_to_datetime(published: str) -> datetime:
    try:
        dt = parsedate_to_datetime(published)
        formated_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
        return formated_dt
    except Exception as e:
        raise ValueError(f"Invalid date format: {published}") from e


async def run():

    sources: dict = await get_dict_with_sources()
    # sources = {"1": "https://dostup1.ru/rss/"}
    for url in sources.values():
        response = await get_response(url=url)
        parsed_response = await parse_response(response=response)
        for article in parsed_response.entries:
            # print(type(article.title))
            new_in = NewsCreate(
                name=article.title,
                url=article.link,
                created_at=await str_time_to_datetime(article.published),
            )
            print(
                f"{type(new_in)} | {new_in.name} | {new_in.url} | {new_in.created_at}"
            )
            await add_news_to_db(new_in=new_in)


asyncio.run(run())
