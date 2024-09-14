

def only_even(numbers):
    even_numbers = [num for num in numbers if num%2==0]
    return even_numbers

my_list =input("Enter the list of numbers: ")
numbers = list(map(int, my_list.split()))


even_list = only_even(numbers)


print("original list = ",numbers)
print("List only even numbers:",even_list)