# Add interface for players
class Player:
    def __init__(self):
        self.username = None
        self.score = 0
        self.running_score = 0
        self.roll = "R"
        self.hold = "H"


    @staticmethod  # Helper method for resetGame
    def resetTurns(self, turns):
        self.turns = turns


    @staticmethod  # Helper method for resetGame
    def resetScore(self, score):
        self.score = score


    def resetGame(self):
        self.resetScore(self, 0)  # reset the scores and keep track of
        self.resetTurns(self, 0)  # games played and previous scores.


    def roll_decision(self):
        pass
