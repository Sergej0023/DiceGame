import unittest
from player import Player 

class TestPlayer(unittest.TestCase):

    def test_changeUsername(self):
        player1 = Player("One", 0, 0)

        changedName = "Eleven"
        player1.changeUsername(changedName)

        self.assertEqual(player1.username, changedName)

        changedName2 = "Twelve"
        player1.changeUsername(changedName2)

        self.assertEqual(player1.username, changedName2)

    def test_cheat(self):
        player2 = Player("Two", 0, 0)
        cheatChangedScore = 25
        player2.cheat(cheatChangedScore)

        self.assertEqual(player2.score, cheatChangedScore)

        cheatChangedScore2 = 99
        player2.cheat(cheatChangedScore2)

        self.assertEqual(player2.score, 99)

    def test_updateScore(self):
        player3 = Player("Three", 10, 0)
        newScore = 25
        player3.updateScore(newScore)   

        self.assertEqual(player3.score, 35)  

        newScore2 = 15
        player3.updateScore(newScore2)

        self.assertEqual(player3.score, 50)

    def test_scoreReset1 (self):
        player4 = Player("Four", 99, 13)
        player4.scoreReset

        self.assertEqual(player4.score, 0)
        self.assertEqual(player4.turns, 0)
        self.assertEqual(player4.gamesPlayed, 1)
        
        
if __name__ == "__main__":      
    unittest.main()