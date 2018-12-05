#Test Driven Devlopment TDD
#Unittest
import unittest
from unittest.mock import patch
import app1

class TestDiceRolling(unittest.TestCase):
    def test_dice_rolling(self):
        # with patch('builtins.input',return_value="y"):
            res = app1.roll()
            self.assertIn(res, range(1,7))
            
if __name__ == '__main__':
    unittest.main()