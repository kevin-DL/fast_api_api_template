import uuid

from pydantic import BaseModel

from schemas.items import Item


class UserBase(BaseModel):
    display_name: str


class UserCreate(UserBase):
    password: str
    email: str


class User(UserBase):
    id: uuid.UUID
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
