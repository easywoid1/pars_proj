"""Create
Read
Update
Delete"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.source.schemas import SourceCreate
from db.models import Source
from db.models.db_helper import db_helper
from core.config import logger

from sqlalchemy.exc import SQLAlchemyError


async def get_sources(
    session: AsyncSession = db_helper.session_dependency,
) -> list[Source]:
    try:
        stmt = select(Source).order_by(Source.id)
        result: Result = await session.execute(stmt)
        sources = result.scalars().all()
        return list(sources)
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при выполнении запроса: {e}")
        raise


async def get_source(session: AsyncSession, source_id: int) -> Source | None:
    return await session.get(Source, source_id)


async def add_source(
    source_in: SourceCreate,
    session: AsyncSession = db_helper.session_dependency,
) -> Source:
    source = Source(**source_in.model_dump())
    session.add(source)
    await session.commit()
    await session.refresh(source)
    return source
