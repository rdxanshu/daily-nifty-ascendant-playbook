# daily-nifty-ascendant-playbook
Automated Python script for daily NIFTY trading playbook with capital, risk control &amp; positive signals.
A sophisticated, automated trading system designed to scalp NIFTY options with a goal of doubling capital daily. It leverages real-time market data, aggregated news sentiment from multiple sources, Monte Carlo simulations, and broker APIs (Zerodha, Upstox, Angel One) to execute high-probability trades with strict risk controls.
Table of Contents
•  Overview
•  Features
•  Core Trading Principles
•  How It Works
•  Setup Instructions
•  Dependencies
•  Broker Integration
•  Usage
•  Testing
•  Security and Best Practices
•  Disclaimers
•  Future Ideas
•  Support
•  License
Overview
NYROS QUANT TITAN AI is an advanced trading bot that scalps NIFTY options, aiming to double capital daily through high-probability trades (≥70% success probability). It collects and analyzes news from Alpha Vantage, Finnhub, and NewsAPI to form a robust sentiment score, enabling the AI to “think” and make informed trade decisions. Trades are logged with detailed calculations (entry price, stop-loss, target, probability) and timestamps for transparency. The system prioritizes Zerodha for its low costs (₹20/order) and reliable APIs, with fallbacks to Upstox or Angel One.
Market Snapshot (October 17, 2025, 01:52 AM IST):
•  NIFTY 50: ~25,145.50 (based on prior data; fetch real-time via script)
•  Bank NIFTY: ~56,359.90
•  India VIX: ~11.01 (low volatility)
•  Conditions: Stable post-US Fed rate cuts, mildly bearish bias, low inflation, RBI steady.
Features
•  Multi-Source News Aggregation: Combines sentiment from Alpha Vantage, Finnhub, and NewsAPI for comprehensive market analysis.
•  AI-Driven Decision-Making: Aggregates sentiment to “think” and select optimal trades, reducing reliance on single data points.
•  Detailed Trade Plans: Logs trades line-by-line with timestamps, entry price, stop-loss, target, probability, and sentiment bias.
•  Profit Optimization: Targets ≥70% success probability with 0.3% stop-loss and 1% profit per trade, aiming for “no-loss” scenarios (risks apply).
•  Automatic Broker Selection: Prioritizes Zerodha, falls back to Upstox or Angel One.
•  Real-Time Data: Fetches NIFTY 50, VIX, and option chain data every minute via nsepython.
•  Trade Notifications: Supports Telegram/console approval with 30-second auto-approve timeout.
•  Email Reports: Sends daily summaries of trades, profits, and capital.
•  Robust Error Handling: Extensive logging and retry logic for reliability.
•  Future-Ready: Modular design for ML, backtesting, and cloud integration.
Core Trading Principles
•  Capital Adaptability: Adjusts trade sizes dynamically for recovery and growth.
•  Trade Limits: Up to 3 trades/day or stops at doubling target.
•  Strict Risk Control: 0.3% stop-loss per trade, immediate closure on breach.
•  High-Probability Trades: Uses Monte Carlo simulations and sentiment to ensure ≥70% success likelihood.
•  Loss Recovery: Increases trade size (optional martingale) post-loss for recovery.
•  Profit Focus: Targets 1% per trade, aiming for daily doubling (risks apply).
•  Flexibility: Supports NIFTY options; expandable to stocks/futures.
