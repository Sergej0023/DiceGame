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


    @staticmethod
    def playerTurn(player, maxScore):
        turn = Turn()

        turnScore = turn.score
        playerScore = player.score

        while True:
            dice = Turn.playTurn()

            print(playerScore)
            print(dice)

            if Turn.skipTurn(dice):
                print("LOST ROUND!!!")  # put this somewhere else
                return

            newPlayerScore = turnScore + dice
            checkWin = Turn.winGame(newPlayerScore, maxScore)

            if checkWin is True:
                return 1  # wins the game

            turnScore += dice

            anotherTurn = Turn.anotherTurn(input("Another turn? "))  # change input from different place
            if anotherTurn is False:
                player.updateScore(turnScore)
                return

