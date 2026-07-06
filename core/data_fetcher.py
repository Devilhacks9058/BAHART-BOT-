import pandas as pd
import numpy as np
from typing import List, Dict, Tuple
from datetime import datetime, timedelta
from utils.logger import setup_logger
from utils.config import TIMEFRAME, ASSETS

logger = setup_logger('DataFetcher')

class DataFetcher:
    """Fetch and manage market data"""
    
    def __init__(self):
        self.candle_data = {}
        self.last_update = {}
        
    async def fetch_candles(self, asset: str, limit: int = 100) -> List[Dict]:
        """
        Fetch candle data from Pocket Option
        Returns list of candle dictionaries with OHLCV data
        """
        try:
            # This would be implemented with actual API calls
            # For now, returning placeholder structure
            
            candles = []
            # Implementation would fetch real data via WebSocket
            
            logger.info(f"Fetched {len(candles)} candles for {asset}")
            return candles
            
        except Exception as e:
            logger.error(f"Error fetching candles for {asset}: {e}")
            return []
    
    async def fetch_current_price(self, asset: str) -> float:
        """
        Get current price for asset
        """
        try:
            candles = self.candle_data.get(asset, [])
            if candles:
                return candles[-1]['close']
            return 0.0
        except Exception as e:
            logger.error(f"Error fetching current price: {e}")
            return 0.0
    
    def calculate_returns(self, candles: List[Dict]) -> List[float]:
        """
        Calculate log returns from candles
        """
        if len(candles) < 2:
            return []
        
        closes = np.array([c['close'] for c in candles])
        returns = np.diff(np.log(closes))
        return returns.tolist()
    
    def prepare_dataframe(self, candles: List[Dict]) -> pd.DataFrame:
        """
        Convert candles to pandas DataFrame
        """
        if not candles:
            return pd.DataFrame()
        
        df = pd.DataFrame(candles)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)
        
        return df