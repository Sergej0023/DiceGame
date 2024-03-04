from Player import Player
from Turn import Turn
from Computer import Computer
import Difficulty


class Game:
    def __init__(self, username, playerTwoName, difficultyLevel, mode): 
        self.playerOne = Player(str(username))  # enforces string on player name
        self.maxScore = 25

        #both are "playerTwo". When using which specific methods in DiceRoll with do check with: 
        # if type(self.playerTwo) is Player: 
        if mode == "p":
            self.playerTwo = Player(str(playerTwoName))
        elif mode == "c":
            self.playerTwo = Computer(difficultyLevel) #Need to set this up again. Did something wrong with my enums

    
    def pig(self):
        while True:
            print("PLAYER 1!!!!!!!")
            P1 = Turn.playerTurn(self.playerOne, self.maxScore)
            if P1 == True:
                print(f"{self.playerOne.username} wins")  # Testing purposes
                break
            
            print("PLAYER 2!!!!!!!!!")
            P2 = Turn.playerTurn(self.playerTwo, self.maxScore)
            if P2 == True:
                print(f"{self.playerTwo.username} wins")  # testing purposes
                break

