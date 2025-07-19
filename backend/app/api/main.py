from fastapi import APIRouter

from backend.app.api.routes import delays

api_router = APIRouter()

api_router.include_router(delays.router)