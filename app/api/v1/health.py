from fastapi import APIRouter, Request
from app.core.settings import get_settings

router = APIRouter()

@router.get("/health")
def health_check(request: Request) -> dict[str, str]:
    settings = get_settings()

    return {
        "status": "ok",
        "app_name": settings.app_name,
        "environment": settings.app_env,
    }

