from sqlalchemy.orm import Session
from models.task import Task
from models.user import User
import schemas.task


def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).join(User).filter(Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).join(User).offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.task.TaskCreate):
    new_task = Task(summary=task.summary,
                    description=task.description,
                    is_completed=task.is_completed,
                    owner_id=task.owner_id)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def delete_task(db: Session, task_id: int):
    """Delete directly due to performance"""
    db.query(Task).filter(Task.id == task_id).delete()
    db.commit()
