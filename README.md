# FastAPI Learning Project 🚀
# FastAPI CRUD Template

This is a beginner-friendly FastAPI project demonstrating async CRUD operations using:


A clean, production-structured FastAPI template with:
- APIRouter with prefix and tags
- Pydantic v2 models (separate models/ folder)
- Dependency injection (API key, pagination)
- Background tasks
- In-memory store (replace with DB of your choice)


# Tech 

* Python 3.12
* FastAPI
* Pydantic
* Async programming
* Fake in-memory database (list of dictionaries)
* Uvicorn

## Structure
app/
├── main.py
├── dependencies.py
├── routers/
│   ├── users.py
│   └── items.py
└── models/
    ├── user.py
    └── item.py

## Run

pip install -r requirements.txt

uvicorn app.main:app --reload

## Test
Visit http://127.0.0.1:8000/docs

Headers

x-api-key: my-secret-api-key


