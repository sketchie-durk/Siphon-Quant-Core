
import numpy as np

class QuantIndicators:
    """
    Professional-grade indicators used in HFT and Market Making.
    """
    @staticmethod
    def z_score(data: list, window: int = 20):
        """
        Measures how many standard deviations a price is from its mean.
        Standard for Mean-Reversion strategies.
        """
        if len(data) < window: return 0.0
        subset = data[-window:]
        mean = np.mean(subset)
        std = np.std(subset)
        return (data[-1] - mean) / std if std > 0 else 0.0

    @staticmethod
    def order_flow_imbalance(bids: list, asks: list):
        """
        Calculates the imbalance between buy and sell pressure at the top of the book.
        Crucial for short-term price action prediction.
        """
        bid_vol = sum([b[1] for b in bids]) # volume of top bids
        ask_vol = sum([a[1] for a in asks]) # volume of top asks
        return (bid_vol - ask_vol) / (bid_vol + ask_vol)
