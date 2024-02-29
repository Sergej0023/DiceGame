# Add interface for players
class Player:
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.turns = 0
        self.highscore = None
        self.gamesPlayed = 0


    def changeUsername(self, username):
        self.username = username


    def cheat(self, score):
        self.score = score


    def updateScore(self, newScore):
        self.score += newScore

    def updateGamesPlayed (self, gamesPlayed):
        self.gamesPlayed += 1


