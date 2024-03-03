from Player import Player
from DiceRoll import Turn
from Computer import Computer
import Difficulty


class Game:
    def __init__(self, username, playerTwoName, difficultyLevel, mode): 
        self.playerOne = Player(str(username))  # enforces string on player name

        #both are "playerTwo". When using which specific methods in DiceRoll with do check with: 
        # if type(self.playerTwo) is Player: 
        if mode == "p":
            self.playerTwo = Player(str("Player 2"))
        elif mode == "c":
            self.playerTwo = Computer(Difficulty(difficultyLevel).name) 
        self.maxScore = 100


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

