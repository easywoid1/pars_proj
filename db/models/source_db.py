from sqlalchemy.orm import Mapped

from .base import Base


class Source(Base):
    name: Mapped[str]
    url: Mapped[str]