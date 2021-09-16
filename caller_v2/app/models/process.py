from sqlalchemy import Column, Integer, String, Float, DateTime, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.schema import ForeignKey
import datetime

from app.database.base_class import Base
from app.common import random_string

class Process(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    name = Column(String, nullable=False, default=random_string())
    first_image = Column(Integer, default=-1)
    layers = relationship("Layer", back_populates="process")

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.datetime.now)
    finished_at = Column(DateTime(timezone=True), nullable=True)