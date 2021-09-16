from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.process import Process
from app.schemas import ProcessCreate, ProcessUpdate


class CRUDProcess(CRUDBase[Process, ProcessCreate, ProcessUpdate]):
    # Declare model specific CRUD operation methods.
    pass


process = CRUDProcess(Process)
