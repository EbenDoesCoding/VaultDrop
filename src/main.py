from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
	init_db()
	yield


app = FastAPI(title="VaultDrop", lifespan=lifespan)

@app.get("/health")

def health():
	return {"status": "ok"}
