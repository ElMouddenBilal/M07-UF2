from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_model import BASE

db_user = 'postgres'
db_port = 5433
db_host = 'localhost'
db_password = 'admin'
db_name = 'penjat'

uri = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(uri)
BASE.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
