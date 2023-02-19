import uuid

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: uuid.UUID
    owner_id: uuid.UUID

    class Config:
        orm_mode = True
