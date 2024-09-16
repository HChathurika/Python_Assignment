airport_data  = {}
def add_airport():
     icao_code = input("Enter the ICAO code ").strip().upper()
     if icao-code in airport_data:
         print("This ICAO code exist.Enter the different code.")
     else:
         name = input("Enter the name of the airport:").strip()
         airport_data[icao_code] = name
         print(f"Airport '{name} with ICAO code '{icao_code}' has been added.")

def fetch_airport():
    icao_code = input("Enter ICAO code to fetch airport information:").strip().upper()
    if icao_code in airport_data:
        print(f"Airport with ICAO code '{icao_code}")
    else:
        print("No information found for this ICAO code.")


def main():
    while True:
        print("\nOptions:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            add_airport()
        elif choice == '2':
            fetch_airport()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

    if __name__ == "__main__":
        main()