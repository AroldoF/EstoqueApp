from typing import List
from .repositories import NotificationHistoryRepository
from .schemas import NotificationCreateSchema, NotificationResponseSchema

class NotificationHistoryService:
    def __init__(self, repository: NotificationHistoryRepository):
        self.repository = repository or NotificationHistoryRepository()

    async def handle_new_notification(
        self, 
        data: NotificationCreateSchema  
    ) -> NotificationResponseSchema:   
        
        notification = await self.repository.create(data)

        return NotificationResponseSchema.from_orm(notification)