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