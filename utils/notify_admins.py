import logging
from aiogram import Bot
from data.config import ADMINS


async def on_startup_notify(bot: Bot):
    """Bot ishga tushganda administratorlarga xabar yuboradi"""
    for admin_id in ADMINS:
        try:
            await bot.send_message(admin_id, "✅ Bot muvaffaqiyatli ishga tushdi!")
        except Exception as e:
            logging.error(f"Admin {admin_id} ga xabar yuborishda xatolik: {e}")
