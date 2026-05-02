from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False   # ✅ Yeni alan eklendi

    class Config:
        from_attributes = True

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool   # ✅ Yeni alan eklendi

    class Config:
        from_attributes = True   # ✅ SQLAlchemy objelerini JSON’a çevirmek için