import numpy as np
from typing import List, Dict
from utils.logger import setup_logger

logger = setup_logger('TechnicalIndicators')

class TechnicalIndicators:
    """Calculate all technical indicators (20+ optimized for 1-minute timeframe)"""
    
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
        min_len = min(len(ema_fast), len(ema_slow))
        macd_line = np.array(ema_fast[-min_len:]) - np.array(ema_slow[-min_len:])
        signal_line = self.calculate_ema(macd_line.tolist(), signal)
        histogram = macd_line[-len(signal_line):] - np.array(signal_line)
        return {'macd': macd_line.tolist(), 'signal': signal_line, 'histogram': histogram.tolist()}
    
    def calculate_bollinger_bands(self, prices: List[float], period: int = 20, deviation: int = 2) -> Dict:
        """Calculate Bollinger Bands"""
        sma = self.calculate_sma(prices, period)
        if not sma:
            return {}
        std_dev = [np.std(prices[i:i+period]) for i in range(len(prices)-period+1)]
        upper_band = np.array(sma) + (deviation * np.array(std_dev))
        lower_band = np.array(sma) - (deviation * np.array(std_dev))
        return {'middle': sma, 'upper': upper_band.tolist(), 'lower': lower_band.tolist()}