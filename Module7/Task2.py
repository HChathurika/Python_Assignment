names_set = set()

while True:

    name = input("Enter a name: ").strip()
    if name == "":

        break

    if name in names_set:
        print("Existing Name")

    else:
        print("New Name")
        names_set.add(name)

print("\nnames entered:")
for name in names_set:
    print(name)
