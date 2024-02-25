import Dice

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.dice = Dice()
        self.player1_total = 0
        self.player2_total = 0