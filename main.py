# main.py
from fastapi import FastAPI
from app.api.endpoints import router
from app.api.database import engine

app = FastAPI()

app.include_router(router, prefix="/api")

# No need for database connect/disconnect with the engine, as we're not using the databases module
