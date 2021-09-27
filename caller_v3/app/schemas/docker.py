from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel


class DockerImageBase(BaseModel):
    id: str
    tags: List[str]

class DockerVolumeBase(BaseModel):
    id: str
    name: str

class DockerImageRespond(BaseModel):
    images: List[DockerImageBase]

class DockerVolumeRespond(BaseModel):
    volumes: List[DockerVolumeBase]
