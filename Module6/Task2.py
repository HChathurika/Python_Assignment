import random


def roll_dice(sides):
   return random.randint(1, sides)


def main():
    sides = int(input("Enter the number of sides on the dice: "))

    roll = 0
    while roll != sides:
        roll = roll_dice(sides)
        print(f"Rolled: {roll}")

    print(f"Max number {sides} got!")






# Run the main function
if __name__ == "__main__":
    main()