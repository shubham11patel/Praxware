
from time import sleep

# import os
# os.chdir("Project/Ads")
# Ads_data = open("Ads_Details.txt", "w")

# About Product (Name, Details, Price, Quantity)
No_of_Ads = int(input("Enter the no of ads :"))

Title = []
for i in range(0, No_of_Ads):
    Product_Name = input("Enter the Name of Product : ")
    Title.append(Product_Name)
print("\n")

Details = []
for i in range(0, No_of_Ads):
    Product_Details = input("Enter the Details of Product : ")
    Details.append(Product_Details)
print("\n")

Price = []
for i in range(0, No_of_Ads):
    Product_Price = input("Enter Price of Product : ")
    Price.append(Product_Price)
print("\n")

Quantity = []
for i in range(0, No_of_Ads):
    Quantity_of_Product = input("Enter the Quantity of Product : ")
    Quantity.append(Quantity_of_Product)
print("\n")

# Phases of Ads
Phase_1 = "1-4"
Phase_2 = "5-8"
Phase_3 = "9-12"
Phase_4 = "13-16"
Phase_5 = "17-20"
Phase_6 = "21-24"

# Price as per Phases

Price_1 = 500000
Price_2 = 500000
Price_3 = 500000
Price_4 = 500000
Price_5 = 500000
Price_6 = 1000000

print("Phase 1 to 5 are normal phase and Phase 6 is Prime Phase")


def Show(Title, Details, Price, Quantity):
    for i in range(No_of_Ads):
        print("*" * 30)
        print(f"Name : {Title[i]}")
        print(f"Details : {Details[i]}")
        print(f"Price : {Price[i]}")
        print(f"Quantity : {Quantity[i]}")
        print("*" * 30)
        sleep(5)


print("\n")
while True:
    Phase = int(input("Select the phase you want to show Ads : "))

    if Phase == 1:
        print(f"Phase 1 : {Phase_1}")
        Show(Title, Details, Price, Quantity)

    elif Phase == 2:
        print(f"Phase 2 : {Phase_2}")
        Show(Title, Details, Price, Quantity)

    elif Phase == 3:
        print(f"Phase 3 : {Phase_3}")
        Show(Title, Details, Price, Quantity)

    elif Phase == 4:
        print(f"Phase 4 : {Phase_4}")
        Show(Title, Details, Price, Quantity)

    elif Phase == 5:
        print(f"Phase 5 : {Phase_5}")
        Show(Title, Details, Price, Quantity)

    elif Phase == 6:
        print(f"Phase 6 : {Phase_6}")
        Show(Title, Details, Price, Quantity)

    else:
        print("<<<!!--Invalid Input--!!>>>")

    Phase_Change = input("Do you want to change the phase of your Ads \n YES or NO : ")
    if Phase_Change == "NO" or Phase_Change == "no":
        break
