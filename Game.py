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
            if P1 == True:
                print(f"{self.playerOne.username} wins")  # Testing purposes
                break
            
            print("Next Player Turn")
            P2 = Turn.playerTurn(self.playerTwo, self.maxScore)
            if P2 == True:
                print(f"{self.playerTwo.username} wins")  # testing purposes
                break
            print("Next Player Turn")

