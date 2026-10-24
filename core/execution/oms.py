
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import time

class OrderStatus(Enum):
    PENDING = "PENDING"
    FILLED = "FILLED"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"

@dataclass
class Order:
    order_id: str
    asset: str
    amount: float
    price: float
    side: str
    status: OrderStatus = OrderStatus.PENDING
    filled_amount: float = 0.0
    timestamp: float = field(default_factory=time.time)

class OrderManagementSystem:
    """
    OMS (Order Management System).
    Tracks the state of all live orders and handles the order lifecycle.
    """
    def __init__(self):
        self.orders: Dict[str, Order] = {}

    def create_order(self, order_id: str, asset: str, amount: float, price: float, side: str) -> Order:
        order = Order(order_id, asset, amount, price, side)
        self.orders[order_id] = order
        return order

    def update_order_status(self, order_id: str, status: OrderStatus, filled: float = 0.0):
        if order_id in self.orders:
            order = self.orders[order_id]
            order.status = status
            order.filled_amount += filled
            if order.filled_amount >= order.amount:
                order.status = OrderStatus.FILLED

    def get_open_orders(self) -> List[Order]:
        return [o for o in self.orders.values() if o.status in [OrderStatus.PENDING, OrderStatus.PARTIALLY_FILLED]]
