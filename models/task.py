from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    summary = Column(String(length=150), index=True)
    description = Column(Text(length=500))
    is_completed = Column(Boolean, default=False)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("models.user.User", back_populates="tasks")
