from typing import List, Dict, Tuple
from utils.logger import setup_logger

logger = setup_logger('PriceAction')

class PriceAction:
    """Advanced price action analysis: Market Structure, BOS, CHoCH, Liquidity, etc."""
    
    def identify_market_structure(self, candles: List[Dict], lookback: int = 20) -> str:
        if len(candles) < lookback:
            return 'INSUFFICIENT_DATA'
        recent = candles[-lookback:]
        highs = [c['high'] for c in recent]
        lows = [c['low'] for c in recent]
        if all(highs[i] > highs[i-1] for i in range(1, len(highs))) and all(lows[i] > lows[i-1] for i in range(1, len(lows))):
            return 'UPTREND'
        if all(highs[i] < highs[i-1] for i in range(1, len(highs))) and all(lows[i] < lows[i-1] for i in range(1, len(lows))):
            return 'DOWNTREND'
        return 'SIDEWAYS'
    
    def detect_break_of_structure(self, candles: List[Dict]) -> Tuple[bool, str]:
        if len(candles) < 10:
            return False, 'NONE'
        recent = candles[-10:]
        highs = [c['high'] for c in recent]
        lows = [c['low'] for c in recent]
        swing_high = max(highs[:-1])
        swing_low = min(lows[:-1])
        current_high = candles[-1]['high']
        current_low = candles[-1]['low']
        if current_high > swing_high:
            return True, 'BOS_UP'
        if current_low < swing_low:
            return True, 'BOS_DOWN'
        return False, 'NONE'
    
    def identify_liquidity_sweeps(self, candles: List[Dict]) -> List[Dict]:
        sweeps = []
        if len(candles) < 10:
            return sweeps
        recent_high = max(c['high'] for c in candles[-10:-1])
        recent_low = min(c['low'] for c in candles[-10:-1])
        current = candles[-1]
        if current['high'] > recent_high and current['low'] < recent_high:
            sweeps.append({'type': 'LIQUIDITY_SWEEP_HIGH', 'level': recent_high, 'direction': 'BEARISH'})
        if current['low'] < recent_low and current['high'] > recent_low:
            sweeps.append({'type': 'LIQUIDITY_SWEEP_LOW', 'level': recent_low, 'direction': 'BULLISH'})
        return sweeps