# index   0           1         2       3       4          5
#place    1           2         3       4        5         6

names = ["viivi", "Ahemed", "Pekka", "olga", "Mary", "fifth index"]
# names[ 0          1         2        3       4           5      ]
print(names)
print(names[1])
print(names[0])
print(names[4])
if len(names) > 5:
     print(names[5])
print(names[1:3])
print(names[2:])
print(names[-2])
print(names[-3])
print(names[len(names) - 1])
print(names[2])

names.append("Chathu")
print(names)
names.append("Chathu")
print(names)
names.insert(0,"Chathu")

print(names[0])
print(names)

names.remove("Chathu")
print(names)
print(names.index("olga"))
name = "Chathu"
if "Olga" in names:
    print(f"{name} (from variable) found in index {names.index('olga')}")
if "olga" in names:
    print(f"Found olga in index {names.index('olga')}")


else:




