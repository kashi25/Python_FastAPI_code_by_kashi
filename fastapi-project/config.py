from fastapi_sqlalchemy import db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Linking with our PostgresSQL database
DATABASE_URL = "postgresql://postgres:djangohero@localhost/shun"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
