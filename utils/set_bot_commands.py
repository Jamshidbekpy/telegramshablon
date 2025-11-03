from aiogram import Bot
from aiogram.types import BotCommand


async def set_default_commands(bot: Bot):
    """Botning asosiy buyruqlarini o‘rnatish"""
    commands = [
        BotCommand(command="start", description="🤖 Botni ishga tushurish"),
        BotCommand(command="help", description="ℹ️ Yordam"),
    ]
    await bot.set_my_commands(commands)
