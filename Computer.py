import Difficulty

class Computer:
    def  __init__(self, difficulty):
        self.difficulty = difficulty
        self.runningScore = 0


    def rollDecision(self):
        match self.difficulty:
            case Difficulty.Difficulty.EASY.name:
                 self.decision(20) #From wikipedia, gives an 8% disadvantage
            case Difficulty.Difficulty.MEDIUM.name:
                self.decision(25) #From wikipedia, those are all 
            case Difficulty.Difficulty.HARD.name:
                self.decision(15) #To be tweaked still
            
    def decision(self, turnTotal):
        return "r" if self.runningScore < turnTotal else "h"
    
    def setDifficulty(self, difficultyLvl):
        self.difficulty = difficultyLvl
            
            
        
