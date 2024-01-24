from typing import Any, Optional

from fastapi import Header, Request
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from pydantic import BaseModel
from ytmusicapi import YTMusic

from src import templates

router = APIRouter()

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


@router.get("/test")
def test() -> None:
    print("test")


@router.get("/search")
def search(request: Request):
    search = request.query_params["search"]
    search_results = yt.search(search, filter="albums")
    context = {"request": request, "search_results": search_results}
    return templates.TemplateResponse("home/components/search_results.html", context)


@router.get("/")
def home(
    request: Request,
    hx_request: Optional[str] = Header(None),
) -> HTMLResponse:
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

        return templates.TemplateResponse(
            "home/components/poster.html", {"request": request, "album": album}
        )

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

    context = {"request": request, "album": album}

    return templates.TemplateResponse("home/page.html", context)
