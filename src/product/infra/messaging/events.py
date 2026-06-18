from pydantic import BaseModel


class StockLowEvent(BaseModel):
    id: int
    user_id: str
    name_product: str
    total_items: int
    email: str