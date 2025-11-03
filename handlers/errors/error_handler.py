import logging
from aiogram import Router
from aiogram.types import Update
from aiogram.exceptions import (
    TelegramAPIError,
    TelegramBadRequest,
    TelegramUnauthorizedError,
    TelegramForbiddenError,
    TelegramRetryAfter,
)

router = Router()
logger = logging.getLogger(__name__)


@router.errors()
async def errors_handler(update: Update, exception: Exception):
    """
    Global error handler for aiogram 3.x
    """
    # RetryAfter (rate limit)
    if isinstance(exception, TelegramRetryAfter):
        logger.warning(f"Flood control: retry after {exception.retry_after} seconds.")
        return True

    # Unauthorized / Forbidden
    if isinstance(exception, (TelegramUnauthorizedError, TelegramForbiddenError)):
        logger.error(f"Access error: {exception}")
        return True

    # BadRequest (invalid message edits, empty text, etc.)
    if isinstance(exception, TelegramBadRequest):
        logger.warning(f"Bad request: {exception}")
        return True

    # API-level errors
    if isinstance(exception, TelegramAPIError):
        logger.error(f"Telegram API error: {exception}")
        return True

    # Unexpected exceptions
    logger.exception(f"Unexpected error: {exception}\nUpdate: {update}")
    return True
