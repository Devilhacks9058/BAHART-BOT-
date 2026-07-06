from typing import List, Dict, Tuple
from utils.logger import setup_logger

logger = setup_logger('CandlestickPatterns')

class CandlestickPatterns:
    """Recognize and analyze candlestick patterns (20+ patterns)"""
    
    def __init__(self):
        self.patterns_found = []
    
    def analyze_candle(self, candle: Dict) -> Dict:
        """
        Analyze a single candle for pattern characteristics
        """
        open_price = candle['open']
        close_price = candle['close']
        high_price = candle['high']
        low_price = candle['low']
        
        body = abs(close_price - open_price)
        upper_wick = high_price - max(open_price, close_price)
        lower_wick = min(open_price, close_price) - low_price
        total_range = high_price - low_price
        
        return {
            'body': body,
            'upper_wick': upper_wick,
            'lower_wick': lower_wick,
            'total_range': total_range,
            'is_bullish': close_price > open_price,
            'is_bearish': close_price < open_price,
            'body_percent': (body / total_range * 100) if total_range > 0 else 0
        }
    
    def detect_doji(self, candle: Dict) -> bool:
        """Doji: Opening and closing prices equal; indecision"""
        analysis = self.analyze_candle(candle)
        return analysis['body_percent'] < 5  # Very small body
    
    def detect_hammer(self, candle: Dict, is_at_support: bool = True) -> bool:
        """Hammer: Small body, long lower wick; bullish reversal at support"""
        analysis = self.analyze_candle(candle)
        return (analysis['is_bullish'] and 
                analysis['body_percent'] < 25 and 
                analysis['lower_wick'] > analysis['body'] * 2)
    
    def detect_shooting_star(self, candle: Dict, is_at_resistance: bool = True) -> bool:
        """Shooting Star: Small body, long upper wick; bearish at resistance"""
        analysis = self.analyze_candle(candle)
        return (analysis['is_bearish'] and 
                analysis['body_percent'] < 25 and 
                analysis['upper_wick'] > analysis['body'] * 2)
    
    def detect_marubozu(self, candle: Dict) -> bool:
        """Marubozu: Long body, little to no wicks; strong conviction"""
        analysis = self.analyze_candle(candle)
        return (analysis['body_percent'] > 90 and 
                analysis['upper_wick'] < analysis['body'] * 0.1 and 
                analysis['lower_wick'] < analysis['body'] * 0.1)
    
    def detect_engulfing(self, candle1: Dict, candle2: Dict) -> Tuple[bool, str]:
        """Engulfing pattern (bullish or bearish)"""
        a1 = self.analyze_candle(candle1)
        a2 = self.analyze_candle(candle2)
        
        # Bullish engulfing
        if (a1['is_bearish'] and a2['is_bullish'] and 
            candle2['close'] > candle1['open'] and 
            candle2['open'] < candle1['close']):
            return True, 'BULLISH_ENGULFING'
        
        # Bearish engulfing
        if (a1['is_bullish'] and a2['is_bearish'] and 
            candle2['close'] < candle1['open'] and 
            candle2['open'] > candle1['close']):
            return True, 'BEARISH_ENGULFING'
        
        return False, 'NONE'
    
    def detect_morning_star(self, candle1: Dict, candle2: Dict, candle3: Dict) -> bool:
        """Morning Star: Long red, small gap, long green; bullish reversal"""
        a1 = self.analyze_candle(candle1)
        a2 = self.analyze_candle(candle2)
        a3 = self.analyze_candle(candle3)
        
        return (a1['is_bearish'] and a1['body_percent'] > 70 and
                a2['body_percent'] < 40 and
                a3['is_bullish'] and a3['body_percent'] > 70 and
                candle3['close'] > candle1['open'])
    
    def detect_evening_star(self, candle1: Dict, candle2: Dict, candle3: Dict) -> bool:
        """Evening Star: Long green, small gap, long red; bearish reversal"""
        a1 = self.analyze_candle(candle1)
        a2 = self.analyze_candle(candle2)
        a3 = self.analyze_candle(candle3)
        
        return (a1['is_bullish'] and a1['body_percent'] > 70 and
                a2['body_percent'] < 40 and
                a3['is_bearish'] and a3['body_percent'] > 70 and
                candle3['close'] < candle1['open'])
    
    def detect_three_white_soldiers(self, candles: List[Dict]) -> bool:
        """Three White Soldiers: Three consecutive long green candles"""
        if len(candles) < 3:
            return False
        
        last_three = candles[-3:]
        analyses = [self.analyze_candle(c) for c in last_three]
        
        return all(a['is_bullish'] and a['body_percent'] > 70 for a in analyses)
    
    def detect_three_black_crows(self, candles: List[Dict]) -> bool:
        """Three Black Crows: Three consecutive long red candles"""
        if len(candles) < 3:
            return False
        
        last_three = candles[-3:]
        analyses = [self.analyze_candle(c) for c in last_three]
        
        return all(a['is_bearish'] and a['body_percent'] > 70 for a in analyses)
    
    # More patterns...
    # (Harami, Tweezer Top/Bottom, Piercing Line, Dark Cloud, etc.)