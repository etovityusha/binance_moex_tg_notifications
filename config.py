import os

from dotenv import load_dotenv

load_dotenv()

MIN_PROFIT_FOR_NOTIFICATION = 5

TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
