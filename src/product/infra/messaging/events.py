from pydantic import BaseModel


class StockLowEvent(BaseModel):
    id: int
    name_product: str
    total_items: int
    email: str