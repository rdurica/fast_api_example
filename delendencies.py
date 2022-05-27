# Dependency
from database import SessionLocal


def get_database() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
