from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from handlers.users.start import router as start_router
from handlers.users.help import router as help_router
from handlers.users.echo import router as echo_router

from data import config

# Default xususiyatlar orqali parse_mode ni o‘rnatamiz
bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(help_router)
dp.include_router(echo_router)

