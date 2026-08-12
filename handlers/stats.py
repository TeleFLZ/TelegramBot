from telegram import Update
from telegram.ext import ContextTypes
from database import SessionLocal
from models import Channel
from config import ADMIN_ID

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Только для админа")
        return
    db = SessionLocal()
    total = db.query(Channel).count()
    await update.message.reply_text(f"📊 Всего каналов в базе: {total}")
