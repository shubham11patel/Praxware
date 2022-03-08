
from time import sleep

No_of_Meeting = int(input("Enter the numbers of meeting : "))

Name = []
State = []
City = []
Pincode = []
Purpose = []
ID = []
for i in range(No_of_Meeting):
    name = input("Enter the Name of Preson :")
    state = input("Enter the name of your State : ")
    city = input("Enter the city name : ")
    pincode = input("Enter the Pin-code of city : ")
    purpose = input("Puropse of your meeting : ")
    id = 1 + i

    Name.append(name)
    State.append(state)
    City.append(city)
    Pincode.append(pincode)
    Purpose.append(purpose)
    ID.append(id)
    print("\n")


# Display all meeting details

class IPS_Meeting:

    def showall(self, Name, ID, State, City, Pincode, Purpose):
        for i in range(No_of_Meeting):
            print(f"Name : {Name[i]}")
            print(f"ID : {ID[i]}")
            print(f"State : {State[i]}")
            print(f"City : {City[i]}")
            print(f"Pin-code : {Pincode[i]}")
            print(f"Purpose : {Purpose[i]}")
            print("*"*30)
            print("\n")


obj = IPS_Meeting()
print(" All Meetings".center(50, "*"))
obj.showall(Name, ID, State, City, Pincode, Purpose)
print("*" * 50)
print("\n")

for i in range(No_of_Meeting):
    call = int(input("Enter the name or ID for the meeting :"))
    Meeting_Dutation = int(input("Enter the duration of meeting : "))
    if call == ID[i]:
        print(f"Name : {Name[i]}")
        print(f"ID : {ID[i]}")
        print(f"State : {State[i]}")
        print(f"City : {City[i]}")
        print(f"Pin-code : {Pincode[i]}")
        print(f"Purpose : {Purpose[i]}")
        sleep(Meeting_Dutation)
        Feedback = input("Enter your feedback : ")
        print("\n")

    else:
        print("Invalid Input")

print("\n")


class OutPut:
    def output(self):
        print("Conducted Meeting".center(50, "*"))
        for i in range(No_of_Meeting):
            print(f"Name : {Name[i]}")
            print(f"ID : {ID[i]}")
            print(f"State : {State[i]}")
            print(f"City : {City[i]}")
            print(f"Pin-code : {Pincode[i]}")
            print(f"Purpose : {Purpose[i]}")
            print(f"Feedback : {Feedback}")
            print("\n")
            print("*"*30)
        print("*" * 50)


obj = OutPut()
obj.output()
