from typing import Protocol
from pydantic import BaseModel

class SenderProtocol[T: BaseModel](Protocol):
    async def send(self, notification: T) -> bool: ...