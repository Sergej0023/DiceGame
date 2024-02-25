class DiceHand:

    def __init__(self):
        self.Dice_Value = 0
        
    @staticmethod
    def addRoll (self, Dice):

        current_dice_rolls = 0
        dice_roll = Dice.rollDice
        if dice_roll > 1:
            dice_roll += current_dice_rolls