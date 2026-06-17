from src.emails.dependencies import get_notification_service
from src.emails.schemas.emails import EmailPayload
from ..events.stock_low import StockLowEvent
from ..broker import broker
from ..exchanges import exchange_stock
from ..queues import stock_low_queue

@broker.subscriber(
    exchange=exchange_stock,
    queue=stock_low_queue
)
async def handler_send_email(event: StockLowEvent):
    service = get_notification_service()

    await service.send_email(
        payload=EmailPayload(
            subject="Alerta de estoque",
            template_name="stock_low.html",
            to_email=event.email,
            name_product=event.name_product,
            total_items=event.total_items,
            context={
                "name_product": event.name_product,
                "total_items": event.total_items
            }
        )
    )