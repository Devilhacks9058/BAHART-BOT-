import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_ADMIN_ID = os.getenv('TELEGRAM_ADMIN_ID')

# Pocket Option Configuration
POCKET_OPTION_SESSION_TOKEN = os.getenv('POCKET_OPTION_SESSION_TOKEN', '27abb5e58c1d57e2aa2a4567042f64e3')
POCKET_OPTION_UID = os.getenv('POCKET_OPTION_UID', '81704775')
POCKET_OPTION_WS_URL = 'wss://api.poc-app.com/socket.io'

# Trading Configuration
MIN_ACCURACY_THRESHOLD = 0.90  # 90% minimum accuracy
TIMEFRAME = '1m'  # 1-minute candles
EXPIRY_TIME = 60  # 1 minute expiry

# Technical Indicators - 1-Minute Optimized Settings
INDICATOR_SETTINGS = {
    'ema': {'fast': 10, 'slow': 50},
    'parabolic_sar': {'acceleration': 0.05, 'max': 0.2},
    'ichimoku': {'tenkan': 7, 'kijun': 22, 'senkou_b': 44},
    'adx': {'period': 14},
    'bollinger_bands': {'period': 20, 'deviation': 2},
    'donchian': {'period': 20},
    'keltner': {'period': 20, 'multiplier': 1.5},
    'rsi': {'period': 7, 'oversold': 20, 'overbought': 80},
    'stochastic': {'k_period': 5, 'd_period': 3, 'smooth': 3},
    'macd': {'fast': 12, 'slow': 26, 'signal': 9},
    'cci': {'period': 14, 'upper': 100, 'lower': -100},
    'williams_r': {'period': 14, 'upper': -20, 'lower': -80},
    'awesome_oscillator': {'fast': 5, 'slow': 34},
    'momentum': {'period': 10, 'centerline': 100},
    'roc': {'period': 9},
    'osma': {'fast': 12, 'slow': 26, 'signal': 9},
    'vortex': {'period': 14},
    'atr': {'period': 14},
    'zigzag': {'deviation': 1, 'depth': 5},
    'fractals': {'period': 2}
}

# Signal Generation Settings
SIGNAL_SETTINGS = {
    'require_multi_confirmation': True,
    'min_indicators_agree': 12,  # At least 12 indicators must agree
    'pattern_weight': 0.3,
    'indicator_weight': 0.7,
    'use_consensus_voting': True
}

# Trading Risk Management
RISK_MANAGEMENT = {
    'max_daily_loss': 0.10,  # 10% max daily loss
    'max_position_size': 0.05,  # 5% per trade
    'stop_loss_pips': 50,
    'take_profit_ratio': 2.0  # 1:2 risk-reward
}

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = 'logs/bahart_bot.log'

# Assets to Monitor
ASSETS = [
    'EURUSD',
    'GBPUSD',
    'USDJPY',
    'USDCHF',
    'AUDUSD',
    'NZDUSD',
    'USDCAD',
    'XAUUSD',
    'XAGUSD',
    'US500',
    'US100',
    'OIL',
    'BTCUSD',
    'ETHUSD'
]

# API Rate Limits
RATE_LIMITS = {
    'candles_per_minute': 100,
    'signals_per_minute': 10,
    'trades_per_minute': 5
}

# Database Configuration (Optional)
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/bahart_bot')