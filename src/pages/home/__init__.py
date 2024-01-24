from typing import Any, Optional

from fastapi import Header, Request
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from pydantic import BaseModel
from ytmusicapi import YTMusic

from src import templates

router = APIRouter()


class Album(BaseModel):
    title: str
    artist: str
    year: int
    cover_url: str
    duration: int
    tracks: list[dict[str, Any]]


def removeFeatFromTracks(tracks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for track in tracks:
        track["title"] = track["title"].split("(")[0]
    return tracks


@router.get("/")
def home(
    request: Request,
    hx_request: Optional[str] = Header(None),
) -> HTMLResponse:
    yt = YTMusic()
    search_results = yt.search("Stoney", filter="albums")
    albumId = search_results[0]["browseId"]
    album_raw = yt.get_album(albumId)
    album = Album(
        title=album_raw["title"].upper(),
        artist=album_raw["artists"][0]["name"],
        year=album_raw["year"],
        cover_url=album_raw["thumbnails"][-1]["url"],
        duration=album_raw["duration_seconds"],
        tracks=removeFeatFromTracks(album_raw["tracks"]),
    )

    context = {"request": request, "album": album}

    if hx_request:
        return templates.TemplateResponse("home/components/table.html", context)

    return templates.TemplateResponse("home/page.html", context)
