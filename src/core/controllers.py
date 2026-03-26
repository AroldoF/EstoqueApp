from ninja import NinjaAPI
from . import schemas
api = NinjaAPI()


@api.patch('', response= schemas.ProductRead)
def product_update(payload:schemas.ProductUpdate):
    return {'a': 'a'}