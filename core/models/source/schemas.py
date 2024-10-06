from pydantic import BaseModel


class SourceBase(BaseModel):
    url: str


class SourceCreate(SourceBase):
    pass


class Source(SourceBase):
    id: int
