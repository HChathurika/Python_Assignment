cities = []

for i in range(5):
    city = input(f'Enter the five cities {i+1}:')
    cities.append(city)

    for city in cities:
        print(city)

print("There are five cities entered you ; ")