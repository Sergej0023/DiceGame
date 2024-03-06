# Add interface for players
from Player import Player
from Displays import Displays


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

        self.turns = 0
        self.scoreHistory = []
        self.gamesPlayed = 0
        self.quit = "Q"


    def changeUsername(self, username):
        self.username = username


    def cheat(self, score):
        self.score = score


    def updatePlayerStats(self):
        self.scoreHistory.append([f"Scored {self.score} in {self.turns} turns"])
        self.gamesPlayed += 1  # Call this at end of each game to


    def anotherTurn(self):
        while True:
            playerDecision = Displays.inputAnotherTurn()
            if playerDecision.upper() == self.roll or playerDecision.upper() == self.hold:
                return playerDecision.upper()
            elif playerDecision.upper() == self.quit:
                return self.quit
