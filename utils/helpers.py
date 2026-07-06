import numpy as np
from typing import List, Dict, Tuple

def consensus_voting(indicator_signals: Dict[str, str]) -> Tuple[str, float]:
    """Determine consensus signal from multiple indicators"""
    buy_votes = sum(1 for signal in indicator_signals.values() if signal == 'BUY')
    sell_votes = sum(1 for signal in indicator_signals.values() if signal == 'SELL')
    total = len(indicator_signals)
    
    if buy_votes > sell_votes:
        confidence = buy_votes / total
        return 'BUY', confidence
    elif sell_votes > buy_votes:
        confidence = sell_votes / total
        return 'SELL', confidence
    return 'NEUTRAL', 0.5

def calculate_support_resistance(candles: List[Dict], lookback: int = 20) -> Tuple[float, float]:
    """Calculate dynamic support and resistance levels"""
    if len(candles) < lookback:
        return 0.0, 0.0
    recent = candles[-lookback:]
    highs = [c['high'] for c in recent]
    lows = [c['low'] for c in recent]
    return min(lows), max(highs)

def calculate_fibonacci_levels(high: float, low: float) -> Dict[str, float]:
    """Calculate Fibonacci retracement and extension levels"""
    diff = high - low
    return {
        'level_0': high,
        'level_236': high - (diff * 0.236),
        'level_382': high - (diff * 0.382),
        'level_500': high - (diff * 0.5),
        'level_618': high - (diff * 0.618),
        'level_786': high - (diff * 0.786),
        'level_100': low,
    }

def calculate_pivot_points(candle: Dict) -> Dict[str, float]:
    """Calculate daily pivot points"""
    h, l, c = candle['high'], candle['low'], candle['close']
    pivot = (h + l + c) / 3
    return {
        'pivot': pivot,
        'r1': (2 * pivot) - l,
        'r2': pivot + (h - l),
        's1': (2 * pivot) - h,
        's2': pivot - (h - l)
    }