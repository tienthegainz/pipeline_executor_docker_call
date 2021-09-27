from typing import Any, List, Callable

from fastapi import APIRouter, HTTPException, status, BackgroundTasks

from app import schemas
from app.bg_tasks import run_serial_image

import json
from copy import deepcopy

router = APIRouter()


@router.post("", response_model=schemas.ProcessResponse)
async def create_process(*, background_tasks: BackgroundTasks, process: schemas.ProcessCreateInput) -> Any:

    # TODO: start first container here
    background_tasks.add_task(run_serial_image, process.layers, process.volume)

    return {"status": "Running"}
