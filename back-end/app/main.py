from fastapi import FastAPI, APIRouter
from app.routes.task_routes import create_task_routes
from app.routes.user_routes import create_user_routes
from app.middleware.cors import add_cors_middleware

app = FastAPI()

# Adiciona o middleware CORS
add_cors_middleware(app)

# Roteador de tasks
task_router = APIRouter(prefix="/api/v1/tasks")
create_task_routes(task_router)

# Roteador de usuários
user_router = APIRouter(prefix="/api/v1/users")
create_user_routes(user_router)

app.include_router(task_router)
app.include_router(user_router)