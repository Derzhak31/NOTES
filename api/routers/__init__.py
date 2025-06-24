from fastapi import APIRouter
from api.routers.notes import router as notes_router
from api.routers.users import router as users_router

router = APIRouter()
router.include_router(notes_router)
router.include_router(users_router)
