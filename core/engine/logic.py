
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

class SignalType(Enum):
    LONG = "LONG"
    SHORT = "SHORT"
    NEUTRAL = "NEUTRAL"

@dataclass
class Signal:
    asset: str
    type: SignalType
    confidence: float
    reasoning: str

class SiphonLogicEngine:
    """
    Core logic system that processes data and generates signals.
    """
    def __init__(self):
        self.active_filters = []

    def add_filter(self, filter_func):
        self.active_filters.append(filter_func)

    def evaluate(self, asset: str, data: Dict) -> Signal:
        scores = [f(data) for f in self.active_filters]
        avg_score = sum(scores) / len(scores) if scores else 0
        
        if avg_score > 0.7:
            return Signal(asset, SignalType.LONG, avg_score, "Combined filter convergence positive")
        elif avg_score < -0.7:
            return Signal(asset, SignalType.SHORT, abs(avg_score), "Combined filter convergence negative")
        
        return Signal(asset, SignalType.NEUTRAL, 0.0, "Insufficient signal strength")

# Example Usage
if __name__ == "__main__":
    # Mock filters
    def rsi_filter(data): return 0.8 if data['rsi'] < 30 else -0.8 if data['rsi'] > 70 else 0
    def sentiment_filter(data): return 0.9 if data['sentiment'] > 0.5 else -0.9
    
    engine = SiphonLogicEngine()
    engine.add_filter(rsi_filter)
    engine.add_filter(sentiment_filter)
    
    mock_data = {'rsi': 25, 'sentiment': 0.8}
    signal = engine.evaluate("BTC", mock_data)
    print(f"Signal for BTC: {signal.type} (Confidence: {signal.confidence})")
