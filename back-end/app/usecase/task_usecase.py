from app.repository.task_repository import TaskRepository

class TaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def get_all_tasks(self):
        return self.task_repository.get_all_tasks()

    def get_task(self, task_id: int):
        return self.task_repository.get_task_by_id(task_id)

    def create_task(self, task_data: dict):
        return self.task_repository.create_task(task_data)

    def update_task(self, task_id: int, task_data: dict):
        task = self.task_repository.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        return self.task_repository.update_task(task_id, task_data)

    def delete_task(self, task_id: int):
        task = self.task_repository.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        self.task_repository.delete_task(task_id)
