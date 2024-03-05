from Difficulty import Difficulty
from Player import Player


class Computer(Player):
    def __init__(self, difficulty):
        super().__init__()
        self.username = "Bob the AI"
        self.difficulty = difficulty


    def rollDecision(self):
        match self.difficulty:
            case "1":  # Easy level
                return self.decision(20)  # From wikipedia, gives an 8% disadvantage
            case "2":  # Medium level
                return self.decision(25)  # From wikipedia, those are all
            case "3":  # Hard level
                return self.decision(15)  # To be tweaked still


    def decision(self, turnTotal):
        return "r" if self.runningScore < turnTotal else "h"


    def setDifficulty(self, difficultyLvl):
        values = [member.name for member in Difficulty]
        if difficultyLvl not in values:
            raise ValueError("Sorry, the difficulty level does not exist")
        else:
            self.difficulty = difficultyLvl


    def checkDifficulty(self, difficultyLvl):
        values = [member.name for member in Difficulty]
        if difficultyLvl not in values: raise ValueError("Sorry, the difficulty level does not exist")


    def updateScore(self, score):
        self.score = score


    def updateRunningScore(self, runningScore):
        self.runningScore = runningScore
