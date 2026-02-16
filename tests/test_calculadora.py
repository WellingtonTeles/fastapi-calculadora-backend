from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_somar():
    response = client.post("/calc/somar", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"resultado": 15}

def test_subtrair():
    response = client.post("/calc/subtrair", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"resultado": 5}

def test_multiplicar():
    response = client.post("/calc/multiplicar", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"resultado": 50}

def test_dividir():
    response = client.post("/calc/dividir", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"resultado": 2}

def test_dividir_por_zero():
    response = client.post("/calc/dividir", json={"a": 10, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"erro": "Divisão por zero não permitida"}