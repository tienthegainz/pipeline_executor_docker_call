from fastapi import APIRouter

from app.api.v1 import process

api_router = APIRouter()
api_router.include_router(process.router, prefix="/processes", tags=["processes"])
