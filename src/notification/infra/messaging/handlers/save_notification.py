from ..broker import broker
from src.history.dependencies import get_notification_history_service
from ..exchanges import exchange_stock
from ..queues import save_notification_queue
from src.history.schemas import AlertEventSchema, NotificationCreateSchema

@broker.subscriber(
    exchange=exchange_stock,
    queue=save_notification_queue
)
async def save_notifications_handler(event: AlertEventSchema):
    service = get_notification_history_service()
    await service.handle_new_notification(NotificationCreateSchema(**event.model_dump()))