
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Position:
    asset: str
    size: float
    entry_price: float
    unrealized_pnl: float = 0.0

class PortfolioTracker:
    def __init__(self, initial_cash: float):
        self.cash = initial_cash
        self.positions: Dict[str, Position] = {}
        self.total_equity = initial_cash

    def update_position(self, asset: str, size_change: float, price: float):
        if asset not in self.positions:
            self.positions[asset] = Position(asset, 0.0, price)
        pos = self.positions[asset]
        if pos.size > 0 and size_change > 0:
            pos.entry_price = ((pos.size * pos.entry_price) + (size_change * price)) / (pos.size + size_change)
        pos.size += size_change
        self.cash -= (size_change * price)

    def get_total_value(self, current_prices: Dict[str, float]) -> float:
        asset_value = 0.0
        for asset, pos in self.positions.items():
            asset_value += pos.size * current_prices.get(asset, pos.entry_price)
        self.total_equity = self.cash + asset_value
        return self.total_equity
