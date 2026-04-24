\# FastAPI Learning Project 🚀



This is a beginner-friendly FastAPI project demonstrating async CRUD operations using:



* Python 3.12
* FastAPI
* Pydantic
* Async programming
* Fake in-memory database (list of dictionaries)



\---



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



| Method | Endpoint       | Description        |

|--------|--------------|--------------------|

| GET    | /users       | Get all users      |

| GET    | /users/{id}  | Get user by ID     |

| POST   | /users       | Create new user    |

| PUT    | /users/{id}  | Update user        |

| DELETE | /users/{id}  | Delete user        |



\---



\## ▶️ Run Locally



```bash

pip install -r requirements.txt

uvicorn main:app --reload



Headers

x-api-key: my-secret-api-key

