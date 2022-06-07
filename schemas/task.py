from pydantic import BaseModel

from schemas.user import User


class TaskBase(BaseModel):
    summary: str
    description: str
    is_completed: bool = False


class TaskWithId(TaskBase):
    id: int


class TaskView(TaskBase):
    owner: User


class TaskCreate(TaskBase):
    owner_id: int


class Task(TaskView, TaskWithId):
    class Config:
        orm_mode = True
