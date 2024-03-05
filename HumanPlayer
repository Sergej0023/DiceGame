# Add interface for players
from Player import Player


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

        self.turns = 0
        self.scoreHistory = []
        self.gamesPlayed = 0


    def changeUsername(self, username):
        self.username = username


    def cheat(self, score):
        self.score = score


    def updatePlayerStats(self):
        self.scoreHistory.append([f"Scored {self.score} in {self.turns} turns"])
        self.gamesPlayed += 1  # Call this at end of each game to
