from ninja import Schema, Field
from decimal import Decimal
from datetime import datetime

class ProductRead(Schema):
    id: int
    name: str
    sku: str
    description: str
    stock: int
    price: Decimal = Field(Decimal(0))
    created_at: datetime
    is_active: bool

class ProductCreate(Schema):
    name: str
    sku: str
    description: str
    stock: int
    price: Decimal = Field(Decimal(0))
    is_active: bool

class ProductUpdate(Schema):
    name: str | None = None
    sku: str | None = None
    description: str | None = None
    stock: int | None = None
    price: Decimal | None = None
    is_active: bool | None = None
