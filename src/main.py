from fastapi import FastAPI, staticfiles
from fastapi.middleware.cors import CORSMiddleware

from src import pages

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/public", staticfiles.StaticFiles(directory="src/public"), name="public")

app.include_router(pages.router)
