
from abc import ABC, abstractmethod
from core.engine.logic import Signal, SignalType

class BaseStrategy(ABC):
    """
    Abstract Base Class for all trading strategies.
    Ensures a consistent interface for the Logic Engine to execute.
    """
    def __init__(self, name: str, params: dict):
        self.name = name
        self.params = params

    @abstractmethod
    def on_data(self, data: dict) -> Signal:
        """
        Analyzes market data and returns a Signal.
        """
        pass

    def update_params(self, new_params: dict):
        self.params.update(new_params)
