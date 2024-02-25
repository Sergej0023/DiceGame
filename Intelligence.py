class Intelligence:
    def  __init__(self,strength):
        self.strength = strength


    def rollDecision(self, turnTotal):
        match self.strength:
            case "Easy":
                return "roll" if turnTotal < 20 else "hold" #From wikipedia, gives an 8% disadvantage
            case "medium":
                return "roll" if turnTotal < 25 else "hold" #From wikipedia, those are all 
            case "hard":
                return "roll" if turnTotal < 15 else "hold" #To be tweaked still
            
            
        
