from pydantic import BaseModel


class NewsBase(BaseModel):
    name: str
    url: str
    created_at: str

class NewsCreate(NewsBase):
    pass


class News(NewsBase):
    id: int
