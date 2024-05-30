# app/models.py
from sqlalchemy import Column, String
from .config import Base

class Screenshot(Base):
    __tablename__ = "screenshots"
    id = Column(String, primary_key=True, index=True)
    urls = Column(String)
