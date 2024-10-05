import asyncio
from db.models import db_helper
from core.models.source.crud import get_sources


async def get_dict_with_sources():
    session = db_helper.get_scoped_session()
    try:
        sources = await get_sources(session=session)
        sources_dict = {
            source.id: source.url for source in sources
        }  # todo разобрать эту магию
        return sources_dict
        # print(sources)
    except Exception as e:
        print(f"Ошибка при получении источников: {e}")
    finally:
        await session.close()


asyncio.run(get_dict_with_sources())
