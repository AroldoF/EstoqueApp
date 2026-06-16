# src/modules/emails/services/emails.py
from src.utils.interfaces.senders import SenderProtocol
from ..schemas.emails import EmailPayload

class EmailService:
    def __init__(self, sender: SenderProtocol[EmailPayload]):
        self.sender = sender

    async def send_email(self, payload: EmailPayload) -> None:

        await self.sender.send(payload)