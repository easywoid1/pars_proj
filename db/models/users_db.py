from sqlalchemy.orm import Mapped

from .base import Base


class Users(Base):
    username: Mapped[str]
    user_id: Mapped[str]