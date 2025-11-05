from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def bot_help(message: types.Message):
    text = (
        "Buyruqlar:",
        "/start - Botni ishga tushirish",
        "/help - Yordam"
    )
    await message.answer("\n".join(text))
