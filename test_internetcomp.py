# test_internetcomp.py
"""
Tests for InternetComp module.
"""

import unittest
from internetcomp import InternetComp

class TestInternetComp(unittest.TestCase):
    """Test cases for InternetComp class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InternetComp()
        self.assertIsInstance(instance, InternetComp)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InternetComp()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
