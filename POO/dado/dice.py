from random import randint

class Die:
    def __init__(self):
        self.sides = 6

    def roll_dice(self):
        return randint(1, self.sides)

mi_dado = Die()

print(mi_dado.roll_dice())

