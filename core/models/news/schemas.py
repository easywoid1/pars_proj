from pydantic import BaseModel


class NewsBase(BaseModel):
    name: str
    url: str
    news_datetime: str


class News(NewsBase):
    id: int
