from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel


class LayerBase(BaseModel):
    order: int
    docker_image: str
    input_params: Dict[str, Any]
