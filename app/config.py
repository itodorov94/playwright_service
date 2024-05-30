# app/config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./screenshots.db"
SCREENSHOTS_DIR = "screenshots"
Base = declarative_base()

# Synchronous settings for both FastAPI and Celery tasks
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db(Base):
    Base.metadata.create_all(bind=engine)
