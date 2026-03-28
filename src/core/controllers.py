from ninja import NinjaAPI
from . import schemas
from .models import Product
api = NinjaAPI()


@api.post('/product', response=schemas.ProductCreate)
def product_create(request, payload:schemas.ProductCreate):
    product = Product.objects.create(**payload.dict())
    return product


@api.patch('', response= schemas.ProductRead)
def product_update(payload:schemas.ProductUpdate):
    return {'a': 'a'}


@api.get('/product', response=list[schemas.ProductRead])
def list_products(request):
    return Product.objects.all()