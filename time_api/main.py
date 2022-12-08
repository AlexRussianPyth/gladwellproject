from fastapi import FastAPI
import uvicorn

from src.api.v1 import users

app = FastAPI(
    title="GladwellTracker",
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

# TODO Endpoint for getting user by user_id

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
