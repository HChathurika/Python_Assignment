seasons= ("winter","spring","summer","Autumn")

month = int(input("Enter number of a month: "))
if 12<month:
    print("Please enter number between 1 and 12")
else:

    if month in (1,2,12):
        print("The season is :",seasons[0])
    elif month in(3,4,5):
        print("The season is :",seasons[1])
    elif month in (6,7,8):
     print("The season is :",seasons[2])
    else:
        print("the season is :",seasons[3])



