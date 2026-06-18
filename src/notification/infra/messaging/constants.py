from enum import StrEnum


class Exchange(StrEnum):
    STOCK = "estoque.events"

class RoutingKey(StrEnum):
    STOCK_KEY = "estoque.stock"
    NOTIFICATION = "#.notification"

class Queue(StrEnum):
    STOCK_LOW = "estoque.stock.low"
    SAVE_NOTIFICATION = "notification.save_notification.queue"