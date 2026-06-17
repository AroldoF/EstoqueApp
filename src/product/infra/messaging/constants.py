from enum import StrEnum


class Exchange(StrEnum):
    STOCK = "estoque.events"

class RoutingKey(StrEnum):
    STOCK_KEY = "estoque.stock"

class Queue(StrEnum):
    STOCK_LOW = "estoque.stock.low"