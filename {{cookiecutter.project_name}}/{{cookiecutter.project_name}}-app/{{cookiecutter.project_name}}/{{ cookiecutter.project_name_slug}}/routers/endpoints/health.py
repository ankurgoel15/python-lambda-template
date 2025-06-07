"""{{cookiecutter.project_description}} health-check endpoint."""

from fastapi import APIRouter
from loguru import logger

from ...common import timeit

router = APIRouter()

@router.get("/health-check")
@timeit
def get_health():
    return {"Status": "Healthy"}