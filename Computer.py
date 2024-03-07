from Player import Player
import time


class Computer(Player):
    def __init__(self, difficulty):
        super().__init__()
        self.username = "Bob the AI"
        self.difficulty = difficulty


    def roll_decision(self):
        time.sleep(1)
        match self.difficulty:
            case "1":  # Easy level
                return self.decision(20)  # From wikipedia, gives an 8% disadvantage
            case "2":  # Medium level
                return self.decision(25)  # From wikipedia, those are all
            case "3":  # Hard level
                return self.decision(15)  # To be tweaked still


    def decision(self, turnTotal):
        return self.roll if self.running_score < turnTotal else self.hold
