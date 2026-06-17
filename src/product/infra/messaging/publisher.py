from faststream.rabbit import RabbitExchange

from .broker import broker
from .constants import Exchange, RoutingKey
from .events import LowStockEvent

exchange = RabbitExchange(Exchange.STOCK)

async def publish_low_stock(event: LowStockEvent):

    
    print("evento")
    print(event.model_dump())

    
    async with broker:
       
       await broker.publish(
            message=event.model_dump(),
            exchange=exchange,
            routing_key=RoutingKey.STOCK_KEY,
        )

  

    # print("publicado")