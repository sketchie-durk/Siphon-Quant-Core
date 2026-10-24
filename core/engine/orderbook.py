
from dataclasses import dataclass, field
from typing import Dict, List, Tuple
import collections

@dataclass
class OrderBookLevel:
    price: float
    size: float

class LimitOrderBook:
    """
    Local L2 Order Book manager.
    Maintains synchronized bids and asks to calculate market impact and slippage.
    """
    def __init__(self, asset: str):
        self.asset = asset
        self.bids: Dict[float, float] = collections.defaultdict(float)
        self.asks: Dict[float, float] = collections.defaultdict(float)

    def update_level(self, side: str, price: float, size: float):
        target = self.bids if side == 'BID' else self.asks
        if size == 0:
            target.pop(price, None)
        else:
            target[price] = size

    def get_best_bid(self) -> float:
        return max(self.bids.keys()) if self.bids else 0.0

    def get_best_ask(self) -> float:
        return min(self.asks.keys()) if self.asks else float('inf')

    def calculate_slippage(self, size: float, side: str) -> float:
        book = self.asks if side == 'BUY' else self.bids
        sorted_levels = sorted(book.items(), key=lambda x: x[0] if side == 'BUY' else -x[0])
        accumulated_size = 0.0
        weighted_price = 0.0
        for price, size_at_level in sorted_levels:
            fill = min(size_at_level, size - accumulated_size)
            weighted_price += price * fill
            accumulated_size += fill
            if accumulated_size >= size:
                break
        if accumulated_size < size:
            return float('inf')
        return weighted_price / size
