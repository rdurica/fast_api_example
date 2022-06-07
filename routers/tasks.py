from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import crud.tasks
from delendencies import get_database
import schemas.task as schemas

router = APIRouter()


@router.get("/task/{task_id}", response_model=schemas.Task, tags=["Tasks"])
def get_task(task_id: int, db: Session = Depends(get_database)):
    task = crud.tasks.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.get("/tasks/", response_model=list[schemas.Task], tags=["Tasks"])
def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_database)):
    return crud.tasks.get_tasks(db, skip, limit)


@router.post("/task/create", response_model=schemas.Task, tags=["Tasks"])
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_database)):
    try:
        new_task = crud.tasks.create_task(db, task)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e.orig))

    return new_task


@router.delete("/task/delete/{task_id}", response_description="Successfully deleted", tags=["Tasks"])
def delete_task_by_id(task_id: int, db: Session = Depends(get_database)):
    crud.tasks.delete_task(db, task_id)
    return "Successfully deleted"
