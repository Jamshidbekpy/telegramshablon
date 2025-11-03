from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
ADMINS: list[str] = os.getenv("ADMINS", "").split(",")
IP_ADDRESS: str = os.getenv("IP", "127.0.0.1")
