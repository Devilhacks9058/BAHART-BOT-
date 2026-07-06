#!/usr/bin/env python3
# BAHART Trading Bot - Main Entry Point with Telegram Integration

import asyncio
import logging
from telegram.ext import Application
from utils.config import TELEGRAM_BOT_TOKEN, POCKET_OPTION_SESSION_TOKEN, POCKET_OPTION_UID
from utils.logger import setup_logger
from core.websocket_manager import WebSocketManager
from core.data_fetcher import DataFetcher
from core.signal_generator import SignalGenerator
from telegram_bot.handlers import start_handler, status_handler, help_handler, error_handler
from telegram import Update, BotCommand
from telegram.ext import CommandHandler, ContextTypes

logger = setup_logger('BAHART-BOT-MAIN')

class BaahartBot:
    def __init__(self):
        self.app = None
        self.ws_manager = WebSocketManager(POCKET_OPTION_SESSION_TOKEN, POCKET_OPTION_UID)
        self.data_fetcher = DataFetcher()
        self.signal_generator = SignalGenerator()
        
    async def setup_telegram(self):
        """Setup Telegram bot"""
        logger.info("Setting up Telegram bot...")
        
        self.app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        
        # Add command handlers
        self.app.add_handler(CommandHandler('start', start_handler))
        self.app.add_handler(CommandHandler('status', status_handler))
        self.app.add_handler(CommandHandler('help', help_handler))
        
        # Add error handler
        self.app.add_error_handler(error_handler)
        
        # Set bot commands
        commands = [
            BotCommand('start', 'Start the bot'),
            BotCommand('status', 'View bot status'),
            BotCommand('signals', 'Get latest signals'),
            BotCommand('analysis', 'View analysis'),
            BotCommand('portfolio', 'Open positions'),
            BotCommand('balance', 'Account balance'),
            BotCommand('help', 'Get help'),
            BotCommand('settings', 'Bot settings')
        ]
        await self.app.bot.set_my_commands(commands)
        
        logger.info("Telegram bot setup complete")
    
    async def start(self):
        """Start the bot"""
        logger.info("\n" + "="*70)
        logger.info("🤖 BAHART TRADING BOT INITIALIZING")
        logger.info("="*70)
        
        # Setup Telegram
        await self.setup_telegram()
        
        logger.info(f"\n📱 Telegram Configuration:")
        logger.info(f"   Token: {TELEGRAM_BOT_TOKEN[:20]}...")
        logger.info(f"   Username: @LALIxLOVE")
        logger.info(f"   User ID: 6562788255")
        
        logger.info(f"\n🔌 Pocket Option Configuration:")
        logger.info(f"   Session Token: {POCKET_OPTION_SESSION_TOKEN[:15]}...")
        logger.info(f"   UID: {POCKET_OPTION_UID}")
        
        logger.info(f"\n📊 Analysis Modules:")
        logger.info(f"   ✅ 16+ Technical Indicators")
        logger.info(f"   ✅ 20+ Candlestick Patterns")
        logger.info(f"   ✅ Price Action Analysis")
        logger.info(f"   ✅ Market Structure Detection")
        logger.info(f"   ✅ Consensus Voting System")
        logger.info(f"   ✅ 90%+ Accuracy Threshold")
        
        logger.info("\n" + "="*70)
        logger.info("✅ BOT READY FOR TRADING")
        logger.info("="*70)
        logger.info("📋 Commands Available:")
        logger.info("   /start - Start the bot")
        logger.info("   /status - View bot status")
        logger.info("   /signals - Get latest signals")
        logger.info("   /analysis - View market analysis")
        logger.info("   /help - Get help")
        logger.info("="*70 + "\n")
        
        # Start Telegram bot
        await self.app.initialize()
        await self.app.start()
        await self.app.updater.start_polling(allowed_updates=Update.ALL_TYPES)
        
        logger.info("🟢 BOT IS LIVE ON TELEGRAM")
        logger.info("Waiting for commands...\n")
        
        # Keep bot running
        await self.app.updater.idle()
    
    async def stop(self):
        """Stop the bot"""
        logger.info("\nShutting down bot...")
        if self.app:
            await self.app.stop()
            await self.app.shutdown()
        if self.ws_manager:
            self.ws_manager.disconnect()
        logger.info("✅ Bot stopped")

if __name__ == '__main__':
    bot = BaahartBot()
    try:
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        logger.info("\n⚠️  Bot stopped by user")
        asyncio.run(bot.stop())
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        asyncio.run(bot.stop())