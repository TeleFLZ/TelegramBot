from sqlalchemy import or_
from database import SessionLocal
from models import Channel

def search_channels(query: str, limit=20):
    db = SessionLocal()
    results = db.query(Channel).filter(
        or_(
            Channel.title.ilike(f"%{query}%"),
            Channel.description.ilike(f"%{query}%"),
            Channel.username.ilike(f"%{query}%")
        )
    ).limit(limit).all()
    return results

def filter_by_language(results, lang="ru"):
    return [c for c in results if c.language == lang]

def filter_by_members(results, min_members=0):
    return [c for c in results if c.members >= min_members]
