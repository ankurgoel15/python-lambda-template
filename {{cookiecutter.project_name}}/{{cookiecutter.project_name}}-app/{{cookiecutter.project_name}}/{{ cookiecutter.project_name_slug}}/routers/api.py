"""{{cookiecutter.project_description}} API Router."""

from fastapi import APIRouter

from ..config import ApiSettings
from .endpoints import health
from .endpoints import swagger

settings = ApiSettings()

api_router = APIRouter()

#Register the routers here.
api_router.include_router(health.router, prefix="/health", tags=["Health"])

if settings.enable_swagger:
    api_router.include_router(swagger.router, tags=["swagger"])