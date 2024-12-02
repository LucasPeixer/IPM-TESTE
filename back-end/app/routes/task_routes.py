from fastapi import APIRouter, Depends
from app.controller.task_controller import TaskController
from app.usecase.task_usecase import TaskUseCase
from app.repository.task_repository import TaskRepository
from app.db.db import get_db
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from app.middleware.jwt import verify_jwt_token
from typing import List
from sqlalchemy.orm import Session

# Dependências globais para otimizar instanciamentos
def get_task_repository(db: Session = Depends(get_db)):
    return TaskRepository(db)

def get_task_usecase(task_repository: TaskRepository = Depends(get_task_repository)):
    return TaskUseCase(task_repository)

def get_task_controller(task_usecase: TaskUseCase = Depends(get_task_usecase)):
    return TaskController(task_usecase)

# Criando as rotas com JWT aplicado
def create_task_routes(router: APIRouter):
    # Rota para obter todas as tarefas
    @router.get("/", response_model=List[TaskResponse])
    def get_tasks(task_controller: TaskController = Depends(get_task_controller),
                  current_user=Depends(verify_jwt_token)):

        return task_controller.get_all_tasks()

    # Rota para obter uma tarefa pelo ID
    @router.get("/{task_id}", response_model=TaskResponse)
    def get_task(task_id: int,
                 task_controller: TaskController = Depends(get_task_controller),
                 current_user=Depends(verify_jwt_token)):

        return task_controller.get_task(task_id)

    # Rota para criar uma nova tarefa
    @router.post("/", response_model=TaskResponse, status_code=201)
    def create_task(task_data: TaskCreate,
                    task_controller: TaskController = Depends(get_task_controller),
                    current_user=Depends(verify_jwt_token)):

        return task_controller.create_task(task_data.dict())

    # Rota para atualizar uma tarefa
    @router.put("/{task_id}", response_model=TaskResponse)
    def update_task(task_id: int,
                    task_data: TaskUpdate,
                    task_controller: TaskController = Depends(get_task_controller),
                    current_user=Depends(verify_jwt_token)):

        return task_controller.update_task(task_id, task_data.dict())

    # Rota para deletar uma tarefa
    @router.delete("/{task_id}", status_code=204)
    def delete_task(task_id: int,
                    task_controller: TaskController = Depends(get_task_controller),
                    current_user=Depends(verify_jwt_token)):

        return task_controller.delete_task(task_id)
