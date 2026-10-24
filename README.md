# ⚡ Siphon-Quant-Core

A modular, high-frequency financial intelligence and signal execution engine. The blueprint for a next-generation autonomous terminal.

## 🎯 Objective
To replace traditional terminal lag with a predictive, autonomous pipeline that transforms raw market data into high-confidence execution signals.

## 🏗️ Institutional-Grade Architecture
Siphon-Quant-Core is built to Wall Street standards, focusing on low-latency, quantitative rigor, and strict risk management.

### 1. The Async Core (`/core/engine`)
Utilizes an **Event-Driven Architecture** via an asynchronous `EventBus`. This decouples data providers from signal consumers, enabling microsecond-level propagation of market events.

### 2. Quantitative Indicators (`/core/indicators`)
Implements high-alpha indicators used in professional trading:
- **Z-Score Analysis**: Mean-reversion detection.
- **Order Flow Imbalance (OFI)**: Real-time buy/sell pressure analysis.

### 3. Risk Management (`/core/risk`)
A strict risk gate based on the **Fixed-Fractional Risk Model**. It calculates position sizes dynamically based on account equity and volatility to ensure solvency.

### 4. Quantitative Specification
For a detailed mathematical breakdown of the system, see the [`QUANTSPEC.md`](docs/QUANTSPEC.md).

## 🚀 System Flow
`Data Feeders` $ightarrow$ `EventBus` $ightarrow$ `QuantIndicators` $ightarrow$ `RiskManager` $ightarrow$ `ExecutionAdapter`

## 📜 License
Proprietary / Siphon-Research
