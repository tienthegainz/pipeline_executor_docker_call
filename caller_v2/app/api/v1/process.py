from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api.deps import get_db

import json
from copy import deepcopy

router = APIRouter()

# TODO: Add file handler

@router.get("", response_model=List[schemas.ProcessResponse])
def read_processes(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all processes.
    """
    processes = crud.process.get_multi(db, skip=skip, limit=limit)
    return processes


@router.post("", response_model=schemas.ProcessResponse)
def create_process(*, db: Session = Depends(get_db), process_in: schemas.ProcessCreateInput) -> Any:
    """
    Create new processes.
    """
    p_input = schemas.ProcessCreate()
    if process_in.name:
        p_input.name = process_in.name
    process = crud.process.create(db, obj_in=p_input)

    _layers = process_in.layers
    layers = []
    for i in range(len(_layers)):
        l = _layers[i]
        l_input = None
        input_params: str = json.dumps(l.input_params)
        if l.next_image:
            l_input = schemas.LayerCreate(
                process_id=process.id,
                cur_image = l.cur_image,
                input_params = input_params,
                next_image = l.next_image,
            )
        else:
            l_input = schemas.LayerCreate(
                process_id=process.id,
                cur_image = l.cur_image,
                input_params = input_params,
            )
        
        layers.append(crud.layer.create(db, obj_in=l_input))
    
    
    process = crud.process.update(db, db_obj=process, obj_in={"first_image": layers[0].id})

    # TODO: start first container here

    return process


@router.put("", response_model=schemas.ProcessResponse)
def update_process(*, db: Session = Depends(get_db), process_in: schemas.ProcessUpdateInput) -> Any:
    """
    Update existing processes.
    """
    process = crud.process.get(db, model_id=process_in.id)
    if not process:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The process with this ID does not exist in the system.",
        )
    process = crud.process.update(db, db_obj=process, obj_in=process_in)
    return process


@router.delete("", response_model=schemas.ProcessResponse)
def delete_process(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Delete existing process.
    """
    process = crud.process.get(db, model_id=id)
    if not process:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The process with this ID does not exist in the system.",
        )
    crud.process.remove(db, model_id=process.id)
    return process
