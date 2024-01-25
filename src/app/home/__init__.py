from functools import wraps
from typing import Any, Optional

from fastapi import Header, Request
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from ytmusicapi import YTMusic

from src import templates


class HTMXRouter(APIRouter):
    def __init__(self, templates: Jinja2Templates, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.templates = templates

    def hx_get(
        self,
        path: str,
        template: str,
        hx_template: str = "",
        api_prefix: str = "api",
        *args,
        **kwargs,
    ):
        """
        Extended APIRouter.get method with additional parameters.

        Parameters:
        - path (str): The endpoint path.
        - template (str): Optional template name.
        - hx_template (Optional[str]): Optional HX template name for partial page updates based on the HX-Request Header.
        - api_prefix (Optional[str]): The API prefix to use for the endpoint and tag separated by a slash.
            - Example: "api/v4"
        - **kwargs: Additional keyword arguments, same as APIRouter.get.
        """

        def decorator(func):
            @self.get(path, *args, **kwargs)
            @wraps(func)
            def html_route(*args, **kwargs):
                response = func(*args, **kwargs)
                context = {"request": kwargs["request"], **response}

                if hx_template and kwargs["request"].headers.get("HX-Request"):
                    return self.templates.TemplateResponse(hx_template, context)

                return self.templates.TemplateResponse(template, context)

            @self.get(
                f"/{api_prefix}{path}",
                *args,
                **kwargs,
                tags=[api_prefix.upper()],
            )
            @wraps(func)
            def json_route(*args, **kwargs):
                response = func(*args, **kwargs)
                return response

        return decorator


router = HTMXRouter(templates)

yt = YTMusic()


def secondsToMinutes(seconds: int) -> str:
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds}"


class Album(BaseModel):
    title: str
    artist: str
    year: int
    cover_url: str
    duration: int
    duration_minutes: str
    tracks: list[dict[str, Any]]


def removeFeatFromTracks(tracks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for track in tracks:
        track["title"] = track["title"].split("(")[0]
    return tracks


@router.hx_get("/search", "home/components/search_results.html")
def search(request: Request, search: str):
    search_results = yt.search(search, filter="albums")
    context = {"search_results": search_results}
    return context


@router.hx_get("/", "home/page.html", "home/components/poster.html")
def home(
    request: Request,
    hx_request: Optional[str] = Header(None),
):
    if hx_request:
        album_id = request.query_params["browseId"]
        album_raw = yt.get_album(album_id)
        album = Album(
            title=album_raw["title"].upper().split("(")[0],
            artist=album_raw["artists"][0]["name"],
            year=album_raw["year"],
            cover_url=album_raw["thumbnails"][-1]["url"],
            duration=album_raw["duration_seconds"],
            duration_minutes=secondsToMinutes(album_raw["duration_seconds"]),
            tracks=removeFeatFromTracks(album_raw["tracks"]),
        )

        return {"album": album}

    search_results = yt.search("Stoney", filter="albums")
    albumId = search_results[0]["browseId"]
    album_raw = yt.get_album(albumId)
    album = Album(
        title=album_raw["title"].upper().split("(")[0],
        artist=album_raw["artists"][0]["name"],
        year=album_raw["year"],
        cover_url=album_raw["thumbnails"][-1]["url"],
        duration=album_raw["duration_seconds"],
        duration_minutes=secondsToMinutes(album_raw["duration_seconds"]),
        tracks=removeFeatFromTracks(album_raw["tracks"]),
    )

    context = {"album": album}
    return context
