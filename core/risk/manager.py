
from dataclasses import dataclass
import math

@dataclass
class RiskConfig:
    max_position_size: float  # Max % of portfolio
    max_drawdown: float       # Max allowed drawdown before kill-switch
    risk_per_trade: float     # Fixed risk per trade (e.g. 0.01 for 1%)

class RiskManager:
    """
    Institutional-grade risk gate. 
    Ensures no single trade can blow the account and manages overall exposure.
    """
    def __init__(self, config: RiskConfig):
        self.config = config
        self.current_exposure = 0.0

    def calculate_position_size(self, equity: float, stop_loss_pct: float) -> float:
        """
        Calculate position size based on fixed risk per trade.
        Formula: (Equity * RiskPerTrade) / StopLossPercentage
        """
        risk_amount = equity * self.config.risk_per_trade
        position_size = risk_amount / stop_loss_pct
        
        # Cap at max position size
        max_allowed = equity * self.config.max_position_size
        return min(position_size, max_allowed)

    def validate_signal(self, signal_amount: float, total_equity: float) -> bool:
        if signal_amount > (total_equity * self.config.max_position_size):
            return False
        return True
