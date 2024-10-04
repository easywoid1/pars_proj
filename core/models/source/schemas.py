from pydantic import BaseModel


class SourceBase(BaseModel):
    name: str
    url: str


class Source(SourceBase):
    id: int
