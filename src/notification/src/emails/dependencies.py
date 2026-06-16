from .services.emails import EmailService
from .providers.emails import EmailSender
from config.config import settings

def get_notification_service() -> EmailService:
    sender = EmailSender(settings.smtp)

    service = EmailService(sender=sender)

    return service