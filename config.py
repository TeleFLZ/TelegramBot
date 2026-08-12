import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8451451541:AAGG7qhMu9GvqfwGujGrz-i3MOjm0l-dEMs")
ADMIN_ID = int(os.getenv("5004281510", 0))
DATABASE_URL = os.getenv("t.me", "sqlite:///channels.db")
