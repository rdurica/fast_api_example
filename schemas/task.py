from pydantic import BaseModel

from schemas.user import User


class TaskBase(BaseModel):
    id: int
    summary: str
    description: str
    is_completed: bool


class TaskCreate(TaskBase):
    owner: User


class Task(TaskCreate):
    class Config:
        orm_mode = True
