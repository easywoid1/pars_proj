__all__ = ("router")

from aiogram import Router

from .commands import router as commands_router
from .commands.echo import router as echo_router #todo: подумать над упрощением импорта


router = Router(name=__name__)

router.include_router(commands_router)

router.include_router(echo_router) #last