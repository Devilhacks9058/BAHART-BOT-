import numpy as np
from typing import List, Dict, Tuple
from datetime import datetime, timedelta
import pandas as pd

def calculate_accuracy(signals: List[Dict], results: List[bool]) -> float:
    """
    Calculate signal accuracy from historical data
    """
    if not signals or not results:
        return 0.0
    
    correct = sum(results)
    total = len(signals)
    return correct / total if total > 0 else 0.0

def consensus_voting(indicator_signals: Dict[str, str]) -> Tuple[str, float]:
    """
    Determine consensus signal from multiple indicators
    Returns: (signal_direction, confidence_percentage)
    """
    buy_votes = sum(1 for signal in indicator_signals.values() if signal == 'BUY')
    sell_votes = sum(1 for signal in indicator_signals.values() if signal == 'SELL')
    total = len(indicator_signals)
    
    if buy_votes > sell_votes:
        confidence = buy_votes / total
        return 'BUY', confidence
    elif sell_votes > buy_votes:
        confidence = sell_votes / total
        return 'SELL', confidence
    else:
        return 'NEUTRAL', 0.5

def calculate_support_resistance(candles: List[Dict], lookback: int = 20) -> Tuple[float, float]:
    """
    Calculate dynamic support and resistance levels
    """
    if len(candles) < lookback:
        return 0.0, 0.0
    
    recent = candles[-lookback:]
    highs = [c['high'] for c in recent]
    lows = [c['low'] for c in recent]
    
    resistance = max(highs)
    support = min(lows)
    
    return support, resistance

def calculate_fibonacci_levels(high: float, low: float) -> Dict[str, float]:
    """
    Calculate Fibonacci retracement and extension levels
    """
    diff = high - low
    
    return {
        'level_0': high,
        'level_236': high - (diff * 0.236),
        'level_382': high - (diff * 0.382),
        'level_500': high - (diff * 0.5),
        'level_618': high - (diff * 0.618),
        'level_786': high - (diff * 0.786),
        'level_100': low,
        'extension_127': low - (diff * 0.127),
        'extension_162': low - (diff * 0.162),
        'extension_200': low - (diff * 0.200),
        'extension_261': low - (diff * 0.261)
    }

def calculate_pivot_points(candle: Dict) -> Dict[str, float]:
    """
    Calculate daily pivot points
    """
    h = candle['high']
    l = candle['low']
    c = candle['close']
    
    pivot = (h + l + c) / 3
    r1 = (2 * pivot) - l
    r2 = pivot + (h - l)
    s1 = (2 * pivot) - h
    s2 = pivot - (h - l)
    
    return {
        'pivot': pivot,
        'r1': r1,
        'r2': r2,
        's1': s1,
        's2': s2
    }

def identify_trend(ema_fast: float, ema_slow: float) -> str:
    """
    Identify trend direction
    """
    if ema_fast > ema_slow:
        return 'UPTREND'
    elif ema_fast < ema_slow:
        return 'DOWNTREND'
    else:
        return 'NEUTRAL'

def calculate_risk_reward(entry: float, stop_loss: float, take_profit: float) -> float:
    """
    Calculate risk-reward ratio
    """
    risk = abs(entry - stop_loss)
    reward = abs(take_profit - entry)
    
    return reward / risk if risk > 0 else 0.0

def format_signal_message(asset: str, signal: str, accuracy: float, indicators_agree: int, price: float) -> str:
    """
    Format signal for Telegram delivery
    """
    emoji = '📈' if signal == 'BUY' else '📉'
    
    message = f"""
{emoji} **{signal} SIGNAL** - {asset}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 Current Price: ${price:.5f}
📊 Accuracy: {accuracy*100:.2f}%
✅ Indicators Agree: {indicators_agree}/16
⏱️ Timeframe: 1-MIN
⏰ Expiry: 60 seconds
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """
    
    return message

def is_market_hours(symbol: str) -> bool:
    """
    Check if market is open for trading
    """
    now = datetime.now()
    
    forex_pairs = ['EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'AUDUSD', 'NZDUSD', 'USDCAD']
    
    if symbol in forex_pairs:
        # Forex trades 24/5 (Sunday 5PM - Friday 5PM EST)
        return now.weekday() < 4 or (now.weekday() == 4 and now.hour < 17) or (now.weekday() == 6 and now.hour >= 17)
    
    # Crypto trades 24/7
    if symbol in ['BTCUSD', 'ETHUSD']:
        return True
    
    # Stocks trade during market hours (9:30 AM - 4:00 PM EST)
    if symbol in ['US500', 'US100']:
        return 9.5 <= now.hour <= 16
    
    return True