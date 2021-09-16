from sqlalchemy import Column, Integer, String, Float, DateTime, text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import datetime

from app.database.base_class import Base
from app.common import random_string

class Layer(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    process_id = Column(Integer, ForeignKey('process.id'))
    process = relationship("Process", back_populates="layers")
    cur_image = Column(String, nullable=False)
    input_params = Column(String, nullable=True)
    container = Column(String, nullable=True)
    next_image = Column(String, nullable=True)
    
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.datetime.now)
    finished_at = Column(DateTime(timezone=True), nullable=True)