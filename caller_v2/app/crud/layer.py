from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.layer import Layer
from app.schemas import LayerCreate, LayerUpdate


class CRUDLayer(CRUDBase[Layer, LayerCreate, LayerUpdate]):
    # Declare model specific CRUD operation methods.
    pass


layer = CRUDLayer(Layer)
