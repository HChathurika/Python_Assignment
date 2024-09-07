import math
def pizza_sqm(diameter, price):
    radius_in_meters = diameter / 2/100

    area = radius_in_meters **2*math.pi
    return price/area
print(pizza_sqm(30, 12.5))
print(pizza_sqm(48, 24.9))

price_pizza_1 = 12.9
size_pizza_1 = 30

print(pizza_sqm(size_pizza_1, price_pizza_1))

price_pizza_2 = 24.9
size_pizza_2 = 40

pizza_1 = pizza_sqm(size_pizza_1, price_pizza_1)
pizza_2 = pizza_sqm(size_pizza_2, price_pizza_2)


if pizza_1<pizza_2:
    print("pizza_1 i the better one")

else:
    print("pizza_2 i the better one")

