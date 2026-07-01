from fastapi import APIRouter
from app.api.v1.schema import router as schema_router
from app.api.v1.health import router as health_router
from app.api.v1.ask import router as ask_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(ask_router)
api_router.include_router(schema_router)
