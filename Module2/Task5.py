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
