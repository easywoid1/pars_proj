"""Create
Read
Update
Delete"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.source import Source

async def get_sources(session: AsyncSession)-> list[Source]:
    stmt = select(Source).order_by(Source.id)
    result: Result = await session.execute(stmt)
    sources =  result.scalars().all()
    return list(sources)