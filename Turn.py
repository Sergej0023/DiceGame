from Dice import Dice
from Computer import Computer
from Player import Player
from Difficulty import Difficulty


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

    '''@staticmethod  # endTurn is a choice taken by a player if they want to end the Turn
    def anotherTurn(choice):
        roll = "r"
        hold = "h"
        if choice == roll:
            return True
        elif choice == hold:
            return False'''

    @staticmethod  # skipTurn returns True if turnScore is 0
    def skipTurn(turnScore):
        resetPoints = 0
        return True if turnScore == resetPoints else False


    @staticmethod  # winGame returns True if score reaches maxScore
    def winGame(score, maxScore):
        return True if score >= maxScore else False


    @staticmethod
    def playerTurn(player, maxScore):
        turn = Turn()

        turnScore = turn.score

        while True:
            dice = Turn.playTurn()
            player.updateRunningScore(dice + player.runningScore)
            

            if dice == 0:
                print(f"{player.username} rolled a {dice+1}")
            else:
                print(f"{player.username} rolled a {dice}")
            #print(f"Total score: {player.runningScore}") #Test purpose
            print(f"{player.username} runningScore: {player.runningScore}")

            if Turn.skipTurn(dice):
                #Implement print for skip turn
                if type(player) is Computer:
                    player.updateRunningScore(0)                
                return False

            newPlayerScore = turnScore + dice
            checkWin = Turn.winGame(newPlayerScore, maxScore)

            if checkWin is True:
                return True  # wins the game

            turnScore += dice



            if type(player) is Player:     
                #anotherTurn = Turn.anotherTurn(input("Another turn? "))  # change input from different place

                anotherTurn = input("Another turn? ")
                if anotherTurn != "r":
                    player.updateScore(turnScore)
                    return False
            
            elif type(player) is Computer:
                #computerDecision = player.rollDecision()
                anotherTurn = player.rollDecision()

                if anotherTurn != "r":
                    player.updateScore(player.runningScore)
                    player.updateRunningScore(0)
                    return False
            