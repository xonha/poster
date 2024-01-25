from typing import Any

from pydantic import BaseModel


class Album(BaseModel):
    title: str
    artist: str
    year: int
    cover_url: str
    duration: int
    duration_minutes: str
    tracks: list[dict[str, Any]]
