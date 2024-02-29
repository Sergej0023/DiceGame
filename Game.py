from Player import Player
from DiceRoll import Turn
from Intelligence import Intelligence


class Game:
    def __init__(self, username, maxScore):
        self.playerOne = Player(str(username))  # enforces string on player name
        self.playerTwo = Player(str("Player 2"))
        self.maxScore = maxScore


    def pig(self):
        while True:
            P1 = Turn.playerTurn(self.playerOne, self.maxScore)
            if P1 == 1:
                print(f"{self.playerOne.username} wins")  # Testing purposes
                break

            P2 = Turn.playerTurn(self.playerTwo, self.maxScore)
            if P2 == 1:
                print(f"{self.playerTwo.username} wins")  # testing purposes
                break

