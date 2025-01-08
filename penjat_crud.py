from sqlalchemy.orm import Session
from sql_model import WordTheme
from typing import List
import random

# Obtener todas las temáticas
def get_all_themes(db: Session) -> List[str]:
    themes = db.query(WordTheme.theme).distinct().all()
    return [theme[0] for theme in themes]

# Obtener una palabra aleatoria para una temática
def get_random_word_for_theme(db: Session, theme: str) -> str:
    words = db.query(WordTheme.word).filter(WordTheme.theme == theme).all()
    return random.choice(words)[0] if words else None
