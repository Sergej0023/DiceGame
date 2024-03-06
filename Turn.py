import Game
from Dice import Dice
from Computer import Computer
from Player import Player
from Difficulty import Difficulty
from HumanPlayer import HumanPlayer
from Displays import Displays
import time


# Class of static methods which are actions that can be taken during the turn.
# It keeps track of scores per turn, temporary score
class Turn:
    def __init__(self):
        self.score = 0


    @staticmethod  # playTurn rolls dice, returns corresponding value
    def playTurn():
        diceRollOne = 1
        currentDiceRolls = 0
        diceRoll = Dice.rollDice()

        if diceRoll != diceRollOne:
            currentDiceRolls += diceRoll
        return currentDiceRolls


    @staticmethod  # skipTurn returns True if turnScore is 0
    def skipTurn(turnScore):
        resetPoints = 1
        return True if turnScore == resetPoints else False


    @staticmethod  # winGame returns True if score reaches maxScore
    def winGame(score, maxScore):
        return True if score >= maxScore else False


    @staticmethod
    def playerTurn(player, maxScore):
        while True:
            dice = Dice.rollDice()
            player.updateRunningScore(dice + player.runningScore)

            Displays.printDice(player, dice)
            # print(f"\nCurrent running {player.runningScore}") # TESTING
            # print(f"Score {player.score}")                    # TESTING
            Displays.printScore(player.score, player.runningScore)

            if Turn.skipTurn(dice):
                return Game.GameOptions.ENDTURN

            if Turn.winGame(player.runningScore + player.score, maxScore):
                return Game.GameOptions.WIN

            decision = player.anotherTurn()
            if decision == player.hold:
                player.updateScore(player.runningScore)
                return Game.GameOptions.ENDTURN

            if player == type(HumanPlayer):
                if decision == player.quit:
                    return Game.GameOptions.QUIT








    # 
    # @staticmethod  # Fix or rewrite whole thing
    # def playerTurn(player, maxScore):
    # 
    #     while True:
    #         dice = Turn.playTurn()
    #         player.updateRunningScore(dice + player.runningScore)
    # 
    #         if dice == 0:
    #             print(f"\n{player.username} rolls a {dice + 1}")
    #             print(f"{player.username} Current turn's score: 0")
    #         else:
    #             print(f"\n{player.username} rolls a {dice}")
    #             print(f"Current turn's score: {player.runningScore}")
    #         print(f"Total score is: {player.score}")
    # 
    #         if Turn.skipTurn(dice):
    #             if type(player) is Computer:
    #                 player.updateRunningScore(0)
    #             return "h"
    # 
    #         checkWin = Turn.winGame(player.runningScore + player.score, maxScore)
    # 
    #         if checkWin is True:
    #             return "w"  # wins the game
    # 
    #         if type(player) is HumanPlayer:
    # 
    #             anotherTurn = input("\nEnter r to roll and h to hold: ")
    #             if anotherTurn == "h":
    #                 player.updateScore(player.runningScore)
    #                 player.updateRunningScore(0)
    #                 return "h"
    #             elif anotherTurn == "q":  # q for quit. Here you need to exit the game. It's the only time that the player is acting
    #                 return "q"  # but if you return true it says you won. Must be changed to 3 options "r", "h", "q" or something
    # 
    #         elif type(player) is Computer:
    #             anotherTurn = player.rollDecision()
    #             time.sleep(1)
    #             if anotherTurn == "h":
    #                 print(f"{player.username} holds.")
    #                 player.updateScore(player.runningScore)
    #                 player.updateRunningScore(0)
    #                 return "h"
