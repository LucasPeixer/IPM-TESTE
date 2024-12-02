from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

class TaskController:
    def __init__(self, task_usecase):
        self.task_usecase = task_usecase

    def get_all_tasks(self):
        try:
            return self.task_usecase.get_all_tasks()
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Database error")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def get_task(self, task_id: int):
        try:
            task = self.task_usecase.get_task(task_id)
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            return task
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Database error")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def create_task(self, task_data: dict):
        try:
            return self.task_usecase.create_task(task_data)
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Database error")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def update_task(self, task_id: int, task_data: dict):
        try:
            return self.task_usecase.update_task(task_id, task_data)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Database error")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def delete_task(self, task_id: int):
        try:
            self.task_usecase.delete_task(task_id)
            return {"message": "Task deleted"}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail="Database error")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")
