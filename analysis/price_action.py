from typing import List, Dict, Tuple
from utils.logger import setup_logger

logger = setup_logger('PriceAction')

class PriceAction:
    """Advanced price action analysis: Market Structure, BOS, CHoCH, Liquidity, etc."""
    
    def identify_market_structure(self, candles: List[Dict], lookback: int = 20) -> str:
        """
        Identify current market structure (Higher Highs & Higher Lows, Lower Lows & Lower Highs, etc.)
        """
        if len(candles) < lookback:
            return 'INSUFFICIENT_DATA'
        
        recent = candles[-lookback:]
        highs = [c['high'] for c in recent]
        lows = [c['low'] for c in recent]
        
        # Check for Higher Highs & Higher Lows (Uptrend)
        if all(highs[i] > highs[i-1] for i in range(1, len(highs))) and \
           all(lows[i] > lows[i-1] for i in range(1, len(lows))):
            return 'UPTREND'
        
        # Check for Lower Lows & Lower Highs (Downtrend)
        if all(highs[i] < highs[i-1] for i in range(1, len(highs))) and \
           all(lows[i] < lows[i-1] for i in range(1, len(lows))):
            return 'DOWNTREND'
        
        return 'SIDEWAYS'
    
    def detect_break_of_structure(self, candles: List[Dict]) -> Tuple[bool, str]:
        """
        Detect Break of Structure (BOS) - Breaking previous swing high or low
        """
        if len(candles) < 10:
            return False, 'NONE'
        
        recent = candles[-10:]
        highs = [c['high'] for c in recent]
        lows = [c['low'] for c in recent]
        
        # Find recent swing high and swing low
        swing_high = max(highs[:-1])
        swing_low = min(lows[:-1])
        
        current_high = candles[-1]['high']
        current_low = candles[-1]['low']
        
        # BOS to the upside
        if current_high > swing_high:
            return True, 'BOS_UP'
        
        # BOS to the downside
        if current_low < swing_low:
            return True, 'BOS_DOWN'
        
        return False, 'NONE'
    
    def detect_change_of_character(self, candles: List[Dict]) -> Tuple[bool, str]:
        """
        Detect Change of Character (CHoCH) - Shift in market structure
        """
        if len(candles) < 20:
            return False, 'NONE'
        
        structure_prev = self._get_structure_at_index(candles, -20, -11)
        structure_curr = self._get_structure_at_index(candles, -10, -1)
        
        if structure_prev != structure_curr and structure_prev != 'SIDEWAYS':
            return True, f'CHOCH_{structure_curr}'
        
        return False, 'NONE'
    
    def identify_liquidity_sweeps(self, candles: List[Dict]) -> List[Dict]:
        """
        Identify liquidity sweeps (price hitting recent lows/highs)
        """
        sweeps = []
        
        if len(candles) < 10:
            return sweeps
        
        recent_high = max(c['high'] for c in candles[-10:-1])
        recent_low = min(c['low'] for c in candles[-10:-1])
        
        current = candles[-1]
        
        # Liquidated above recent high
        if current['high'] > recent_high and current['low'] < recent_high:
            sweeps.append({
                'type': 'LIQUIDITY_SWEEP_HIGH',
                'level': recent_high,
                'direction': 'BEARISH'
            })
        
        # Liquidated below recent low
        if current['low'] < recent_low and current['high'] > recent_low:
            sweeps.append({
                'type': 'LIQUIDITY_SWEEP_LOW',
                'level': recent_low,
                'direction': 'BULLISH'
            })
        
        return sweeps
    
    def identify_order_blocks(self, candles: List[Dict], lookback: int = 20) -> List[Dict]:
        """
        Identify Order Blocks - Areas of supply/demand
        """
        blocks = []
        
        if len(candles) < lookback:
            return blocks
        
        recent = candles[-lookback:]
        
        # Find strong bullish candles (potential demand blocks)
        for i, candle in enumerate(recent):
            body = abs(candle['close'] - candle['open'])
            range_size = candle['high'] - candle['low']
            
            if body > range_size * 0.7 and candle['close'] > candle['open']:
                blocks.append({
                    'type': 'DEMAND_BLOCK',
                    'high': candle['high'],
                    'low': candle['low'],
                    'index': i
                })
        
        return blocks
    
    def identify_fair_value_gaps(self, candles: List[Dict]) -> List[Dict]:
        """
        Identify Fair Value Gaps (FVG) - Price gaps not yet filled
        """
        gaps = []
        
        if len(candles) < 3:
            return gaps
        
        for i in range(2, len(candles)):
            candle_1 = candles[i-2]
            candle_2 = candles[i-1]
            candle_3 = candles[i]
            
            # Bullish FVG: candle_1 low > candle_3 high
            if candle_1['low'] > candle_3['high']:
                gaps.append({
                    'type': 'BULLISH_FVG',
                    'top': candle_1['low'],
                    'bottom': candle_3['high'],
                    'candle_index': i
                })
            
            # Bearish FVG: candle_1 high < candle_3 low
            if candle_1['high'] < candle_3['low']:
                gaps.append({
                    'type': 'BEARISH_FVG',
                    'top': candle_3['low'],
                    'bottom': candle_1['high'],
                    'candle_index': i
                })
        
        return gaps
    
    def _get_structure_at_index(self, candles: List[Dict], start: int, end: int) -> str:
        """Helper to get structure at specific candle range"""
        range_candles = candles[start:end+1]
        highs = [c['high'] for c in range_candles]
        lows = [c['low'] for c in range_candles]
        
        if all(highs[i] > highs[i-1] if i > 0 else True for i in range(len(highs))):
            return 'UPTREND'
        elif all(highs[i] < highs[i-1] if i > 0 else True for i in range(len(highs))):
            return 'DOWNTREND'
        else:
            return 'SIDEWAYS'