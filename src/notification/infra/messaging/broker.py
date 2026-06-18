from faststream import FastStream
from faststream.rabbit import RabbitBroker
from config.config import settings
from src.history.database import init_db, close_db

broker = RabbitBroker(settings.messaging_url)

# handlers
from .handlers.send_email import handler_send_email
from .handlers.save_notification import save_notifications_handler
app = FastStream(broker)

@app.on_startup
async def startup():
    await init_db()

@app.on_shutdown
async def shutdown():
    await close_db()

