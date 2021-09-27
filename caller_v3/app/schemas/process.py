from typing import Optional, List, Dict
from datetime import datetime
from pydantic import BaseModel
from app.schemas.layer import LayerBase


class ProcessCreateInput(BaseModel):
    layers: List[LayerBase]
    volume: str

class ProcessResponse(BaseModel):
    status: str
