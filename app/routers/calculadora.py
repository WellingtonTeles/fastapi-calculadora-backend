from fastapi import APIRouter
from app.schemas.operacao_schema import Operacao, Numero
from app.services import calculadora_service as service

import math

router = APIRouter(prefix="/calc", tags=["Calculadora"])

@router.post("/somar")
def somar(op: Operacao):
    return {"resultado": op.a + op.b}

@router.post("/subtrair")
def subtrair(op: Operacao):
    return {"resultado": op.a - op.b}

@router.post("/multiplicar")
def multiplicar(op: Operacao):
    return {"resultado": op.a * op.b}

@router.post("/dividir")
def dividir(op: Operacao):
    if op.b == 0:
        return {"erro": "Divisão por zero não permitida"}
    return {"resultado": op.a / op.b}

@router.post("/potencia")
def potencia(op: Operacao):
    return {"resultado": op.a ** op.b}

@router.post("/raiz")
def raiz(num: Numero):
    if num.x < 0:
        return {"erro": "Não existe raiz real de número negativo"}
    return {"resultado": math.sqrt(num.x)}

@router.post("/porcentagem")
def porcentagem(op: Operacao):
    return {"resultado": (op.a / 100) * op.b}
