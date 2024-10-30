from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor 
import time
from .config import settings


SLQALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SLQALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Attempt to establish a connection to a PostgreSQL database using psycopg2.
# RealDictCursor allows rows to be returned as dictionaries.
# try:
#     conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#     password='Hunter18!!', cursor_factory=RealDictCursor)  # Insert your DB password here
#     cursor = conn.cursor()
#     print("Database connection was successful!")
# except Exception as error:
#     Catch and print any errors during the connection attempt
#     print("Connecting to database failed")
#     print('Error: ', error)