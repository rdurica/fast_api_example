from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
import crud.tasks
from config.delendencies import get_database
from config.responses import responses
import schemas.task as schemas

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.get("/id/{task_id}", response_model=schemas.Task, responses=responses)
def get_task(task_id: int, db: Session = Depends(get_database)):
    task = crud.tasks.get_task_by_id(db, task_id)
    if task is None:
        return JSONResponse(status_code=404, content=responses.get(404))
    return task


@router.get("/all/", response_model=list[schemas.Task])
def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_database)):
    return crud.tasks.get_tasks(db, skip, limit)


@router.post("/create", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_database)):
    try:
        new_task = crud.tasks.create_task(db, task)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e.orig))

    return new_task


@router.delete("/delete/{task_id}", response_description="Successfully deleted")
def delete_task_by_id(task_id: int, db: Session = Depends(get_database)):
    crud.tasks.delete_task(db, task_id)
    return JSONResponse(status_code=200, content={"message": "Successfully deleted"})
