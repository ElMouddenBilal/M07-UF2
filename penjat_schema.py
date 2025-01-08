from pydantic import BaseModel
from typing import List

class ThemeResponse(BaseModel):
    option: str

    class Config:
        orm_mode = True

class WordResponse(BaseModel):
    option: str

    class Config:
        orm_mode = True
