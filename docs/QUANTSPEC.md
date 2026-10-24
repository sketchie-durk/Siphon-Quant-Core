# 📉 Quantitative Specification (QuantSpec)

This document defines the mathematical and engineering rigor of the Siphon-Quant-Core system to ensure it meets institutional standards.

## 1. Mathematical Foundations
### 1.1 Signal Convergence
A signal $S$ is generated when the weighted sum of $n$ indicators exceeds a threshold $	heta$:
$$\sum_{i=1}^{n} w_i \cdot I_i > 	heta$$
Where $w_i$ is the weight of indicator $I_i$ and $	heta$ is the confidence threshold.

### 1.2 Risk Calibration
Position sizing is derived from the **Fixed-Fractional Risk Model**:
$$	ext{Position Size} = rac{	ext{Equity} 	imes 	ext{Risk Per Trade}}{	ext{Stop Loss Percentage}}$$

## 2. Engineering Constraints
- **Latency**: Goal of $<10ms$ from Data Ingestion to Signal Generation.
- **Reliability**: $99.99\%$ uptime requirement for the Event Bus.
- **Slippage**: Every signal must include a `max_slippage` parameter based on the current Order Book depth.

## 3. Validation Metrics
The system is examined based on the following KPIs:
- **Sharpe Ratio**: Risk-adjusted return.
- **Sortino Ratio**: Focus on downside volatility.
- **Max Drawdown (MDD)**: The peak-to-trough decline.
- **Profit Factor**: Sum of gross profits / sum of gross losses.
