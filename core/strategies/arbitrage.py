
from core.strategies.base import BaseStrategy
from core.engine.logic import Signal, SignalType

class CrossVenueArbitrageStrategy(BaseStrategy):
    """
    Institutional Arbitrage Strategy.
    Monitors price divergence between two different venues (e.g., Binance and Uniswap).
    """
    def __init__(self, name: str, params: dict):
        super().__init__(name, params)
        self.venue_a = params.get('venue_a', 'BINANCE')
        self.venue_b = params.get('venue_b', 'UNISWAP')
        self.min_spread = params.get('min_spread', 0.005) # 0.5% minimum profit

    def on_data(self, data: dict) -> Signal:
        # Expecting data to contain price from multiple venues
        price_a = data.get(f'{self.venue_a}_price')
        price_b = data.get(f'{self.venue_b}_price')
        
        if not price_a or not price_b:
            return Signal("CROSS_ARB", SignalType.NEUTRAL, 0.0, "Insufficient venue data")

        spread = abs(price_a - price_b) / min(price_a, price_b)
        
        if spread > self.min_spread:
            direction = SignalType.LONG if price_a < price_b else SignalType.SHORT
            reason = f"Spread detected: {spread:.4f} between {self.venue_a} and {self.venue_b}"
            return Signal("CROSS_ARB", direction, 0.9, reason)
            
        return Signal("CROSS_ARB", SignalType.NEUTRAL, 0.0, "Spread below threshold")
