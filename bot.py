import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from database import init_db
from handlers.start import start
from handlers.search import search
from handlers.stats import stats
from handlers.filters import apply_filters

init_db()

logging.basicConfig(level=logging.INFO)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("search", search))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CallbackQueryHandler(apply_filters))

print("✅ Бот-поисковик каналов запущен")
app.run_polling()
