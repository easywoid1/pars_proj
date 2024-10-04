from sqlalchemy.orm import Mapped

from .base import Base


class SourceList(Base):
    name: Mapped[str]
    url: Mapped[str]
    news_datetime: Mapped[str]