
from dataclasses import dataclass
import math

@dataclass
class RiskParams:
    max_leverage: float = 3.0
    max_portfolio_exposure: float = 0.8 # 80% of equity
    min_confidence_threshold: float = 0.6

class AdvancedRiskManager:
    """
    Institutional Risk Management using the Kelly Criterion.
    Optimizes position size to maximize long-term growth while avoiding ruin.
    """
    def __init__(self, params: RiskParams):
        self.params = params

    def calculate_kelly_size(self, win_prob: float, win_loss_ratio: float) -> float:
        """
 same as Kelly Formula: f* = (bp - q) / b
        where b = win_loss_ratio, p = win_prob, q = 1 - p
        """
        if win_prob <= 0 or win_prob >= 1:
            return 0.0
        
        q = 1.0 - win_prob
        fraction = (win_loss_ratio * win_prob - q) / win_loss_ratio
        
        # Fractional Kelly (typically 0.25 or 0.5) to reduce volatility
        return max(0.0, fraction * 0.5)

    def validate_exposure(self, current_exposure: float, total_equity: float) -> bool:
        return current_exposure <= (total_equity * self.params.max_portfolio_exposure)
