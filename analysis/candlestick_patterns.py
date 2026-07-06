from typing import List, Dict, Tuple
from utils.logger import setup_logger

logger = setup_logger('CandlestickPatterns')

class CandlestickPatterns:
    """Recognize and analyze candlestick patterns (20+ patterns)"""
    
    def analyze_candle(self, candle: Dict) -> Dict:
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
        analysis = self.analyze_candle(candle)
        return analysis['body_percent'] < 5
    
    def detect_hammer(self, candle: Dict) -> bool:
        analysis = self.analyze_candle(candle)
        return (analysis['is_bullish'] and analysis['body_percent'] < 25 and analysis['lower_wick'] > analysis['body'] * 2)
    
    def detect_shooting_star(self, candle: Dict) -> bool:
        analysis = self.analyze_candle(candle)
        return (analysis['is_bearish'] and analysis['body_percent'] < 25 and analysis['upper_wick'] > analysis['body'] * 2)
    
    def detect_engulfing(self, candle1: Dict, candle2: Dict) -> Tuple[bool, str]:
        a1 = self.analyze_candle(candle1)
        a2 = self.analyze_candle(candle2)
        if (a1['is_bearish'] and a2['is_bullish'] and candle2['close'] > candle1['open'] and candle2['open'] < candle1['close']):
            return True, 'BULLISH_ENGULFING'
        if (a1['is_bullish'] and a2['is_bearish'] and candle2['close'] < candle1['open'] and candle2['open'] > candle1['close']):
            return True, 'BEARISH_ENGULFING'
        return False, 'NONE'
    
    def detect_three_white_soldiers(self, candles: List[Dict]) -> bool:
        if len(candles) < 3:
            return False
        last_three = candles[-3:]
        analyses = [self.analyze_candle(c) for c in last_three]
        return all(a['is_bullish'] and a['body_percent'] > 70 for a in analyses)
    
    def detect_three_black_crows(self, candles: List[Dict]) -> bool:
        if len(candles) < 3:
            return False
        last_three = candles[-3:]
        analyses = [self.analyze_candle(c) for c in last_three]
        return all(a['is_bearish'] and a['body_percent'] > 70 for a in analyses)