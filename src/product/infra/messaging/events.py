from pydantic import BaseModel


class LowStockEvent(BaseModel):
    id: int
    name_product: str
    total_items: int
    email: str