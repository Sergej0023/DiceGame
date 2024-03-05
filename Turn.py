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
            dice = Turn.playTurn()
            player.updateRunningScore(dice + player.runningScore)
            

            if dice == 0:
                print(f"\n{player.username} rolled a {dice+1}")
                print(f"{player.username} Current turn's score: 0")
            else:
                print(f"\n{player.username} rolled a {dice}")
                print(f"Current turn's score: {player.runningScore}")
            print(f"Total score is: {player.score}")

            if Turn.skipTurn(dice):
                #Implement print for skip turn
                if type(player) is Computer:
                    player.updateRunningScore(0)                
                return False

            checkWin = Turn.winGame(player.runningScore + player.score, maxScore)

            if checkWin is True:
                return True  # wins the game



            if type(player) is Player:     

                anotherTurn = input("\nEnter r to roll and h to hold: ")
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
            