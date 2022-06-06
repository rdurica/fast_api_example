from sqlalchemy.orm import Session

from models.task import Task
from models.user import User


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).join(User).filter(Task.id == task_id).first()
