from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Source(Base):
    __tablename__ = "sources"
    url: Mapped[str] = mapped_column(unique=True, nullable=False)

    def __repr__(self):
        return f"Source_id={self.id}, url={self.url}"

    def __str__(self):
        return f"Source ID: {self.id}, URL: {self.url}"
