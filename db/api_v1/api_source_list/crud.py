"""
CREATE
READ
UPDATE
DELETE
"""

from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from db.models.source_db import SourceList


async def get_news(session: AsyncSession) -> list[SourceList]:

    return
