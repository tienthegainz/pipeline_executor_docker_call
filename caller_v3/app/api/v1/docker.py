from typing import Any, List, Callable

from fastapi import APIRouter, HTTPException, status, BackgroundTasks

from app import schemas
from app.core import docker_client

import json
from copy import deepcopy

router = APIRouter()


@router.get("/images", response_model=schemas.DockerImageRespond)
def get_docker_image() -> Any:
    images_list = docker_client.images.list(all=True)
    return {
      'images': [{'id': image.short_id, 'tags': image.tags} for image in images_list if image.tags]
    }

@router.get("/volumes", response_model=schemas.DockerVolumeRespond)
def get_docker_volume() -> Any:
    volumes_list = docker_client.volumes.list()
    return {
      'volumes': [{'id': volume.short_id, 'name': volume.name} for volume in volumes_list]
    }
