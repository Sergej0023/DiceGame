import unittest
import Turn
import Dice
import HumanPlayer
import Displays

class test_turn(unittest.TestCase):

    def test_skip_turn(self):

        turnScore1 = 1
        result_1 = Turn.skip_turn(turnScore1)
        self.assertTrue(result_1)

        turnScore2 = 2
        result_2 = Turn.skip_turn(turnScore2)
        self.assertFalse(result_2)


        










if __name__ == '__main__':
    unittest.main()