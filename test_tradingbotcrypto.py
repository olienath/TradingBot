# test_tradingbotcrypto.py
"""
Tests for TradingBotCrypto module.
"""

import unittest
from tradingbotcrypto import TradingBotCrypto

class TestTradingBotCrypto(unittest.TestCase):
    """Test cases for TradingBotCrypto class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TradingBotCrypto()
        self.assertIsInstance(instance, TradingBotCrypto)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TradingBotCrypto()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
