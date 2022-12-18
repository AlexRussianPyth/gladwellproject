from fastapi import FastAPI
import uvicorn

from src.api.v1 import users
from src.core.config import settings

app = FastAPI(
    title=settings.timeapi.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)

app.include_router(users.router, prefix=f"{settings.timeapi.path}/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=settings.timeapi.uvicorn_reload,
        host=settings.timeapi.host,
        port=settings.timeapi.port
    )
