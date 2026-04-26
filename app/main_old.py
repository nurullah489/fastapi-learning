from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi import HTTPException

app = FastAPI(
    title="FastAPI Learning Template",
    description="A template for building FastAPI applications.",
    version="1.0.0",
)

# root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Learning Template!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Now run in terminal 
# (make sure you are in the correct directory with the app.main module and the environment is activated):
# uvicorn app.main:app --reload

# if the following three urls are working, then the app is running successfully:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redocs

# Path Parameters
""" @app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"} """

# now run the following url to test the new endpoint:
# http://127.0.0.1:8000/users/15
# and
# http://127.0.0.1:8000/users/abc
# The first one should return a user object with user_id 123,
# while for the second one FastAPI auto-validates the type and should return a 422 Unprocessable Entity error 
# because the user_id is not an integer.
 
# Query Parameters
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10, search: str | None = None):
    return {
        "skip": skip,
        "limit": limit,
        "search": search,  
    }
    
# Now test if the following url is working:
# http://127.0.0.1:8000/items?skip=0&limit=5&search=laptop

# Pydantic Models (request body)


class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    active: bool = True
    
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    active: bool

# In-memory store (we'll replace with DB later)
fake_db: list[dict] = []

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    new_user = {
        "id": len(fake_db) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "active": user.active,
    }
    fake_db.append(new_user)
    return new_user

@app.get("/users", response_model=list[UserResponse])
def list_users():
    return fake_db

# Now Test in Swagger UI — 
# go to POST /users, click Try it out, submit a user,
# then hit GET /users to see it listed

# Full CRUD + HTTP Exceptions


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in fake_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail = f"User {user_id} not found")

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserCreate):
    for user in fake_db:
        if user["id"] == user_id:
            user["name"] = user_update.name
            user["email"] = user_update.email
            user["age"] = user_update.age
            user["active"] = user_update.active
            return user
    raise HTTPException(status_code=404, detail = f"User {user_id} not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(fake_db):
        if user["id"] == user_id:
            del fake_db[index]   # or fake_db.pop(index)
            return {"detail": f"User {user_id} deleted"}
    raise HTTPException(status_code=404, detail = f"User {user_id} not found")