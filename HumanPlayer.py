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
        self.cheat = "C"


    def roll_decision(self):
        while True:
            playerDecision = Displays.input_another_turn()
            if playerDecision.upper() == self.roll or playerDecision.upper() == self.hold:
                return playerDecision.upper()

            elif playerDecision.upper() == self.quit:
                return self.quit

            elif playerDecision.upper() == self.cheat:
                return self.cheat
