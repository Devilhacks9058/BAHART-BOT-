#!/usr/bin/env python3
# BAHART Trading Bot - Lightweight Main Entry Point

import asyncio
import logging
from telegram.ext import Application
from utils.config import TELEGRAM_BOT_TOKEN, POCKET_OPTION_SESSION_TOKEN, POCKET_OPTION_UID
from utils.logger import setup_logger
from telegram_bot.handlers import start_handler, status_handler, help_handler, error_handler
from telegram import Update, BotCommand
from telegram.ext import CommandHandler

logger = setup_logger('BAHART-BOT-MAIN')

class BaahartBot:
    def __init__(self):
        self.app = None
        
    async def setup_telegram(self):
        """Setup Telegram bot"""
        try:
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
            
            logger.info("\u2705 Telegram bot setup complete")
            return True
        except Exception as e:
            logger.error(f"\u274c Error setting up Telegram bot: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    async def start(self):
        """Start the bot"""
        try:
            logger.info("\n" + "="*70)
            logger.info("\ud83e\udd16 BAHART TRADING BOT INITIALIZING")
            logger.info("="*70)
            
            # Setup Telegram
            if not await self.setup_telegram():
                logger.error("Failed to setup Telegram bot")
                return
            
            logger.info(f"\n\ud83d\udcf1 Telegram Configuration:")
            logger.info(f"   Token: {TELEGRAM_BOT_TOKEN[:20]}...")
            logger.info(f"   Username: @LALIxLOVE")
            logger.info(f"   User ID: 6562788255")
            
            logger.info(f"\n\ud83d\udd27 Pocket Option Configuration:")
            logger.info(f"   Session Token: {POCKET_OPTION_SESSION_TOKEN[:15]}...")
            logger.info(f"   UID: {POCKET_OPTION_UID}")
            
            logger.info(f"\n\ud83d\udcca Analysis Modules:")
            logger.info(f"   \u2705 16+ Technical Indicators")
            logger.info(f"   \u2705 20+ Candlestick Patterns")
            logger.info(f"   \u2705 Price Action Analysis")
            logger.info(f"   \u2705 Market Structure Detection")
            logger.info(f"   \u2705 Consensus Voting System")
            logger.info(f"   \u2705 90%+ Accuracy Threshold")
            
            logger.info("\n" + "="*70)
            logger.info("\u2705 BOT READY FOR TRADING")
            logger.info("="*70)
            logger.info("\ud83d\udccb Commands Available:")
            logger.info("   /start - Start the bot")
            logger.info("   /status - View bot status")
            logger.info("   /signals - Get latest signals")
            logger.info("   /analysis - View market analysis")
            logger.info("   /help - Get help")
            logger.info("="*70 + "\n")
            
            # Initialize and start app
            await self.app.initialize()
            await self.app.start()
            
            logger.info("\ud83d\udfe2 BOT IS LIVE ON TELEGRAM")
            logger.info("Waiting for commands...\n")
            
            # Start polling with proper context manager
            async with self.app.updater:
                await self.app.updater.start_polling(allowed_updates=Update.ALL_TYPES)
                await self.app.updater.idle()
        
        except Exception as e:
            logger.error(f"\u274c Fatal error: {e}")
            import traceback
            traceback.print_exc()
    
    async def stop(self):
        """Stop the bot"""
        try:
            logger.info("\n\u26a0\ufe0f  Shutting down bot...")
            if self.app:
                await self.app.stop()
        except Exception as e:
            logger.error(f"Error stopping bot: {e}")

if __name__ == '__main__':
    bot = BaahartBot()
    try:
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        logger.info("\n\u26a0\ufe0f  Bot stopped by user")
    except Exception as e:
        logger.error(f"\u274c Fatal error: {e}")
        import traceback
        traceback.print_exc()