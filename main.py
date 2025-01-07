from fastapi import FastAPI, HTTPException
from typing import List
from schemas.users_sch import UserCreate, UserUpdate, User
from crud.users import read_users, create_user, update_user, delete_user

app = FastAPI()

@app.get("/users", response_model=List[User])
async def get_users():
    try:
        users = read_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/users", response_model=User)
async def add_user(user: UserCreate):
    try:
        user_id = create_user(user.name, user.surname)
        return {"id": user_id, "name": user.name, "surname": user.surname}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/users/{user_id}", response_model=dict)
async def modify_user(user_id: int, user: UserUpdate):
    try:
        message = update_user(user_id, user.name, user.surname)
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/users/{user_id}", response_model=dict)
async def remove_user(user_id: int):
    try:
        message = delete_user(user_id)
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
