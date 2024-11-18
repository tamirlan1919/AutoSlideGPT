from .start import router as start_router
from .help import router as help_router
from .presentation import router as present_router
from aiogram import Router

router = Router()

router.include_router(start_router)
router.include_router(help_router)
router.include_router(present_router)