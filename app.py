import asyncio
# from aiogram import Bot, Dispatcher
from loader import bot, dp

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def on_startup():
    """Bot ishga tushganda bajariladigan funksiyalar"""
    # Asosiy komandalarni o'rnatish
    await set_default_commands(bot)

    # Adminlarga xabar yuborish
    await on_startup_notify(dp)

    print("✅ Bot muvaffaqiyatli ishga tushdi!")


async def main():
    # Botni ishga tushirish
    await on_startup()
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
