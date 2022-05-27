from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from delendencies import get_database
import schemas.user
import crud

router = APIRouter()


@router.get("/user/{user_id}", response_model=schemas.user.User, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_database)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/", response_model=list[schemas.user.User], tags=["Users"])
def get_users(db: Session = Depends(get_database)):
    return crud.get_users(db)
