# ⚡ Siphon-Quant-Core

A modular, high-frequency financial intelligence and signal execution engine. The blueprint for a next-generation autonomous terminal.

## 🎯 Objective
To replace traditional terminal lag with a predictive, autonomous pipeline that transforms raw market data into high-confidence execution signals.

## 🏗️ Institutional-Grade Architecture
Siphon-Quant-Core is built to Wall Street standards, focusing on low-latency, quantitative rigor, and strict risk management.

### 1. The Async Core (`/core/engine`)
Utilizes an **Event-Driven Architecture** via an asynchronous `EventBus`. Decouples data providers from signal consumers for microsecond propagation.

### 2. Quantitative Indicators (`/core/indicators`)
Professional-grade alpha generators:
- **Z-Score Analysis**: Mean-reversion detection.
- **Order Flow Imbalance (OFI)**: Real-time buy/sell pressure analysis.

### 3. Risk Management (`/core/risk`)
A strict risk gate based on the **Fixed-Fractional Risk Model**, calculating position sizes dynamically to prevent account ruin.

### 4. Backtesting Engine (`/core/backtest`)
Institutional-grade simulation layer. Calculates **Sharpe Ratio**, **Max Drawdown**, and **Win Rate** to verify strategy alpha before deployment.

### 5. Execution Layer (`/core/adapters`)
API-agnostic adapters for seamless connectivity:
- **CEX**: Direct integration with Binance, etc.
- **DEX**: On-chain routing via Uniswap V3.

### 6. Observability (`/core/telemetry`)
Real-time telemetry monitoring system for system latency and signal accuracy.

## 🚀 System Flow
`Data Feeders` $
ightarrow$ `EventBus` $
ightarrow$ `QuantIndicators` $
ightarrow$ `RiskManager` $
ightarrow$ `ExecutionAdapter`

## 📜 License
Proprietary / Siphon-Research
