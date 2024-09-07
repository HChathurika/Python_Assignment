from fontTools.misc.cython import returns
def it_is_prime(number):
    if number <=1:

     return False

    for i in range(2, number):
        if number % i ==0:
         return False

    return True

try:

    num = int(input("Enter an integer number: "))

    if it_is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

except ValueError:

    print("Please enter an integer")



