from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String, UUID
from sqlalchemy.orm import relationship

from api.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(UUID, primary_key=True, index=True, default=uuid4)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(UUID, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
