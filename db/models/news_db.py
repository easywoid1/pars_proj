from sqlalchemy.orm import Mapped

from .base import Base


class News(Base):
    __tablename__ = "news"
    description: Mapped[str]
    url: Mapped[str]
    created_at: Mapped[str]