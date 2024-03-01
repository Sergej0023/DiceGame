# Add interface for players
class Player:
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.turns = 0
        self.scoreHistory = []
        self.gamesPlayed = 0


    def changeUsername(self, username):
        self.username = username


    def cheat(self, score):
        self.score = score


    def updateScore(self, newScore):
        self.score += newScore


    def scoreReset (self):
        self.scoreHistory.append((self.name, self.score))
        self.gamesPlayed += 1   # Call this at end of each game to
        self.score = 0          # reset the scores and keep track of
        self.turns = 0          # games played and previous scores.