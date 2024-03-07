import unittest
from Player import Player 

class TestPlayer(unittest.TestCase):

    def test_changeUsername(self): # Testing changing name
        player1 = Player()

        changedName = "Eleven"
        player1.changeUsername(changedName)

        self.assertEqual(player1.username, changedName)

        changedName2 = "Twelve"
        player1.changeUsername(changedName2)

        self.assertEqual(player1.username, changedName2)

    def test_cheat(self): # Testing score changing
        player2 = Player("Two")
        cheatChangedScore = 25
        player2.cheat(cheatChangedScore)

        self.assertEqual(player2.score, cheatChangedScore)

        cheatChangedScore2 = 99
        player2.cheat(cheatChangedScore2)

        self.assertEqual(player2.score, 99)

    def test_updateScore(self): # Testing updateScore
        player3 = Player("Three", 10)
        newScore = 25
        player3.updateScore(newScore)   

        self.assertEqual(player3.score, 35)  

        newScore2 = 15
        player3.updateScore(newScore2)

        self.assertEqual(player3.score, 50)

    def test_scoreReset1 (self): # testing scoreReset
        player4 = Player("Four", 99, 13)
        player4.scoreReset()

        self.assertEqual(player4.score, 0)
        self.assertEqual(player4.turns, 0)
        self.assertEqual(player4.gamesPlayed, 1)

    def test_gamesPlayed (self): # Testing gamesPlayed updating
        player5 = Player("Five")
        player5.scoreReset()

        self.assertEqual(player5.gamesPlayed, 1)

        player5.scoreReset()

        self.assertEqual(player5.gamesPlayed, 2)

    def test_gamesPlayed2 (self): # Testing scoreReset with bigger numbers
        player6 = Player("Six", 999, 999)
        player6.scoreReset()

        self.assertEqual(player6.score, 0)
        self.assertEqual(player6.turns, 0)
        self.assertEqual(player6.gamesPlayed, 1)

    def test_changeUsername2 (self): # Testing 2 name changes in a row
        player7 = Player("Seven")
        changedUsername1 = "SevenSeven"
        player7.changeUsername(changedUsername1)

        self.assertEqual(player7.username, changedUsername1)

        changedUsername2 = "SevenSevenSeven"
        player7.changeUsername(changedUsername2)

        self.assertEqual(player7.username, changedUsername2)

    def test_scoreHistory (self): # Testing if Score History list works
        player8 = Player("Eight", 100, 27)
        player8.scoreReset()
        
        self.assertEqual(player8.scoreHistory, [["Scored 100 in 27 turns"]])

    def test_scoreHistory2 (self): # Testing Score History list with more entries
        player9 = Player("Nine", 100, 36)
        player9.scoreReset()

        player9.updateScore(99)
        player9.scoreReset()

        self.assertEqual(player9.scoreHistory, [["Scored 100 in 36 turns"], ["Scored 99 in 0 turns"]])
        
if __name__ == "__main__":      
    unittest.main()