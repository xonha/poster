from fastapi.routing import APIRouter as __APIRouter

from . import home

router = __APIRouter(tags=["Pages"])
router.include_router(home.router)
