import random

num_of_dice = int(input("Enter a number that How many dice you roll?: "))

total = 0

for _ in range(num_of_dice):
    roll = random.randint(1, 6)
    total += roll
print("The total is", total)
