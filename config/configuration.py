import os
from dotenv import load_dotenv


load_dotenv()

# Telegram Token for client
TOKEN_BOT = os.getenv('TOKEN_BOT')
# URL
URL = os.getenv('URL')