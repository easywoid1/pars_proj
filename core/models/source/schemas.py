from pydantic import BaseModel


class SourceBase(BaseModel):
    url: str

class SourceCreate(BaseModel):
    pass

class Source(SourceBase):
    id: int
