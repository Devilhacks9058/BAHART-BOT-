import logging
import os
from logging.handlers import RotatingFileHandler

LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/bahart_bot.log'

def setup_logger(name: str) -> logging.Logger:
    """Setup logger with console and file handlers"""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, LOG_LEVEL))
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, LOG_LEVEL))
    
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=10485760, backupCount=5
    )
    file_handler.setLevel(getattr(logging, LOG_LEVEL))
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

logger = setup_logger('BAHART-BOT')