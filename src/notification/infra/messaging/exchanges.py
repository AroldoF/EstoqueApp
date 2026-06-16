from faststream.rabbit import RabbitExchange, ExchangeType
from .constants import Exchange

exchange_accounts = RabbitExchange(
    name=Exchange.ACCOUNTS,
    type=ExchangeType.TOPIC,
    durable=True
)