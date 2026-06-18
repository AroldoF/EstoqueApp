from src.emails.dependencies import get_notification_service
from src.emails.schemas.emails import EmailPayload
from src.history.models import NotificationChannel
from src.history.schemas import AlertEventSchema  

from ..broker import broker
from ..events.stock_low import StockLowEvent
from ..exchanges import exchange_stock
from ..queues import stock_low_queue



@broker.subscriber(
    exchange=exchange_stock,
    queue=stock_low_queue
)
async def handler_send_email(event: StockLowEvent):
    """
    Consome o evento de estoque baixo, dispara o e-mail imediatamente
    e retorna o payload de alerta para que o FastStream o publique na fila de histórico.
    """
    try:
        service = get_notification_service()

        # 1. Dispara o e-mail (sua lógica atual)
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

        # 2. Monta o contrato de alerta que o `save_notifications` espera receber
        alert = AlertEventSchema(
            user_id=event.user_id,
            topic="inventory_alerts",
            subject=f"Alerta: Estoque Baixo do produto {event.name_product}",
            recipient=event.email,
            channel=NotificationChannel.EMAIL,
            payload={"name_product": event.name_product, "stock": event.total_items}
        )
        await broker.publish(
            exchange=exchange_stock,
            routing_key="estoque.stock.low.notification",
            message=alert
        )
    except Exception as e:
        print(e)
        ...
