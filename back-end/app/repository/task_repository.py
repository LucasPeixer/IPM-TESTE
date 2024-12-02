from sqlalchemy.orm import Session
from app.models.task_model import Task

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_tasks(self):
        return self.db.query(Task).all()

    def get_task_by_id(self, task_id: int):
        return self.db.query(Task).filter(Task.id == task_id).first()

    def create_task(self, task_data: dict):
        new_task = Task(**task_data)
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)
        return new_task

    def update_task(self, task_id: int, task_data: dict):
        task = self.get_task_by_id(task_id)
        if task:
            for key, value in task_data.items():
                setattr(task, key, value)
            self.db.commit()
            self.db.refresh(task)
        return task

    def delete_task(self, task_id: int):
        task = self.get_task_by_id(task_id)
        if task:
            self.db.delete(task)
            self.db.commit()
