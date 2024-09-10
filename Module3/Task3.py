def check_hemoglobin():
    gender = input("Enter your gender(male/female): ").strip().lower()
    hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))

    female_range = (117, 155)
    male_range = (134, 167)

    if gender == "female":
        if hemoglobin_value < female_range[0]:
            print("Your hemoglobin value is lower than normal.")
        elif hemoglobin_value > female_range[1]:
            print("Your hemoglobin value is higher than normal.")
        else:
            print("Your hemoglobin value is within the normal range.")

    elif gender == "male":
        if hemoglobin_value < male_range[0]:
            print("Your hemoglobin value is lower than normal.")
        elif hemoglobin_value > male_range[1]:
            print("Your hemoglobin value is higher than normal.")
        else:
            print("Your hemoglobin value is within the normal range.")
    else:
        print("Invalid input.")

check_hemoglobin()