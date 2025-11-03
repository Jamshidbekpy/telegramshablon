import asyncio
import logging
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.exceptions import TelegramRetryAfter
from typing import Callable, Dict, Any, Awaitable


class ThrottlingMiddleware(BaseMiddleware):
    """
    Simple anti-flood middleware for aiogram 3.x
    """

    def __init__(self, limit: float = 1.0):
        super().__init__()
        self.limit = limit
        self._users: Dict[int, float] = {}

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id
        now = asyncio.get_event_loop().time()

        # Agar foydalanuvchi tez-tez yuborayotgan bo‘lsa
        if user_id in self._users and now - self._users[user_id] < self.limit:
            logging.warning(f"Flood detected from user {user_id}")
            await event.answer("⛔ Juda tez yozayapsan, biroz kut!")
            return  # handler chaqirilmaydi

        # Agar ruxsat etilgan bo‘lsa, vaqtni yangilaymiz
        self._users[user_id] = now
        return await handler(event, data)
