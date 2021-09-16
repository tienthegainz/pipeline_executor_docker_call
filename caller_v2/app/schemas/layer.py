from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel



class LayerBase(BaseModel):
    cur_image: str
    input_params: Dict[str, Any]
    next_image: Optional[str]



class LayerCreate(LayerBase):
    process_id: int
    input_params: str


class LayerUpdate(LayerBase):
    id: int
    cur_image: Optional[str]
    input_params: Optional[str]
    next_image: Optional[str]
    finished_at: Optional[datetime]


class LayerResponse(LayerBase):
    id: int
    process_id: int
    input_params: str
    created_at: datetime
    updated_at: Optional[datetime]
    class Config:
        orm_mode = True

