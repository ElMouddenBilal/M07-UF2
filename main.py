from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from penjat_crud import get_all_themes, get_random_word_for_theme
from penjat_schema import ThemeResponse, WordResponse
from database import SessionLocal

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para obtener todas las temáticas
@app.get("/penjat/tematica/opcions", response_model=List[ThemeResponse])
def get_themes(db: Session = Depends(get_db)):
    themes = get_all_themes(db)
    return [{"option": theme} for theme in themes]

# Endpoint para obtener una palabra aleatoria para una temática
@app.get("/penjat/tematica/{option}", response_model=List[WordResponse])
def get_word_by_theme(option: str, db: Session = Depends(get_db)):
    word = get_random_word_for_theme(db, option)
    if word:
        return [{"option": word}]
    else:
        return []
