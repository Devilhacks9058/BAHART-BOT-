# BAHART Trading Bot Documentation

## Overview
BAHART is an advanced algorithmic trading bot for Pocket Option with real-time analysis and signal generation.

## Features
1. **16+ Technical Indicators** - All optimized for 1-minute timeframe
2. **20+ Candlestick Patterns** - Automatic pattern recognition
3. **Price Action Analysis** - Market structure, BOS, CHoCH, liquidity sweeps
4. **90% Accuracy Threshold** - Multi-indicator consensus voting
5. **WebSocket Integration** - Live Pocket Option connection
6. **Telegram Notifications** - Real-time signal delivery

## Installation

```bash
git clone https://github.com/Devilhacks9058/BAHART-BOT-.git
cd BAHART-BOT-
pip install -r requirements.txt
cp .env.example .env
```

## Configuration

Edit `.env` with your credentials:
```
TELEGRAM_BOT_TOKEN=your_bot_token
POCKET_OPTION_SESSION_TOKEN=27abb5e58c1d57e2aa2a4567042f64e3
POCKET_OPTION_UID=81704775
```

## Running

```bash
python main.py
```

## Architecture

- `core/` - WebSocket, data fetching, signal generation
- `analysis/` - Technical indicators, patterns, price action
- `telegram_bot/` - Telegram integration
- `trading/` - Order execution and position management
- `utils/` - Configuration, logging, helpers

## Supported Assets
EURUSD, GBPUSD, USDJPY, AUDUSD, XAUUSD, US500, US100, BTCUSD, ETHUSD, and more

## Risk Management
- 90% minimum accuracy threshold
- Consensus voting system
- Position size limits
- Stop loss protection
- Risk-reward ratio: 1:2

## License
MIT License

## Disclaimer
⚠️ For educational purposes only. Always trade responsibly.