from loader import dp
from .throttling import ThrottlingMiddleware

def setup_middlewares():
    dp.message.middleware(ThrottlingMiddleware())

setup_middlewares()