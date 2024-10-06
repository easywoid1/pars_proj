from sqlalchemy.orm import Mapped

from .base import Base


class Users(Base):
    __tablename__ = "users"
    username: Mapped[str]
    user_id: Mapped[str]
