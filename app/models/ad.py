from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db import Base

class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner = Column(String(100), nullable=False)
