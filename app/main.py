from fastapi import FastAPI
from app.routes.analysis import router

app = FastAPI()
app.include_router(router, prefix="/api")
