from faststream.rabbit import RabbitExchange, ExchangeType
from .constants import Exchange

exchange_stock = RabbitExchange(
    name=Exchange.STOCK,
    type=ExchangeType.TOPIC,
    durable=True
)