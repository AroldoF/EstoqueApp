from enum import StrEnum
from tortoise import fields
from tortoise.models import Model


class NotificationChannel(StrEnum):
    EMAIL = 'email'
    PUSH = 'push'

class NotificationHistory(Model):
    id = fields.IntField(primary_key=True)
    user_id = fields.CharField(
        max_length=255
    ) 
    topic = fields.CharField(max_length=100)  # Ex: "inventory", "security"
    subject = fields.CharField(max_length=255)  # Ex: "Alerta de Estoque Baixo"

    channel = fields.CharEnumField(NotificationChannel, max_length=50, default=NotificationChannel.EMAIL)
    recipient = fields.CharField(
        max_length=255
    )  # Guarda o e-mail ou telefone que recebeu

    payload = fields.JSONField(
        null=True
    )  # Ex: {"product_id": 99, "product_name": "Teclado"}

    created_at = fields.DatetimeField(auto_now_add=True)
    is_read = fields.BooleanField(
        default=False
    ) 