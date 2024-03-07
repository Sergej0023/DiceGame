import Game
from Dice import Dice
from HumanPlayer import HumanPlayer
from Displays import Displays


# Class of static methods which are actions that can be taken during the turn.
# It keeps track of scores per turn, temporary score
class Turn:
    @staticmethod  # skipTurn returns True if turnScore is 0
    def skip_turn(turnScore):
        reset_points = 1
        return True if turnScore == reset_points else False


    @staticmethod  # winGame returns True if score reaches maxScore
    def win_game(score, max_score):
        return True if score >= max_score else False


    @staticmethod
    def player_turn(player, max_score):
        while True:
            dice = Dice.roll_dice()
            player.running_score += dice

            Displays.print_dice(player, dice)  # PRINT ON CONSOLE

            if Turn.skip_turn(dice):
                return Game.GameOptions.ENDTURN  # RETURNS ENUM

            Displays.print_score(player.score, player.running_score)

            if Turn.win_game(player.running_score + player.score, max_score):
                return Game.GameOptions.WIN  # RETURNS ENUM

            decision = player.roll_decision()
            if decision == player.hold:  # Checks if player selected hold
                player.score += player.running_score
                return Game.GameOptions.ENDTURN  # RETURNS ENUM

            if type(player) is HumanPlayer:
                if decision == player.quit:
                    return Game.GameOptions.QUIT  # RETURNS ENUM

                if decision == player.cheat:
                    return Game.GameOptions.CHEAT
