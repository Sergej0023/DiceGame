from Player import Player
from Turn import Turn
from Intelligence import Intelligence


class Game:
    def __init__(self, username, maxScore):
        self.playerOne = Player(str(username))  # enforces string on player name
        self.playerTwo = Player(str("Player 2"))
        self.maxScore = maxScore


    def pig(self):
        while True:
            P1 = self.player(self.playerOne)
            if P1 == 1:
                print(f"{self.playerOne.username} wins")
                break

            P2 = self.player(self.playerTwo)
            if P2 == 1:
                print(f"{self.playerTwo.username} wins")
                break


    def player(self, player):
        turn = Turn()

        turnScore = turn.score
        playerScore = self.playerOne.score

        while True:
            dice = Turn.playTurn()

            print(playerScore)
            print(dice)

            if Turn.skipTurn(dice):
                print("LOST ROUND!!!")
                return

            newPlayerScore = turnScore + dice
            checkWin = Turn.winGame(newPlayerScore, self.maxScore)

            if checkWin is True:
                return 1  # wins the game

            anotherTurn = Turn.anotherTurn(input("Another turn? "))  # change input from different place
            if anotherTurn is False:
                playerScore += turnScore
                return

            turnScore += dice

