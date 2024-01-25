from fastapi import Request
from ytmusicapi import YTMusic

from fasthtmx import HXRouter
from fasthtmx.headers import HXRequestHeaders
from src import templates
from src.controllers.youtube import search_album
from src.models.album import Album
from src.utils.functions import removeFeatFromTracks, secondsToMinutes

router = HXRouter(templates)

yt = YTMusic()


@router.hx_get("/search", "home/components/search_results.html")
def search(request: Request, search: str):
    return search_album(search)


@router.hx_get(
    "/",
    "home/page.html",
    "home/components/poster.html",
    enable_json_route=False,
)
def home(request: Request):
    if request.headers.get(HXRequestHeaders.hx_request):
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
