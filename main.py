from fastapi import FastAPI

from database import Base, engine
import routers.users
import routers.tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Example",
    description="Api example project based on FastAPI",
    version="1.0.0"
)
app.include_router(routers.users.router)
app.include_router(routers.tasks.router)
