import Dice


class Player:
    def __init__(self, username):
        self.username = username
        self.score = 0

    def changeUsername(self, username):
        self.username = username


    def throwDice(self):
        dice = Dice.rollDice()
        print(dice)
        if dice != 1:
            self.score += dice
