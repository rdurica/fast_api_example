from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from config.delendencies import get_database
import crud.users
from config.responses import responses
import schemas.user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/id/{user_id}", response_model=schemas.user.User, responses=responses)
def get_user(user_id: int, db: Session = Depends(get_database)):
    user = crud.users.get_user(db, user_id=user_id)
    if user is None:
        return JSONResponse(status_code=404, content=responses.get(404))
    return user


@router.get("/all/", response_model=list[schemas.user.User])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_database)):
    return crud.users.get_users(db, skip, limit)
