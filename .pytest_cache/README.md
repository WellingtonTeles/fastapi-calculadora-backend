# pytest cache directory #

# FastAPI Calculadora — Backend

Este projeto é uma API de calculadora desenvolvida com **FastAPI**, organizada em **camadas profissionais** (routers, services, schemas) e com **testes automatizados** utilizando `pytest`.  
O objetivo é demonstrar boas práticas de arquitetura, organização e qualidade de código em aplicações Python modernas.

---

## 🚀 Tecnologias utilizadas

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **Pytest**
- **GitHub Actions** (CI)
- **HTTPX** (para testes)

---

## 🧱 Arquitetura em camadas

A aplicação segue uma arquitetura limpa e modular:
# app/ ├── main.py              
# Inicialização da aplicação ├── routers/             
# Controladores HTTP ├── schemas/             
# Validação e tipagem (Pydantic) ├── services/            
# Regras de negócio └── init.py


### ✔ Benefícios

- Código mais limpo e organizado  
- Fácil manutenção  
- Testes mais simples  
- Separação clara de responsabilidades  
- Escalabilidade

---

## 📁 Estrutura do projeto

# fastapi-calculadora-backend/ │
# ├── app/ │
#    ├── main.py │
#    ├── routers/ │   │
#    └── calculadora_router.py │
#    ├── schemas/ │
#    │   └── operacao_schema.py │
#    ├── services/ │   │
#    └── calculadora_service.py │
#  ├── tests/ │
#    └── test_calculadora.py │
#  ├── .github/ │
#    └── workflows/ │
#        └── tests.yml │
#  ├── .gitignore └── README.md

---

## ▶️ Como executar o projeto localmente

### 1. Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


2. Instalar dependências
pip install -r requirements.txt


3. Rodar o servidor
uvicorn app.main:app --reload


Acesse:
http://127.0.0.1:8000/docs



🧪 Executando os testes
pytest -q



🔄 Integração Contínua (GitHub Actions)
Este repositório possui um workflow que:
- Instala dependências
- Executa os testes
- Valida o build
Arquivo: .github/workflows/tests.yml

📌 Endpoints principais
POST /calc/somar
{
  "a": 10,
  "b": 5
}


POST /calc/subtrair
POST /calc/multiplicar
POST /calc/dividir
POST /calc/potencia
POST /calc/raiz
Documentação completa em:
/docs



📄 Licença
Este projeto está sob a licença MIT.
Sinta-se livre para usar, estudar e contribuir.

---

# 🇺🇸 **README — en_US**

```markdown
# FastAPI Calculator — Backend

This project is a calculator API built with **FastAPI**, following a **professional layered architecture** (routers, services, schemas) and including **automated tests** using `pytest`.  
The goal is to demonstrate clean code practices, modular design, and high‑quality backend development in Python.

---

## 🚀 Technologies

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **Pytest**
- **GitHub Actions** (CI)
- **HTTPX**

---

## 🧱 Layered Architecture

The application follows a clean and modular structure:


# app/ 
#├── main.py              
# Application entrypoint 
#├── routers/             
# HTTP controllers 
#├── schemas/             
# Data validation (Pydantic) 
#├── services/            
# Business logic └── init.py

### ✔ Benefits

- Clean and maintainable code  
- Clear separation of concerns  
- Easier testing  
- Scalable structure  

---

## 📁 Project structure


# fastapi-calculadora-backend/ │
# ├── app/ │
#    ├── main.py │
#    ├── routers/ │   │
#    └── calculadora_router.py │
#    ├── schemas/ │
#    │   └── operacao_schema.py │
#    ├── services/ │   │
#    └── calculadora_service.py │
#  ├── tests/ │
#    └── test_calculadora.py │
#  ├── .github/ │
#    └── workflows/ │
#        └── tests.yml │
#  ├── .gitignore └── README.md

---

## ▶️ Running locally

### 1. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


2. Install dependencies
pip install -r requirements.txt


3. Start the server
uvicorn app.main:app --reload


Open:
http://127.0.0.1:8000/docs



🧪 Running tests
pytest -q



🔄 Continuous Integration (GitHub Actions)
This repository includes a workflow that:
- Installs dependencies
- Runs automated tests
- Validates the build
Workflow file: .github/workflows/tests.yml

📌 Main endpoints
POST /calc/somar
{
  "a": 10,
  "b": 5
}


POST /calc/subtrair
POST /calc/multiplicar
POST /calc/dividir
POST /calc/potencia
POST /calc/raiz
Full documentation available at:
/docs



📄 License
This project is licensed under the MIT License.
Feel free to use, study, and contribute.






**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.
