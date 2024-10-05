import aiohttp
import feedparser

from bot.config import logger

def format_article(article):
    return {
        "title": article.title,
        "link": article.link,
        "published": article.published,
        "summary": article.summary,
    }

async def get_response(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            try:
                response.raise_for_status()
                return await response.text()
            except aiohttp.ClientResponseError as e:
                logger.error(f"Проблема с получением ответа по url {url} | Error: {e}")
                return None

async def parse_response(response: str):
    parsed_response = feedparser.parse(response)
    return parsed_response
# async def get_dict_with_sources()-> dict:
#     session = db_helper.get_scoped_session()
#     try:
#         sources = await get_sources(session=session)
#         # print(sources)
#         sources_dict: dict = {source.id: source.url for source in sources}
#         # todo разобрать эту магию
#         # print(sources)
#         return sources_dict
#     except Exception as e:
#         print(f"Ошибка при получении источников: {e}")
#         return {}
#     finally:
#         await session.close()


# asyncio.run(get_dict_with_sources())