# models.py
from sqlalchemy import Column, Integer, String, Boolean
from database import Base
from pydantic import BaseModel

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

    class Config:
        from_attributes = True


