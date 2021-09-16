from typing import Optional, List, Dict
from datetime import datetime
from pydantic import BaseModel
from app.schemas.layer import LayerBase, LayerResponse

class ProcessCreate(BaseModel):
    name: Optional[str]


class ProcessUpdate(ProcessCreate):
    name: Optional[str]
    first_image: Optional[int]
    finished_at: Optional[datetime]


class ProcessCreateInput(BaseModel):
    name: Optional[str]
    layers: List[LayerBase]


class ProcessUpdateInput(ProcessCreate):
    id: int
    pass


class ProcessResponse(BaseModel):
    id: int
    name: str
    first_image: Optional[int]
    layers: List[LayerResponse]
    created_at: datetime
    updated_at: Optional[datetime]
    finished_at: Optional[datetime]
    class Config:
        orm_mode = True
