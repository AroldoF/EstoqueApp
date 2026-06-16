from dataclasses import dataclass

@dataclass
class StockLowEvent:
    id: int
    name_product: str
    total_items: int
    email: str
    template_prefix: str
