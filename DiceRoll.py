from Dice import Dice


# Class of static methods which are actions that can be taken during the turn.
# It keeps track of scores per turn, temporary score
class Turn:
    def __init__(self):
        self.score = 0


    @staticmethod  # playTurn rolls dice, returns corresponding value
    def playTurn():
        diceRollOne = 1
        current_dice_rolls = 0
        dice_roll = Dice.rollDice()

        if dice_roll != diceRollOne:
            current_dice_rolls += dice_roll
        return current_dice_rolls


    @staticmethod  # endTurn is a choice taken by a player if they want to end the Turn
    def anotherTurn(choice):
        stopTurn = "Stop"
        return False if choice == stopTurn else True


    @staticmethod  # skipTurn returns True if turnScore is 0
    def skipTurn(turnScore):
        resetPoints = 0
        return True if turnScore == resetPoints else False


    @staticmethod  # winGame returns True if score reaches maxScore
    def winGame(score, maxScore):
        return True if score >= maxScore else False
