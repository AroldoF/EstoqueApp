from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, EmailStr, Field
from .models import NotificationChannel
from typing import Any

# ==========================================
# 1. SCHEMAS DE ENTRADA (INPUT / REQUEST)
# ==========================================

class NotificationCreateSchema(BaseModel):
    """Schema para validar os dados quando uma nova notificação for criada via API ou Fila."""
    user_id: str = Field(..., description="ID do usuário que receberá a notificação")
    topic: str = Field(..., max_length=100, examples=["inventory_alerts", "security_alerts"])
    subject: str = Field(..., max_length=255, examples=["Estoque Baixo: Teclado Mecânico"])
    recipient: str = Field(..., description="E-mail, token de push ou telefone de destino")
    channel: NotificationChannel = Field(default=NotificationChannel.EMAIL)
    payload: Optional[Dict[str, Any]] = Field(None, description="Dados dinâmicos da notificação")


# ==========================================
# 2. SCHEMAS DE SAÍDA (OUTPUT / RESPONSE)
# ==========================================

class NotificationResponseSchema(BaseModel):
    """Schema para mascarar a Model do Tortoise e devolver apenas o necessário para o Frontend."""
    id: int
    user_id: str
    topic: str
    subject: str
    channel: NotificationChannel
    payload: Optional[Dict[str, Any]] = None
    is_read: bool
    created_at: datetime

    class Config:
        # Crucial no Pydantic v2: permite que ele leia os dados direto da model do Tortoise ORM
        from_attributes = True

class AlertEventSchema(BaseModel):
    user_id: str
    topic: str
    subject: str
    recipient: str
    channel: NotificationChannel = NotificationChannel.EMAIL
    payload: dict[str, Any]|None = None