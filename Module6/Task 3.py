def gallons_convert_to_liters(gallons):
    # 1 gallon = 3.785 liters
    return gallons*3.785

def main():
    while True:
        galloons = float(input("Enter the amount of gallons = "))
        if galloons < 0:
            print("You eneered negative value .so this will be stop.")
            break

        liters = gallons_convert_to_liters(galloons)
        print(f"{galloons} gallon is = {liters: .2f} liters.")

if __name__ == "__main__":
    main()
