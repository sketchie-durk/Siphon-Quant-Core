# 🏗️ Siphon-Quant-Core Architecture

Siphon-Quant-Core is designed as a modular, low-latency financial intelligence system. It decouples data acquisition from signal generation and execution to allow for hot-swapping of quantitative models.

## 🛠️ System Flow
`Data Feeders` $ightarrow$ `Logic Engine` $ightarrow$ `Signal Processor` $ightarrow$ `Risk Manager` $ightarrow$ `Execution Adapter`

### 1. Data Feeders (`/data/feeders`)
Standardized ingestors for:
- **L1/L2 Orderbook Data**: Real-time WebSocket feeds.
- **On-Chain Metrics**: Liquidity flow, whale movements, contract events.
- **Sentiment**: LLM-processed news and social sentiment.

### 2. Logic Engine (`/core/engine`)
The "Brain" of the terminal. It aggregates raw data and applies quantitative filters.
- **Time-Series Analysis**: Moving averages, RSI, Bollinger Bands.
- **Correlation Matrix**: Monitoring asset pairs for divergence/convergence.

### 3. Signal Processor (`/core/signals`)
Converts engine output into discrete action signals.
- **Logic**: `If (Correlation > X && Sentiment == Positive) -> Signal: LONG`
- **Confidence Score**: Each signal is assigned a 0-1 confidence value.

### 4. Risk Manager (`/core/risk`)
The final safety gate.
- **Position Sizing**: Based on Kelly Criterion or fixed % of equity.
- **Dynamic Hedging**: Automatic opposite-positioning to neutralize delta.

### 5. Execution Adapters (`/core/adapters`)
Translates signals into API calls for:
- **CEX**: Binance, Coinbase, OKX.
- **DEX**: Uniswap, Curve, PancakeSwap.
