
# Enter the cabin class of a cruse ship
cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()


if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class entered. Please choose from LUX, A, B, or C.")
