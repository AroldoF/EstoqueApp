from ninja import NinjaAPI
from . import schemas
from .models import Product
from . import services
api = NinjaAPI()


@api.post('/product', response=schemas.ProductCreate)
def product_create(request, payload:schemas.ProductCreate):
    product = Product.objects.create(**payload.dict())
    return product

@api.get('/product', response=list[schemas.ProductRead])
def list_products(request):
    return Product.objects.all()

@api.get('/product/{product_id}/', response=schemas.ProductRead)
def get_product(request, product_id: int):
    return services.get_product(product_id)

@api.patch('/product/{product_id}/', response= schemas.ProductRead)
def update_product(request, product_id: int, payload:schemas.ProductUpdate):
    return services.update_product(product_id, payload)
