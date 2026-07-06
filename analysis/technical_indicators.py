import pandas as pd
import numpy as np
from typing import List, Dict, Tuple
from utils.logger import setup_logger
from utils.config import INDICATOR_SETTINGS

logger = setup_logger('TechnicalIndicators')

class TechnicalIndicators:
    """Calculate all technical indicators (20+ optimized for 1-minute timeframe)"""
    
    def __init__(self):
        self.settings = INDICATOR_SETTINGS
    
    # Moving Averages
    def calculate_ema(self, prices: List[float], period: int) -> List[float]:
        """Calculate Exponential Moving Average"""
        if len(prices) < period:
            return []
        
        ema = []
        multiplier = 2 / (period + 1)
        
        sma = sum(prices[:period]) / period
        ema.append(sma)
        
        for price in prices[period:]:
            ema_val = (price - ema[-1]) * multiplier + ema[-1]
            ema.append(ema_val)
        
        return ema
    
    def calculate_sma(self, prices: List[float], period: int) -> List[float]:
        """Calculate Simple Moving Average"""
        if len(prices) < period:
            return []
        
        return [np.mean(prices[i:i+period]) for i in range(len(prices)-period+1)]
    
    # Momentum Indicators
    def calculate_rsi(self, prices: List[float], period: int = 7) -> List[float]:
        """Calculate RSI (optimized for 1-min: period=7)"""
        if len(prices) < period + 1:
            return []
        
        deltas = np.diff(prices)
        gains = np.where(deltas > 0, deltas, 0)
        losses = np.where(deltas < 0, -deltas, 0)
        
        avg_gains = np.convolve(gains, np.ones(period)/period, mode='valid')
        avg_losses = np.convolve(losses, np.ones(period)/period, mode='valid')
        
        rs = avg_gains / (avg_losses + 1e-10)
        rsi = 100 - (100 / (1 + rs))
        
        return rsi.tolist()
    
    def calculate_macd(self, prices: List[float], fast: int = 12, slow: int = 26, signal: int = 9) -> Dict:
        """Calculate MACD"""
        ema_fast = self.calculate_ema(prices, fast)
        ema_slow = self.calculate_ema(prices, slow)
        
        # Align lengths
        min_len = min(len(ema_fast), len(ema_slow))
        macd_line = np.array(ema_fast[-min_len:]) - np.array(ema_slow[-min_len:])
        signal_line = self.calculate_ema(macd_line.tolist(), signal)
        histogram = macd_line[-len(signal_line):] - np.array(signal_line)
        
        return {
            'macd': macd_line.tolist(),
            'signal': signal_line,
            'histogram': histogram.tolist()
        }
    
    def calculate_stochastic(self, highs: List[float], lows: List[float], closes: List[float], k_period: int = 5, d_period: int = 3) -> Dict:
        """Calculate Stochastic Oscillator"""
        if len(closes) < k_period:
            return {}
        
        lowest_lows = [min(lows[i:i+k_period]) for i in range(len(lows)-k_period+1)]
        highest_highs = [max(highs[i:i+k_period]) for i in range(len(highs)-k_period+1)]
        
        k_percent = [100 * ((closes[i+k_period-1] - lowest_lows[i]) / (highest_highs[i] - lowest_lows[i] + 1e-10)) 
                    for i in range(len(lowest_lows))]
        d_percent = self.calculate_sma(k_percent, d_period)
        
        return {
            'k_percent': k_percent,
            'd_percent': d_percent
        }
    
    def calculate_bollinger_bands(self, prices: List[float], period: int = 20, deviation: int = 2) -> Dict:
        """Calculate Bollinger Bands"""
        sma = self.calculate_sma(prices, period)
        
        if not sma:
            return {}
        
        std_dev = [np.std(prices[i:i+period]) for i in range(len(prices)-period+1)]
        
        upper_band = np.array(sma) + (deviation * np.array(std_dev))
        lower_band = np.array(sma) - (deviation * np.array(std_dev))
        
        return {
            'middle': sma,
            'upper': upper_band.tolist(),
            'lower': lower_band.tolist()
        }
    
    def calculate_atr(self, highs: List[float], lows: List[float], closes: List[float], period: int = 14) -> List[float]:
        """Calculate Average True Range"""
        if len(closes) < 1:
            return []
        
        tr = []
        for i in range(len(closes)):
            if i == 0:
                tr.append(highs[i] - lows[i])
            else:
                tr.append(max(
                    highs[i] - lows[i],
                    abs(highs[i] - closes[i-1]),
                    abs(lows[i] - closes[i-1])
                ))
        
        atr = self.calculate_sma(tr, period)
        return atr
    
    def calculate_adx(self, highs: List[float], lows: List[float], closes: List[float], period: int = 14) -> Dict:
        """Calculate ADX (Average Directional Index)"""
        # Simplified ADX calculation
        plus_dm = []
        minus_dm = []
        
        for i in range(1, len(closes)):
            up_move = highs[i] - highs[i-1]
            down_move = lows[i-1] - lows[i]
            
            if up_move > down_move and up_move > 0:
                plus_dm.append(up_move)
                minus_dm.append(0)
            elif down_move > up_move and down_move > 0:
                plus_dm.append(0)
                minus_dm.append(down_move)
            else:
                plus_dm.append(0)
                minus_dm.append(0)
        
        atr_vals = self.calculate_atr(highs, lows, closes, period)
        
        # Calculate DI+ and DI-
        plus_di = [(sum(plus_dm[-period:]) / sum(atr_vals[-period:]) * 100) if atr_vals else 0]
        minus_di = [(sum(minus_dm[-period:]) / sum(atr_vals[-period:]) * 100) if atr_vals else 0]
        
        return {
            'plus_di': plus_di,
            'minus_di': minus_di
        }
    
    # Add more indicator methods...
    # (parabolic_sar, ichimoku, fibonacci, pivot_points, etc.)