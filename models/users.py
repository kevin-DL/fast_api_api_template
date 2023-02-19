from sqlalchemy import Boolean, Column, String, UUID
from sqlalchemy.orm import relationship

from api.database import Base
from uuid import uuid4

class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True, default=uuid4)
    email = Column(String, unique=True, index=True)
    display_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")