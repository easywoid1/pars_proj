from pydantic import BaseModel
from datetime import datetime

class NewsBase(BaseModel):
    name: str
    url: str
    created_at: datetime

class NewsCreate(NewsBase):
    pass


class News(NewsBase):
    id: int
