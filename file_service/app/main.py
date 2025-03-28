import uvicorn
from fastapi import FastAPI

from app.routers import file_router

app = FastAPI(title="File Service")
app.include_router(file_router.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
