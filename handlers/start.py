from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔍 Найти канал", callback_data="search")],
        [InlineKeyboardButton("📊 Популярные", callback_data="top")],
        [InlineKeyboardButton("🎯 По категориям", callback_data="categories")],
    ]
    await update.message.reply_text(
        "📡 *Бот для поиска каналов и чатов Telegram*\n\n"
        "Я ищу по названию, описанию и тегам.\n"
        "Выбери действие:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
