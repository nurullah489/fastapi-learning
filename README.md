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
uvicorn app.main:app --reload

## Test
Visit http://127.0.0.1:8000/docs

Headers

x-api-key: my-secret-api-key

<<<<<<< HEAD
=======
Learning Goals

* Understand FastAPI async routes
* Use Pydantic models
* Implement CRUD operations
* Work with dependencies





\## 📂 Features



\- Create user/item

\- Read users/items

\- Update user/item

\- Delete user/item

\- Pagination support

\- API Key header validation



\---



\## ⚙️ Tech Stack



\- FastAPI

\- Pydantic

\- Uvicorn



\---



\## 📌 Example API Endpoints for user



| Method | Endpoint          | Description        |

|--------|-------------------|--------------------|

| GET    | /users            | Get all users      |

| GET    | /users/{user_id}  | Get user by ID     |

| POST   | /users            | Create new user    |

| PUT    | /users/{user_id}  | Update user        |

| DELETE | /users/{user_id}  | Delete user        |



\---



Headers

x-api-key: my-secret-api-key


\## ▶️ Run Locally



```bash
>>>>>>> 8c52892d29db24e2756294a0da6f12dcf60b070f

pip install -r requirements.txt

uvicorn main:app --reload


<<<<<<< HEAD


=======
>>>>>>> 8c52892d29db24e2756294a0da6f12dcf60b070f
