from enum import Enum
import random

class Dice(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @staticmethod
    def rollDice():
        diceRoll = random.choice(list(Dice))
        return diceRoll
