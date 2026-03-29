from django.shortcuts import get_object_or_404
from .models import Product
from . import schemas

def list_product():
    return Product.objects.all()

def create_product(payload: schemas.ProductCreate) -> Product:
    return Product.objects.create(**payload.dict())

def get_product(product_id: int) -> Product:
    return get_object_or_404(Product, pk=product_id)

def update_product(product_id: int, payload: schemas.ProductUpdate) -> Product:
    product = get_object_or_404(Product, pk=product_id)

    data = payload.model_dump(exclude_none=True)
    for attr, value in data.items():
        setattr(product, attr, value)
        
    product.save(update_fields=data.keys())

    return product

def delete_product(product_id: int):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return {'Message': 'Product deleted'}