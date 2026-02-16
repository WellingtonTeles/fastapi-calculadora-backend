from fastapi import FastAPI
from app.routers import calculadora

app = FastAPI()

app.include_router(calculadora.router)

@app.get("/")
def root():
    return {"status": "API funcionando!"}

app.include_router(calculadora.router)
