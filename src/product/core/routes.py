from ninja import NinjaAPI
from . import schemas
from . import services
from .auth import grpc_auth
api = NinjaAPI(auth=grpc_auth)

@api.post('/product', response=schemas.ProductCreate)
def product_create(request, payload:schemas.ProductCreate): 
    return services.create_product(request, payload)

@api.get('/product', response=list[schemas.ProductRead])
def list_products(request):
    return services.list_product(request)

@api.get('/product/{product_id}/', response=schemas.ProductRead)
def get_product(request, product_id: int):
    return services.get_product(request,product_id)

@api.patch('/product/{product_id}/', response= schemas.ProductRead)
def update_product(request, product_id: int, payload:schemas.ProductUpdate):
    return services.update_product(request, product_id, payload)

@api.delete('/product/{product_id}/')
def delete_product(request, product_id: int):
    return services.delete_product(request, product_id)