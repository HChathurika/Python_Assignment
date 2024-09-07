import random

#dice rolling times
number_of_dice = int(input("How many chances do you take? "))

total_sum = 0

for i in range(number_of_dice):
    roll = random.randint(1, 6)  #a dice roll (values from 1 to 6)
    print(f"Dice {i + 1} rolling: {roll}")
    total_sum += roll  # Add the roll to the sum

# Print the total
print(f"\nThe total of the dice rolling: {total_sum}")