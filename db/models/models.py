from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


class News(Base):
    __tablename__ = "news"
    name: Mapped[str] = mapped_column(nullable=True)
    url: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=True)


class Source(Base):
    __tablename__ = "sources"
    url: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __repr__(self):
        return f"Source_id={self.id}, url={self.url}"

    def __str__(self):
        return f"Source ID: {self.id}, URL: {self.url}"


class Users(Base):
    __tablename__ = "users"
    username: Mapped[str]
    user_id: Mapped[str]
