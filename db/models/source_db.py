from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Source(Base):
    __tablename__ = "sources"
    url: Mapped[str] = mapped_column(unique=True, nullable=False)