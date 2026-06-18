from .exchanges import exchange_stock
from  faststream.rabbit import RabbitQueue
from .constants import Queue, RoutingKey

stock_low_queue = RabbitQueue(
    name=Queue.STOCK_LOW,
    routing_key=RoutingKey.STOCK_KEY,
    durable=True,
)

save_notification_queue = RabbitQueue(
    name=Queue.SAVE_NOTIFICATION,
    routing_key=RoutingKey.NOTIFICATION,
    durable=True,
)
