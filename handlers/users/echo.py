from aiogram import Router, types

router = Router()

# Echo bot
@router.message()
async def bot_echo(message: types.Message):
    await message.answer(message.text)
