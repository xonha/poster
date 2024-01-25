from ytmusicapi import YTMusic

yt = YTMusic()


def search_album(query: str):
    search_results = yt.search(query, filter="albums")
    context = {"search_results": search_results}
    return context
