# BAHART TRADING BOT 🤖📈

**Advanced Telegram Bot for Pocket Option with Live Market Analysis & AI Trading Signals**

## Features

### 1. **Real-Time Market Analysis**
- Live trend analysis
- Support & Resistance levels (dynamic)
- Price Action Analysis (Market Structure, BOS, CHoCH, Liquidity Sweeps, Order Blocks, FVGs)
- Candlestick Pattern Recognition (20+ patterns)
- Chart Pattern Recognition (Head & Shoulders, Triangles, Wedges, Flags, etc.)

### 2. **Advanced Technical Indicators (1-Min Optimized)**
- Moving Averages (EMA 10/50, SMA, WMA)
- Parabolic SAR (0.05/0.2)
- Ichimoku Kinko Hyo (7/22/44)
- ADX (14) - Trend Strength
- Bollinger Bands (20/2)
- Donchian Channels (20)
- Keltner Channels (20/1.5)
- RSI (7) - Ultra-responsive
- Stochastic Oscillator (5/3/3)
- MACD (12/26/9)
- CCI (14)
- Williams %R (14)
- Awesome Oscillator (5/34)
- Accelerator Oscillator
- Momentum (10)
- ROC (9)
- OsMA (12/26/9)
- Vortex Indicator (14)
- ATR (14)
- ZigZag (1%/5)
- Fractals (2)

### 3. **Advanced Analysis**
- Fibonacci Retracement & Extension
- Pivot Point Analysis
- Breakout Detection
- Pullback/Retracement Analysis
- Market Sentiment Analysis
- Economic News Impact Analysis
- VWAP Analysis

### 4. **Signal Generation**
- 90%+ Accuracy Threshold
- Multi-timeframe confirmation (1-min primary)
- Majority consensus voting system
- Real-time signal delivery
- Asset-specific signals (OTC & Real Markets)
- Entry & Exit recommendations
- Risk/Reward calculations

### 5. **Live Trading Integration**
- Pocket Option WebSocket connection
- Automated trade execution
- Order monitoring
- Live P&L tracking
- Position management

## Architecture

```
BARHART-BOT/
├── core/
│   ├── websocket_manager.py      # Pocket Option WebSocket
│   ├── data_fetcher.py           # Market data collection
│   └── signal_generator.py       # Signal creation logic
├── analysis/
│   ├── trend_analysis.py         # Trend identification
│   ├── price_action.py           # Price Action analysis
│   ├── candlestick_patterns.py   # Candlestick recognition
│   ├── chart_patterns.py         # Chart pattern detection
│   └── technical_indicators.py   # All 20+ indicators
├── telegram_bot/
│   ├── bot.py                    # Telegram bot main
│   ├── handlers.py               # Message handlers
│   └── keyboard.py               # Custom keyboards
├── trading/
│   ├── pocket_option_trader.py   # Trade execution
│   ├── position_manager.py       # Position tracking
│   └── risk_manager.py           # Risk management
├── utils/
│   ├── config.py                 # Configuration
│   ├── logger.py                 # Logging
│   └── helpers.py                # Helper functions
└── requirements.txt
```

## Quick Start

### Prerequisites
- Python 3.9+
- Telegram Bot Token
- Pocket Option Account
- WebSocket Auth Token

### Installation

```bash
git clone https://github.com/Devilhacks9058/BAHART-BOT-.git
cd BAHART-BOT-
pip install -r requirements.txt
```

### Configuration

1. Create `.env` file:
```
TELEGRAM_BOT_TOKEN=your_bot_token
POCKET_OPTION_SESSION_TOKEN=27abb5e58c1d57e2aa2a4567042f64e3
POCKET_OPTION_UID=81704775
```

2. Run the bot:
```bash
python main.py
```

## WebSocket Connection Details

The bot uses Pocket Option WebSocket authentication:
```
42["auth",{"sessionToken":"27abb5e58c1d57e2aa2a4567042f64e3","uid":"81704775","lang":"en","currentUrl":"cabinet","isChart":1}]
```

## Signal Accuracy & Trading

- **Minimum Accuracy**: 90% before signal generation
- **Timeframe**: 1-minute (1M) primary analysis
- **Signal Types**: BUY/SELL with confidence levels
- **Assets Covered**: All Pocket Option available pairs
- **Delivery**: Real-time Telegram notifications

## Bot Commands

```
/start          - Start the bot
/status         - Current market status
/signals        - Latest signals
/analysis       - Current analysis (all 16 indicators + patterns)
/portfolio      - Your open positions
/balance        - Account balance
/help           - Help information
/settings       - Bot configuration
```

## Technical Specifications

### Data Update Frequency
- **Candle Data**: Real-time (1-min)
- **Indicator Updates**: Every tick
- **Pattern Scanning**: Every candle close
- **Signal Broadcast**: < 1 second from generation

### Accuracy Metrics
- Multi-indicator confirmation required
- Consensus voting system
- Historical backtesting validation
- Live performance tracking

## License

MIT License - See LICENSE file

## Author

Devilhacks9058

## Support

For issues and feature requests, please create an issue in the repository.

---

**⚠️ Risk Disclaimer**: This bot is for educational purposes. Always trade responsibly and never risk more than you can afford to lose.