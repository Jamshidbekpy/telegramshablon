import asyncio
from aiogram import Bot, Dispatcher
from loader import bot, dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import middlewares, filters, handlers


async def on_startup():
    """
    Bot ishga tushganda avtomatik bajariladigan funksiyalar
    """
    await set_default_commands(dp)
    await on_startup_notify(dp)
    print("✅ Bot muvaffaqiyatli ishga tushdi!")


async def main():
    await on_startup()
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
