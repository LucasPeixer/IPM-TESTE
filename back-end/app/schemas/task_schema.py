from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.validators.task_validator import TaskValidators


class TaskBase(BaseModel):
    title: str
    description: str
    dueDate: Optional[datetime] = None

    # Usando os validadores definidos na classe TaskValidators
    _validate_due_date = TaskValidators.validate_due_date
    _validate_title = TaskValidators.validate_title
    _validate_description = TaskValidators.validate_description


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    status: Optional[str] = None
    dueDate: Optional[datetime] = None


class TaskResponse(TaskBase):
    id: int
    status: str

    class Config:
        from_attributes = True
