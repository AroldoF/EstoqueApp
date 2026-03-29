from ninja import NinjaAPI
from . import schemas
from . import services
api = NinjaAPI()


@api.post('/product', response=schemas.ProductCreate)
def product_create(request, payload:schemas.ProductCreate): 
    return services.create_product(payload)

@api.get('/product', response=list[schemas.ProductRead])
def list_products(request):
    return services.list_product()

@api.get('/product/{product_id}/', response=schemas.ProductRead)
def get_product(request, product_id: int):
    return services.get_product(product_id)

@api.patch('/product/{product_id}/', response= schemas.ProductRead)
def update_product(request, product_id: int, payload:schemas.ProductUpdate):
    return services.update_product(product_id, payload)

@api.delete('/product/{product_id}/')
def delete_product(request, product_id: int):
    return services.delete_product(product_id)