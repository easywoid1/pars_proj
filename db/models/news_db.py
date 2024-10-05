from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class News(Base):
    __tablename__ = "news"
    name: Mapped[str] = mapped_column(nullable=True)
    url: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=True)