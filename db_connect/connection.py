from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.sql_model import BASE

db_user = 'postgres'
db_port = 5433
db_host = 'localhost'
db_password = 'admin'

uri = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/users'

engine = create_engine(uri)
BASE.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = SessionLocal()

try:
    connection = engine.connect()
    connection.close()
    print('Conectado')
except Exception as e:
    print(f'Error: {str(e)}')

