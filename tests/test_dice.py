import unittest
from unittest.mock import patch
from DiceGame.Dice import Dice
import random


class test_dice(unittest.TestCase):
    
    @patch('random.choice', return_value = 4)
    def test_roll_dice(self, mock_choice):
        dice = Dice()

        roll = dice.roll_dice()

        self.assertEqual(roll, 4)
       
if __name__ == '__main__':
    unittest.main()