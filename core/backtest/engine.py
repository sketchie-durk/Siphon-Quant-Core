from dataclasses import dataclass
from typing import List, Dict, Any
import pandas as pd
import numpy as np

@dataclass
class Trade:
    entry_price: float
    exit_price: float
    size: float
    direction: str 
    pnl: float = 0.0

class BacktestEngine:
    def __init__(self, initial_equity: float = 100000.0):
        self.equity = initial_equity
        self.trades: List[Trade] = []
        self.equity_curve = [initial_equity]

    def execute_trade(self, entry: float, exit: float, size: float, direction: str):
        pnl = (exit - entry) * size if direction == 'LONG' else (entry - exit) * size
        trade = Trade(entry, exit, size, direction, pnl)
        self.trades.append(trade)
        self.equity += pnl
        self.equity_curve.append(self.equity)

    def calculate_metrics(self):
        returns = pd.Series(self.equity_curve).pct_change().dropna()
        sharpe = (returns.mean() / returns.std()) * np.sqrt(252) if len(returns) > 1 else 0
        max_drawdown = (pd.Series(self.equity_curve).cummax() - pd.Series(self.equity_curve)).max()
        return {
            "Final Equity": self.equity,
            "Total Trades": len(self.trades),
            "Sharpe Ratio": sharpe,
            "Max Drawdown": max_drawdown,
            "Win Rate": len([t for t in self.trades if t.pnl > 0]) / len(self.trades) if self.trades else 0
        }
