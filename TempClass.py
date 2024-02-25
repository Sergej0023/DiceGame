import random


def exit():
    SystemExit(1)
test = "test"

def throwDice():        # Dice throw 1-6 random
    throw = random.randint(1, 6)
    print(throw)
    return throw


class Game:
    # Class variables
    ai = "ai"
    scorePlayer = 0
    scoreAI = 0
    winPoints = 10

    def __init__(self, username):
        self.user = username

    def play(self): # initiates the gameplay
        while True:
            self.player(self.scorePlayer, self.user)
            self.player(self.scoreAI, self.ai)
            if self.win():
                break
            elif not self.win():
                break

    def points(self, score, player): # keeps track of points?
        temp = 0

    def player(self, score, player):  # Algorithm for the gameplay, players turn do stuff
        temp = 0

        while True:
            print(f"{player}")
            dice = throwDice()
            if self.win() == 1 and player == self.user:
                print("You win")
                break
            elif self.win() == -1 and player == self.user:
                print("You lost")
                break

            if temp >= self.winPoints:
                score = temp
                break
            if dice != 1:
                again = self.choice()
                if again == "no":
                    score += temp
                    break
                else:
                    temp += dice
            else:
                print(dice)
                break

    def choice(self):   #menu choices?
        # implement Choices menu

        choice = input("enter choice")
        return choice

    def win(self):  # check if win, lose or continue playing
        if self.scoreAI == self.winPoints:
            print("You lost")
            return 1
        elif self.scorePlayer == self.winPoints:
            print("You won")
            return -1
        else:
            return 0