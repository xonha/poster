import os
from typing import Any


def removeFeatFromTracks(tracks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for track in tracks:
        track["title"] = track["title"].split("(")[0]
    return tracks


def secondsToMinutes(seconds: int) -> str:
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds}"

