import requests
from bs4 import BeautifulSoup
from database import SessionLocal
from models import Channel

def parse_telegram_channel(username: str):
    # имитация сбора данных (реальный парсинг требует аккаунт + API)
    return {
        "username": username,
        "title": f"Channel {username}",
        "description": "Описание канала",
        "members": 1234,
        "language": "ru",
        "category": "news"
    }

def save_channel(data):
    db = SessionLocal()
    channel = Channel(**data)
    db.add(channel)
    db.commit()
