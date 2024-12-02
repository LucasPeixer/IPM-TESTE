from sqlalchemy import Column, Integer, String
from app.db.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String)

    class Config:
        orm_mode = True
        from_attributes = True