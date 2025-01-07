from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    surname: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
