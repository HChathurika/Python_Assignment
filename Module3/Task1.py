# Size limit for zander in cm
Size_limit = 42

# What is the length of the zander Ask the fisher
Zander_length = float(input("Enter the zander lenth in cm: "))

# Check if the zander meets the size limit
if Zander_length >= Size_limit:
    print("The zander equal to the size limit. keep your fish.")
else:
    # Calculate how many cm the zander is below the size limit
    below_limit = Size_limit - Zander_length
    print(f"The zander is {below_limit:.2f} cm below the size limit.Release the fish back into the lake.")