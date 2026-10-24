from core.engine.logic import SiphonLogicEngine, SignalType
from core.indicators.library import QuantIndicators

class MeanReversionStrategy:
    def __init__(self, engine: SiphonLogicEngine):
        self.engine = engine
        
    def on_data(self, data):
        # Using Z-Score for Mean Reversion
        # In a real scenario, 'data' would be a time series
        z_score = QuantIndicators.z_score([10, 11, 12, 10, 9], 5) 
        if z_score < -2.0:
            return "LONG"
        elif z_score > 2.0:
            return "SHORT"
        return "NEUTRAL"
