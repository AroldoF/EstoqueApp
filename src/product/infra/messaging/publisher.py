from faststream.rabbit import RabbitBroker
from .broker import broker
from .constants import Exchange, RoutingKey
from .events import LowStockEvent
from .exchange import exchange


async def publish_low_stock(event: LowStockEvent):

    print("evento")
    print(event.model_dump())

    await broker.connect()
    await broker.start()
    await broker.declare_exchange(exchange=exchange)

    await broker.publish(
            message=event.model_dump(),
            exchange=exchange,
            routing_key=RoutingKey.STOCK_KEY,
        )

    return event.model_dump()

  

   