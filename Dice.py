import random

class Dice:

    diceValues = list(range(1, 7))
  
    @staticmethod
    def roll_dice():
        diceRoll = random.choice(list(Dice.diceValues))
        return diceRoll
