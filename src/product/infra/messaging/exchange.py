from faststream.rabbit import RabbitExchange, ExchangeType
from .constants import Exchange

exchange = RabbitExchange(Exchange.STOCK, type=ExchangeType.TOPIC)