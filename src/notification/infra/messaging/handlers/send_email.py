from src.emails.dependencies import get_notification_service
from src.emails.schemas.emails import EmailPayload
from ..events.user_created import UserCreatedEvent
from ..broker import broker
from ..exchanges import exchange_accounts
from ..queues import user_created_queue

@broker.subscriber(
    exchange=exchange_accounts,
    queue=user_created_queue
)
async def handler_send_email(event: UserCreatedEvent):
    service = get_notification_service()

    await service.send_email(
        payload=EmailPayload(
            subject="Confirme seu email",
            template_name="confirm_email.html",
            to_email=event.email,
            to_first_name=event.first_name,
            confirmation_url=event.confirmation_url,
            context={
                "first_name": event.first_name,
                "confirmation_url": event.confirmation_url
            }
        )
    )