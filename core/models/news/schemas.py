from pydantic import BaseModel, ConfigDict, StringConstraints
from datetime import datetime


class NewsBase(BaseModel):
    name: str
    url: str
    created_at: datetime


class NewsCreate(NewsBase):
    pass


class News(NewsBase):
    id: int


class NewsGet(News):
    model_config = ConfigDict(from_attributes=True)
