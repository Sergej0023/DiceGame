import Displays
from Player import Player
from Turn import Turn
from Computer import Computer
import Difficulty
from HighScore import HighScore
from enum import Enum, auto


class Game:
    def __init__(self, playerOne, playerTwo):
        self.playerOne = playerOne  # enforces string on player name
        self.playerTwo = playerTwo
        self.maxScore = 50


    def pig(self):

        print("\n\nPlayer 1")
        input("Continue...")
        playing = self.decision(Turn.playerTurn(self.playerOne, self.maxScore), self.playerOne)

        if playing != GameOptions.PLAYING:
            return None

        print("\n\nPlayer 2")
        playing = self.decision(Turn.playerTurn(self.playerTwo, self.maxScore), self.playerTwo)

        if playing != GameOptions.PLAYING:
            return None

        Game.pig(self)


    def decision(self, gameOption, player):
        match gameOption:
            case GameOptions.ENDTURN:
                self.resetTurn(player)
                return GameOptions.PLAYING

            case GameOptions.WIN:
                self.save_player_HS(player)
                self.resetTurn(player)
                self.reset()
                Displays.printWin(player)

            case GameOptions.QUIT:
                self.resetTurn(player)
                self.reset()


    @staticmethod
    def resetTurn(player):
        player.updateRunningScore(0)

    def save_player_HS(player):
        HighScore.add_player_to_list(player)


    def reset(self):
        self.playerOne.resetGame()
        self.playerTwo.resetGame()


class GameOptions(Enum):
    WIN = auto()
    QUIT = auto()
    ENDTURN = auto()
    PLAYING = auto()


# P1 = Turn.playerTurn(self.playerOne, self.maxScore)
# if P1 == "w":
#     print(f"\n{self.playerOne.username} wins!!")
# Testing purposes
#     break
# elif P1 == "q":
#     break  #
# print("\nNext Player Turn!")
# P2 = Turn.playerTurn(self.playerTwo, self.maxScore)
# if P2 == "w":
#     print(f"\n{self.playerTwo.username} wins!!")
# testing purposes
#     break
# elif P2 == "q":
#     break
# print("\nNext Player Turn!")

"""
OLD 

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

"""
