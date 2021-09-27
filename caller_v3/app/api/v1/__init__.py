from fastapi import APIRouter

from app.api.v1 import process, docker

api_router = APIRouter()
api_router.include_router(process.router, prefix="/processes", tags=["processes"])
api_router.include_router(docker.router, prefix="/docker", tags=["docker"])