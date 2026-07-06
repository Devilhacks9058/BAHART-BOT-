import pandas as pd
import numpy as np
from typing import List, Dict
from utils.logger import setup_logger

logger = setup_logger('DataFetcher')

class DataFetcher:
    """Fetch and manage market data"""
    
    def __init__(self):
        self.candle_data = {}
        self.last_update = {}
        
    async def fetch_candles(self, asset: str, limit: int = 100) -> List[Dict]:
        """Fetch candle data from Pocket Option"""
        try:
            candles = []
            logger.info(f"Fetched {len(candles)} candles for {asset}")
            return candles
        except Exception as e:
            logger.error(f"Error fetching candles for {asset}: {e}")
            return []
    
    async def fetch_current_price(self, asset: str) -> float:
        """Get current price for asset"""
        try:
            candles = self.candle_data.get(asset, [])
            if candles:
                return candles[-1]['close']
            return 0.0
        except Exception as e:
            logger.error(f"Error fetching current price: {e}")
            return 0.0
    
    def prepare_dataframe(self, candles: List[Dict]) -> pd.DataFrame:
        """Convert candles to pandas DataFrame"""
        if not candles:
            return pd.DataFrame()
        df = pd.DataFrame(candles)
        return df