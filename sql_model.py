from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()

class WordTheme(BASE):
    __tablename__ = 'words_themes'
    
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, index=True)
    theme = Column(String)
