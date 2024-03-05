from Player import Player
from Turn import Turn
from Computer import Computer
import Difficulty


class Game:
    def __init__(self, playerOne, playerTwo):
        self.playerOne = playerOne  # enforces string on player name
        self.playerTwo = playerTwo
        self.maxScore = 50


    def pig(self):
        while True:
            P1 = Turn.playerTurn(self.playerOne, self.maxScore)
            if P1 == "w":
                print(f"\n{self.playerOne.username} wins!!")  # Testing purposes
                break
            elif P1 == "q":
                break

            print("\nNext Player Turn!")
            P2 = Turn.playerTurn(self.playerTwo, self.maxScore)
            if P2 == "w":
                print(f"\n{self.playerTwo.username} wins!!")  # testing purposes
                break
            elif P2 == "q":
                break
            print("\nNext Player Turn!")
