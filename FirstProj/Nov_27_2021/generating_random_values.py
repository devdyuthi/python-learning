import random


# Build a program to roll a dice
class Dice:
    def roll(self):
        x = [1, 2, 3, 4, 5, 6]
        y = [1, 2, 3, 4, 5, 6]

        print(f"({random.choice(x)}, {random.choice(y)})")


dice1 = Dice
dice1.roll(dice1)
