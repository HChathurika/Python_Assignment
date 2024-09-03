#Exercise 05
#get user inputs
print("Give mass in talents,pounds,and lots ")

talents = float (input("Enter talents:"))
pounds = float (input("Enter pounds:"))
lots = float (input("Enter lots:"))

#calculate the mass
grams_per_lot = 13.3
lots_per_pound = 32
pounds_per_talent = 20

total_lots = (talents * pounds_per_talent * lots_per_pound) + (pounds * lots_per_pound) + lots
mass = total_lots * grams_per_lot

#conver mass into kilograms and grams
kg = int(mass // 1000)
grams = mass % 1000

print(f"The weight in modern unit:")
print(f"{kg} kilogram and {round(grams, 2)}grams")

