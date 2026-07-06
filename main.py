#!/usr/bin/env python3
# BAHART Trading Bot - Main Entry Point

import asyncio
import logging
from utils.config import TELEGRAM_BOT_TOKEN, POCKET_OPTION_SESSION_TOKEN, POCKET_OPTION_UID
from utils.logger import setup_logger
from core.websocket_manager import WebSocketManager
from core.data_fetcher import DataFetcher
from core.signal_generator import SignalGenerator

logger = setup_logger('BAHART-BOT-MAIN')

class BaahartBot:
    def __init__(self):
        self.ws_manager = WebSocketManager(POCKET_OPTION_SESSION_TOKEN, POCKET_OPTION_UID)
        self.data_fetcher = DataFetcher()
        self.signal_generator = SignalGenerator()
        
    async def start(self):
        """Start the bot"""
        logger.info("\n" + "="*60)
        logger.info("BAHART TRADING BOT INITIALIZED")
        logger.info("="*60)
        logger.info(f"Session Token: {POCKET_OPTION_SESSION_TOKEN[:10]}...")
        logger.info(f"UID: {POCKET_OPTION_UID}")
        logger.info("="*60 + "\n")
        
        # Register WebSocket callbacks
        self.ws_manager.register_callback('chart', self._handle_chart_update)
        
        # Connect to WebSocket
        try:
            self.ws_manager.connect()
        except Exception as e:
            logger.error(f"Failed to connect: {e}")
    
    def _handle_chart_update(self, data):
        """Handle incoming chart data from WebSocket"""
        try:
            logger.debug(f"Chart update received: {data}")
        except Exception as e:
            logger.error(f"Error handling chart update: {e}")

if __name__ == '__main__':
    bot = BaahartBot()
    try:
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
        bot.ws_manager.disconnect()
    except Exception as e:
        logger.error(f"Fatal error: {e}")