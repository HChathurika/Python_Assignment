
import random

number_of_dice = int(input("Enter the number of dice: "))

Total = 0
for i in range(number_of_dice):
    roll = random.randint(1, 6)
    Total += roll
    print(f"Roll {i + 1}: {roll}")
    print(f"Total of dice rolledd: {Total}")
