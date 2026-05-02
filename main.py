from fastapi import FastAPI
import models
from database import engine
from tasks import router
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Task

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "FastAPI + PostgreSQL ready!"}


@app.put("/tasks/{task_id}/toggle")
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"error": "Task tapılmadı"}

    task.completed = not task.completed

    db.commit()
    db.refresh(task)

    return task