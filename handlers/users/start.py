from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
