from pydantic import BaseModel


class SourceListBase(BaseModel):
    name: str
    url: str
    news_datetime: str


class SourceList(SourceListBase):
    id: int
