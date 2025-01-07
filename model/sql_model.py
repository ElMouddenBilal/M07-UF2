from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

BASE = declarative_base()

class User(BASE):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
