from fastapi import FastAPI
from fastapi_pagination import add_pagination
import uvicorn

from src.api.v1 import users, goals
from src.core.config import settings

app = FastAPI(
    title=settings.timeapi.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)
add_pagination(app)

app.include_router(users.router, prefix=f"{settings.timeapi.path}/users", tags=["users"])
app.include_router(goals.router, prefix=f"{settings.timeapi.path}/goals", tags=["goals"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=settings.timeapi.uvicorn_reload,
        host=settings.timeapi.host,
        port=settings.timeapi.port
    )
