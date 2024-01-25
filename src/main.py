from fastapi import FastAPI, staticfiles
from fastapi.middleware.cors import CORSMiddleware

from src import app

api = FastAPI()


api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
api.mount("/public", staticfiles.StaticFiles(directory="src/public"), name="public")

api.include_router(app.router)
