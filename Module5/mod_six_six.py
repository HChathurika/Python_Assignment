import math


def pizza_sqm(diameter, price):
    radius_in_meter = diameter/100/2
    area = radius_in_meter ** 2*math.pi
    return price/area
print(pizza_sqm(30, 12.5))

print(pizza_sqm(48, 24.90))

price_pizza_1 = 12.9
size_pizza_1 = 30


print(pizza_sqm(size_pizza_1, price_pizza_1))

price_pizza_2 = 24.9
size_pizza_2 = 40


pizza_1 = (pizza_sqm(size_pizza_1, price_pizza_1))
pizza_2 = (pizza_sqm(size_pizza_2, price_pizza_2))

pizza_1 = pizza_sqm(size_pizza_1, price_pizza_1)
if pizza_1 < pizza_2:
    print('pizza_1 is better value')

else:
    print('pizza_2 is better value')

