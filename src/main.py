from contextlib import asynccontextmanager
from src.db import init_db
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
	init_db()
	yield


app = FastAPI(title="VaultDrop", lifespan=lifespan)

app.include_router(router)

@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=400, content={"detail": "Invalid input"})

@app.get("/health")

def health():
	return {"status": "ok"}
