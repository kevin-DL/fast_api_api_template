from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.items import create_user_item, get_items
from schemas.items import Item, ItemCreate
from schemas.users import User
from deps import get_current_active_user, get_db

router = APIRouter()


@router.get("/users/me/items/", response_model=List[Item])
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return current_user.items


@router.post("/users/{user_id}/items/", response_model=Item)
def create_item_for_user(
        user_id: str, item: ItemCreate, db: Session = Depends(get_db)
):
    return create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items
