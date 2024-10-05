from pydantic import BaseModel


class NewsBase(BaseModel):
    name: str
    url: str
    created_at: str


class News_obj(NewsBase):
    id: int
