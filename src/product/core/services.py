from django.shortcuts import get_object_or_404
from .models import Product
from . import schemas
import asyncio
from asgiref.sync import  sync_to_async

from infra.messaging.publisher import publish_low_stock
from infra.messaging.events import LowStockEvent

def list_product(request):
    user_id = request.auth["user_id"]
    return Product.objects.filter(user_id=user_id)

def create_product(request, payload: schemas.ProductCreate) -> Product:
    user_id = request.auth["user_id"]
    return Product.objects.create(user_id=user_id, **payload.dict())

def get_product(request, product_id: int) -> Product:
    user_id = request.auth["user_id"]
    return get_object_or_404(Product, pk=product_id, user_id=user_id)

def update_product(request, product_id: int, payload: schemas.ProductUpdate) -> Product:
    user_id = request.auth["user_id"]
    product = get_object_or_404(Product, pk=product_id, user_id=user_id)

    data = payload.model_dump(exclude_none=True)
    for attr, value in data.items():
        setattr(product, attr, value)
        
    product.save(update_fields=data.keys())

    if product.stock < 5:

        event = LowStockEvent(
            id=product.id,
            name_product=product.name,
            total_items=product.stock,
            email=request.auth["email"]
        )

        asyncio.run(publish_low_stock(event))

    return product

def delete_product(request, product_id: int):
    user_id = request.auth["user_id"]
    product = get_object_or_404(Product, pk=product_id, user_id=user_id)
    product.delete()
    return {'Message': 'Product deleted'}