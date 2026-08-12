from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from search_engine import search_channels, filter_by_language

async def apply_filters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = context.user_data.get("last_query", "")
    results = search_channels(query)
    filtered = filter_by_language(results, "en")  # пример
    # отдаём отфильтрованный список
