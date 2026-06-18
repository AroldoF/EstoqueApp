from .models import NotificationHistory
from .schemas import NotificationCreateSchema


class NotificationHistoryRepository:
    async def create(
        self, 
        data: NotificationCreateSchema
    ) -> NotificationHistory:
        """Salva uma nova notificação no histórico."""
        return await NotificationHistory.create(
            **data.model_dump()
        )