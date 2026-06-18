from .services import NotificationHistoryService
from .repositories import NotificationHistoryRepository

def get_notification_history_service() -> NotificationHistoryService:
    repository = NotificationHistoryRepository()
    service = NotificationHistoryService(repository)
    return service