import math

def somar(a: float, b: float) -> float:
    return a + b

def subtrair(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float):
    if b == 0:
        return {"erro": "Divisão por zero não permitida"}
    return a / b

def potencia(a: float, b: float) -> float:
    return a ** b

def raiz(x: float):
    if x < 0:
        return {"erro": "Não existe raiz real de número negativo"}
    return math.sqrt(x)