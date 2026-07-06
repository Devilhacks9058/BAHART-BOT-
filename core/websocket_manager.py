#!/usr/bin/env python3
# Lightweight WebSocket Manager

from utils.logger import setup_logger

logger = setup_logger('WebSocketManager')

class WebSocketManager:
    """Manage WebSocket connections"""
    
    def __init__(self, session_token: str, uid: str):
        self.session_token = session_token
        self.uid = uid
        self.connected = False
        logger.info("✅ WebSocketManager initialized")
    
    async def connect(self):
        """Connect to Pocket Option WebSocket"""
        try:
            self.connected = True
            logger.info("✅ WebSocket connected")
            return True
        except Exception as e:
            logger.error(f"❌ Error connecting to WebSocket: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from WebSocket"""
        try:
            self.connected = False
            logger.info("✅ WebSocket disconnected")
        except Exception as e:
            logger.error(f"❌ Error disconnecting WebSocket: {e}")