class Intelligence:
    def  __init__(self,strength):
        self.strength = strength


    def rollDecision(self, turnTotal):
        match self.strength:
            case "Easy":
                 self.decision(20) #From wikipedia, gives an 8% disadvantage
            case "medium":
                self.decision(25) #From wikipedia, those are all 
            case "hard":
                self.decision(15) #To be tweaked still
            
    def decision(self, turnTotal):
        return "roll" if turnTotal < turnTotal else "hold"

            
            
        
