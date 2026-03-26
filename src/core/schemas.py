from ninja import ModelSchema, Schema, Field
from .models import Product
from decimal import Decimal

class ProductRead(Schema):
    name: str
    description: str
    stock: int
    price: Decimal = Field(0)

class ProductUpdate(ModelSchema):
    class Meta:
        model = Product
        fields = '__all__'