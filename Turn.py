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

    @staticmethod  # skipTurn returns True if turnScore is 0
    def skipTurn(turnScore):
        resetPoints = 0
        return True if turnScore == resetPoints else False


    @staticmethod  # winGame returns True if score reaches maxScore
    def winGame(score, maxScore):
        return True if score >= maxScore else False


    @staticmethod
    def playerTurn(player, maxScore):

        while True:
            print("NEXT TURN \n")
            dice = Turn.playTurn()
            player.updateRunningScore(dice + player.runningScore)
            

            if dice == 0:
                print(f"{player.username} rolled a {dice+1}")
                print(f"{player.username} RunningScore: 0")
            else:
                print(f"{player.username} rolled a {dice}")
                print(f"{player.username} runningScore: {player.runningScore}")
            print(player.score)

            if Turn.skipTurn(dice):
                #Implement print for skip turn
                if type(player) is Computer:
                    player.updateRunningScore(0)                
                return False

            #newPlayerScore = player.runningScore + dice
            checkWin = Turn.winGame(player.runningScore + player.score, maxScore)

            if checkWin is True:
                return True  # wins the game

            #player.runningScore += dice



            if type(player) is Player:     

                anotherTurn = input("Another turn? ")
                if anotherTurn != "r":
                    player.updateScore(player.runningScore)
                    player.updateRunningScore(0)
                    return False
            
            elif type(player) is Computer:
                anotherTurn = player.rollDecision()

                if anotherTurn != "r":
                    player.updateScore(player.runningScore)
                    player.updateRunningScore(0)
                    return False
            