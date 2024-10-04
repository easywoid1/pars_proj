from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    user_id: str


class User(UserBase):
    id: int
