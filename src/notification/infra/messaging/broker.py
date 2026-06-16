from faststream import FastStream
from faststream.rabbit import RabbitBroker
from config.config import settings

broker = RabbitBroker(settings.messaging_url)
app = FastStream(broker)

# handlers
from .handlers.send_email import handler_send_email