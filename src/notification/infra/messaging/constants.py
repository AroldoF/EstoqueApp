from enum import StrEnum


class Exchange(StrEnum):
    ACCOUNTS = "accounts.events"
    ORDERS = "orders.events"
    CATALOGS = "catalogs.events"


class RoutingKey(StrEnum):
    USER_CREATED = "accounts.user.created"
    ORDER_PAID = "orders.order.paid"
    STORE_CREATED = "catalog.store.created"


class Queue(StrEnum):
    USER_CREATED = "accounts.user.created.queue"
    WALLET_TRANSACTION = "accounts.wallet.transaction.queue"
    BECOME_ARTISAN = "accounts.become.artisan.queue"
    CREATE_WALLET = "accounts.create.wallet.queue"