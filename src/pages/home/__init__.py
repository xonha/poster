from typing import Optional

from fastapi import Header, Request
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter

from src import templates

router = APIRouter()


@router.get("/")
def home(
    request: Request,
    hx_request: Optional[str] = Header(None),
) -> HTMLResponse:
    movies = [
        {"title": "The Godfather", "year": 1972},
        {"title": "The Shawshank Redemption", "year": 1994},
        {"title": "Schindler's List", "year": 1993},
        {"title": "Raging Bull", "year": 1980},
        {"title": "Casablanca", "year": 1942},
        {"title": "Citizen Kane", "year": 1941},
        {"title": "Gone with the Wind", "year": 1939},
        {"title": "The Wizard of Oz", "year": 1939},
        {"title": "One Flew Over the Cuckoo's Nest", "year": 1975},
        {"title": "Lawrence of Arabia", "year": 1962},
    ]
    context = {"request": request, "movies": movies}

    if hx_request:
        return templates.TemplateResponse("home/components/table.html", context)

    return templates.TemplateResponse("home/page.html", context)
