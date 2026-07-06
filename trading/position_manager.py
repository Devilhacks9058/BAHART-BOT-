# Position Manager - Track Open Positions

from typing import Dict, List
from utils.logger import setup_logger
from datetime import datetime

logger = setup_logger('PositionManager')

class PositionManager:
    """Manage trading positions"""
    
    def __init__(self):
        self.open_positions: Dict = {}
        self.closed_positions: List = []
        self.total_wins = 0
        self.total_losses = 0
    
    def open_position(self, asset: str, signal: str, entry_price: float, amount: float):
        """Open a new position"""
        position = {
            'asset': asset,
            'signal': signal,
            'entry_price': entry_price,
            'amount': amount,
            'entry_time': datetime.now(),
            'status': 'OPEN'
        }
        self.open_positions[f"{asset}_{len(self.open_positions)}"] = position
        logger.info(f"Position opened: {asset} {signal} @ {entry_price}")
        return position
    
    def close_position(self, position_id: str, exit_price: float):
        """Close an open position"""
        if position_id in self.open_positions:
            position = self.open_positions[position_id]
            position['exit_price'] = exit_price
            position['status'] = 'CLOSED'
            position['exit_time'] = datetime.now()
            
            # Calculate P&L
            if position['signal'] == 'BUY':
                pnl = (exit_price - position['entry_price']) * position['amount']
            else:
                pnl = (position['entry_price'] - exit_price) * position['amount']
            
            position['pnl'] = pnl
            
            if pnl > 0:
                self.total_wins += 1
            else:
                self.total_losses += 1
            
            self.closed_positions.append(position)
            del self.open_positions[position_id]
            logger.info(f"Position closed: {position_id} P&L: {pnl}")
            return position
        return None
    
    def get_open_positions(self) -> Dict:
        """Get all open positions"""
        return self.open_positions
    
    def get_win_rate(self) -> float:
        """Calculate win rate"""
        total = self.total_wins + self.total_losses
        if total == 0:
            return 0.0
        return (self.total_wins / total) * 100
    
    def get_total_pnl(self) -> float:
        """Calculate total P&L"""
        return sum(p.get('pnl', 0) for p in self.closed_positions)