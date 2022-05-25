from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from database import Base, engine, SessionLocal
import schemas.user

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/user/{user_id}", response_model=schemas.user.User, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users/", response_model=list[schemas.user.User], tags=["Users"])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
