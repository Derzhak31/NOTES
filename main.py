from fastapi import FastAPI
import uvicorn

from api.routers import router as api_router


app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
