from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.tasks
from delendencies import get_database
import schemas.task

router = APIRouter()


@router.get("/task/{task_id}", response_model=schemas.task.Task, tags=["Tasks"])
def get_task(task_id: int, db: Session = Depends(get_database)):
    task = crud.tasks.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
