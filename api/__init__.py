from fastapi import APIRouter
from api.views import router as notes_router

router = APIRouter()
router.include_router(notes_router)
