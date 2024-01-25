from fastapi.routing import APIRouter as __APIRouter

from . import home

router = __APIRouter()
router.include_router(home.router)
