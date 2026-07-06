import asyncio
import websocket
import json
from typing import Callable, Dict
from utils.logger import setup_logger

logger = setup_logger('WebSocketManager')

class WebSocketManager:
    """Manage WebSocket connection to Pocket Option"""
    
    def __init__(self, session_token: str, uid: str):
        self.ws = None
        self.is_connected = False
        self.message_callbacks: Dict[str, Callable] = {}
        self.session_token = session_token
        self.uid = uid
        self.ws_url = 'wss://api.poc-app.com/socket.io'
        
    def register_callback(self, event: str, callback: Callable):
        """Register callback for specific event"""
        self.message_callbacks[event] = callback
        logger.info(f"Registered callback for event: {event}")
    
    def connect(self):
        """Connect to Pocket Option WebSocket"""
        try:
            self.ws = websocket.WebSocketApp(
                self.ws_url,
                on_open=self._on_open,
                on_message=self._on_message,
                on_error=self._on_error,
                on_close=self._on_close
            )
            self.ws.run_forever()
            logger.info("WebSocket connection established")
        except Exception as e:
            logger.error(f"WebSocket connection error: {e}")
            self._reconnect()
    
    def _on_open(self, ws):
        """Handle WebSocket open"""
        self.is_connected = True
        logger.info("WebSocket opened")
        self._authenticate()
    
    def _authenticate(self):
        """Authenticate with Pocket Option"""
        auth_message = f'42["auth",{{"sessionToken":"{self.session_token}","uid":"{self.uid}","lang":"en","currentUrl":"cabinet","isChart":1}}]'
        try:
            self.ws.send(auth_message)
            logger.info("Authentication message sent")
        except Exception as e:
            logger.error(f"Authentication failed: {e}")
    
    def _on_message(self, ws, message: str):
        """Handle incoming WebSocket message"""
        try:
            if message.startswith('42'):
                data = json.loads(message[2:])
                event = data[0] if data else None
                payload = data[1] if len(data) > 1 else {}
                if event in self.message_callbacks:
                    self.message_callbacks[event](payload)
                logger.debug(f"Received event: {event}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")
    
    def _on_error(self, ws, error):
        """Handle WebSocket error"""
        logger.error(f"WebSocket error: {error}")
        self.is_connected = False
    
    def _on_close(self, ws, close_status_code, close_msg):
        """Handle WebSocket close"""
        logger.warning(f"WebSocket closed: {close_msg}")
        self.is_connected = False
    
    def send_message(self, event: str, data: Dict = None):
        """Send message through WebSocket"""
        try:
            message = f'42["{event}",{json.dumps(data or {})}]'
            self.ws.send(message)
            logger.debug(f"Sent event: {event}")
        except Exception as e:
            logger.error(f"Error sending message: {e}")
    
    def disconnect(self):
        """Disconnect WebSocket"""
        if self.ws:
            self.ws.close()
            self.is_connected = False
            logger.info("WebSocket disconnected")