from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from search_engine import search_channels

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args) if context.args else None
    if not query:
        await update.message.reply_text("✏️ Напиши /search [название]")
        return

    results = search_channels(query)
    if not results:
        await update.message.reply_text("❌ Ничего не найдено")
        return

    text = f"🔎 *Результаты по запросу*: `{query}`\n\n"
    for ch in results[:10]:
        text += f"📌 [{ch.title}](https://t.me/{ch.username}) — {ch.members} чел.\n"
        if ch.description:
            text += f"   {ch.description[:80]}...\n\n"

    await update.message.reply_text(text, parse_mode="Markdown", disable_web_page_preview=True)
