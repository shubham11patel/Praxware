
import DMartModule


number_of_items = int(input("Enter the no of Items : "))
print("\n")

Items = []
for i in range(0, number_of_items):
    list_item = input("Enter the list of items :".capitalize())
    Items.append(list_item)
print("\n")

Items_count = []
for i in range(0,number_of_items):
    item_count = int(input("Enter the count of Items : "))
    Items_count.append(item_count)
print("\n")

Items_price = []
for i in range(0,number_of_items):
    item_price = int(input("Enter the Stock Price of Items : "))
    Items_price.append(item_price)
print("\n")

Items_sell_price = []
for i in range(0,number_of_items):
    item_sell_price = int(input("Enter the Sell Price of Items : "))
    Items_sell_price.append(item_sell_price)
print("\n")

Sell_Items = []
for i in range(0,number_of_items):
    sell_count = int(input(f"Enter the count of {Items[i]} sell : "))
    Sell_Items.append(sell_count)
print("\n")

Available_items = []
for i in range(0,number_of_items):
    Available_item_ = Items_count[i] - Sell_Items[i] 
    Available_items.append(Available_item_)
print("\n")


# Salesman Info
salesman = input("Enter the Name of Salesman : ")

for i in range(0,number_of_items):
    commission = DMartModule.Commission(Items_sell_price[i],Sell_Items[i],10)



# Output
print("\n")
print("="*50)
print("\t", "D-Mart".center(25, "*"))
print("="*50)
print("\tTotal Items :", Items)
print("\tSell Items :", Sell_Items)
print("\tAvailable Items :", Available_items)
print("*"*50)
print("\tStock Price :", Items_price)
print("\tSelling price :", Items_sell_price)
print("*"*50)
print("\tSalesman Name : ", salesman)
print("\tCommission of salesman : ", commission)
print("="*50)
