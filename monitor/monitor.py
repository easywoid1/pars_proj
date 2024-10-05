import asyncio
from db.models import db_helper
from core.models.source.crud import get_sources

async def g():
    session = db_helper.get_scoped_session()
    try:
        sources = await get_sources(session=session)
        print(sources)
    except Exception as e:
        print(f"Ошибка при получении источников: {e}")
    finally:
        await session.close()  # Закрываем сессию после использования

asyncio.run(g())
