
from typing import Dict
from core.strategies.base import BaseStrategy

class StrategyManager:
    """
    Handles the lifecycle of active strategies.
    Allows for hot-swapping strategies without restarting the engine.
    """
    def __init__(self):
        self.active_strategies: Dict[str, BaseStrategy] = {}

    def add_strategy(self, name: str, strategy: BaseStrategy):
        self.active_strategies[name] = strategy
        print(f"[STRATEGY] {name} loaded and active.")

    def remove_strategy(self, name: str):
        if name in self.active_strategies:
            del self.active_strategies[name]
            print(f"[STRATEGY] {name} removed.")

    def get_all_signals(self, data: dict) -> list:
        signals = []
        for name, strategy in self.active_strategies.items():
            signals.append(strategy.on_data(data))
        return signals
