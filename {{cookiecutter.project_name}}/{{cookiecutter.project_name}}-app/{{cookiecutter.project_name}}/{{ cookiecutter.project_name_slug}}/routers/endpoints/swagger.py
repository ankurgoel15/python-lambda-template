from fastapi.openapi.docs import (
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.responses import RedirectResponse
from fastapi.routing import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse

from ...service.swagger_services import get_swagger_html

router = APIRouter


@router.get("/swagger/index.html", include_in_schema=False)
async def swagger_ui_html(req: Request) -> HTMLResponse:
    root_path = req.scope.get("root_path", "").rstrip("/")
    swagger_html = get_swagger_html(root_path)
    return HTMLResponse(swagger_html)


@router.get("/", include_in_schema=False)
@router.get("/docs", include_in_schema=False)
@router.get("/swagger", include_in_schema=False)
def redirect_to_swagger():
    response = RedirectResponse(url="/swagger/index.html")
    return response


@router.get("/swagger/oauth2-redirect.html", include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()
