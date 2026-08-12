from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Channel(Base):
    __tablename__ = "channels"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    title = Column(String)
    description = Column(String, nullable=True)
    members = Column(Integer, default=0)
    is_private = Column(Boolean, default=False)
    language = Column(String, default="ru")
    category = Column(String, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow)
    rating = Column(Float, default=0.0)
