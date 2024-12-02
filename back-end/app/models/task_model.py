from sqlalchemy import DateTime, Enum, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()


class TaskStatusEnum(enum.Enum):
    Pendente = "Pendente"
    Finalizado = "Finalizado"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(Enum(TaskStatusEnum), default=TaskStatusEnum.Pendente)
    createdAt = Column(DateTime, default=datetime.now)
    dueDate = Column(DateTime)