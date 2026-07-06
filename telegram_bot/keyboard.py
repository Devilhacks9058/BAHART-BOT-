#!/usr/bin/env python3
# Telegram Bot Keyboard

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    """Get main menu keyboard"""
    keyboard = [
        [KeyboardButton('/status'), KeyboardButton('/signals')],
        [KeyboardButton('/analysis'), KeyboardButton('/portfolio')],
        [KeyboardButton('/balance'), KeyboardButton('/settings')],
        [KeyboardButton('/help')]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_signal_keyboard():
    """Get signal action keyboard"""
    keyboard = [
        [InlineKeyboardButton('📈 Execute BUY', callback_data='execute_buy'),
         InlineKeyboardButton('📉 Execute SELL', callback_data='execute_sell')],
        [InlineKeyboardButton('⏭️ Skip Signal', callback_data='skip_signal'),
         InlineKeyboardButton('📊 More Details', callback_data='signal_details')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_settings_keyboard():
    """Get settings menu keyboard"""
    keyboard = [
        [InlineKeyboardButton('📊 Indicators', callback_data='settings_indicators'),
         InlineKeyboardButton('⚙️ Risk', callback_data='settings_risk')],
        [InlineKeyboardButton('🎯 Assets', callback_data='settings_assets'),
         InlineKeyboardButton('🔔 Notifications', callback_data='settings_notifications')],
        [InlineKeyboardButton('◀️ Back', callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)