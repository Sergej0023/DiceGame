from Player import Player
from Turn import Turn
from Computer import Computer
import Difficulty


class Game:
    def __init__(self, playerOne, playerTwo, computer, mode): 
        self.playerOne = playerOne # enforces string on player name
        self.maxScore = 25

        #both are "playerTwo". When using which specific methods in DiceRoll with do check with: 
        # if type(self.playerTwo) is Player: 
        if mode == "p":
            self.playerTwo = playerTwo
        elif mode == "c":
            self.playerTwo = computer

    
    def pig(self):
        while True:
            P1 = Turn.playerTurn(self.playerOne, self.maxScore)
            if P1 == "w":
                self.playerOne.updateScore(0)
                self.playerTwo.updateScore(0)
                print(f"\n{self.playerOne.username} wins!!")  # Testing purposes
                break
            elif P1 == "q":     
                self.playerOne.updateScore(0)
                self.playerTwo.updateScore(0)
                break
            
            print("\nNext Player Turn!")
            P2 = Turn.playerTurn(self.playerTwo, self.maxScore)
            if P2 == "w":
                self.playerOne.updateScore(0)
                self.playerTwo.updateScore(0)
                print(f"\n{self.playerTwo.username} wins!!")  # testing purposes
                break
            elif P2 == "q":
                self.playerOne.updateScore(0)
                self.playerTwo.updateScore(0)
                break
            print("\nNext Player Turn!")

