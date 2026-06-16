from .exchanges import exchange_accounts
from  faststream.rabbit import RabbitQueue
from .constants import Queue, RoutingKey

user_created_queue = RabbitQueue(
    name=Queue.USER_CREATED,
    routing_key=RoutingKey.USER_CREATED,
    durable=True,
)

