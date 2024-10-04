from sqlalchemy.orm import Mapped

from .base import Base


class Source(Base):
    url: Mapped[str]