
#Execrcise 01
name = input("What is your name?")
print("Hello," + name + "!Nice to meet you")


8



#Execrcise 01
name = input("What is your name?")
print("Hello," + name + "!Nice to meet you")
#Exercise 02
import math
radius=float(input("What is the radius of the circle?"))
area=math.pi*radius**2
print(f"The area of the circle is for", str(radius),"is:",area)
8


#Exercise 03
lenght = float(input("What is the length of the rectangle:"))
width = float(input("What is the width of the rectangle:"))
area=lenght*width
perimeter=2*lenght+2*width
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")

#Exercise 04
num_1 = int(input("Enter first numbers: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

#Calculate sum of three numbers
sum=num_1+num_2+num_3
print("Sum of Three numbers:",sum)

#calculate product of three numbers
product=num_1*num_2*num_3
print("Product of Three numbers:",product)

#calculate average of three numbers
average=sum/3
print("Average of Three numbers:",average)

#Exercise 05
talents = float (input("Enter talents:"))
pounds = float (input("Enter pounds:"))
lots = float (input("Enter lots:"))
kg_weight = (talents*20+pounds)*32+lots*0.0133
gr_weight = 1000*(kg_weight-int(kg_weight))
print(f"The weight in modern unit:\n{int(kg_weight)}kilogram and {gr_weight:2f}grams")
#Exercise 06
import random
def generate_3_digit_code():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))
def generate_4_digit_code():
    return ''.join(str(random.randint(1, 6)) for _ in range(4))
def main():
    code_3_digit = generate_3_digit_code()
    code_4_digit = generate_4_digit_code()
    print(f"3-digit code: {code_3_digit}")
    print(f"4-digit code: {code_4_digit}")
if __name__ == "__main__":

    gender = input("Enter your gender: ")
    hemoglobin = input("Enter your  value: ")

    if gender == "feMale":

        if divisible_by_four and divisible_by_400:
            print(f"{year} is not a leap year")
        else:
            print(f"{year} is not a leap year")



name




