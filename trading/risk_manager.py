# Risk Manager - Manage Trading Risk

from utils.logger import setup_logger
from utils.config import RISK_MANAGEMENT
from datetime import datetime, timedelta

logger = setup_logger('RiskManager')

class RiskManager:
    """Manage trading risk and position sizing"""
    
    def __init__(self, account_balance: float):
        self.account_balance = account_balance
        self.daily_loss = 0.0
        self.daily_reset_time = datetime.now()
        self.position_history = []
    
    def check_daily_loss_limit(self) -> bool:
        """Check if daily loss limit exceeded"""
        max_daily_loss = self.account_balance * RISK_MANAGEMENT['max_daily_loss']
        if self.daily_loss >= max_daily_loss:
            logger.warning(f"Daily loss limit reached: {self.daily_loss}/{max_daily_loss}")
            return False
        return True
    
    def reset_daily_loss(self):
        """Reset daily loss counter at midnight"""
        now = datetime.now()
        if now.day != self.daily_reset_time.day:
            self.daily_loss = 0.0
            self.daily_reset_time = now
            logger.info("Daily loss counter reset")
    
    def calculate_position_size(self, account_balance: float, risk_percentage: float = 5) -> float:
        """Calculate safe position size"""
        max_position = account_balance * (risk_percentage / 100)
        max_allowed = account_balance * RISK_MANAGEMENT['max_position_size']
        return min(max_position, max_allowed)
    
    def calculate_stop_loss(self, entry_price: float, signal: str) -> float:
        """Calculate stop loss level"""
        stop_pips = RISK_MANAGEMENT['stop_loss_pips']
        pip_value = 0.0001  # For forex pairs
        
        if signal == 'BUY':
            return entry_price - (stop_pips * pip_value)
        else:
            return entry_price + (stop_pips * pip_value)
    
    def calculate_take_profit(self, entry_price: float, stop_loss: float, signal: str) -> float:
        """Calculate take profit level"""
        risk = abs(entry_price - stop_loss)
        ratio = RISK_MANAGEMENT['take_profit_ratio']
        
        if signal == 'BUY':
            return entry_price + (risk * ratio)
        else:
            return entry_price - (risk * ratio)
    
    def record_trade_result(self, pnl: float):
        """Record trade result for risk tracking"""
        if pnl < 0:
            self.daily_loss += abs(pnl)
        self.position_history.append({'pnl': pnl, 'timestamp': datetime.now()})
        logger.info(f"Trade result recorded: P&L {pnl}")