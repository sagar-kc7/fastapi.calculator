from fastapi import FastAPI, Query, HTTPException
from .config import settings

app = FastAPI(title=settings.app_name, version=settings.version)


@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.app_name}!"}


@app.get("/add")
def add(a: float = Query(...), b: float = Query(...)):
    return {"result": a + b}


@app.get("/subtract")
def subtract(a: float = Query(...), b: float = Query(...)):
    return {"result": a - b}


@app.get("/multiply")
def multiply(a: float = Query(...), b: float = Query(...)):
    return {"result": a * b}


@app.get("/divide")
def divide(a: float = Query(...), b: float = Query(...)):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}
