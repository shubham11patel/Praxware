Employee_data = open("EmployeeData.txt", "w")

class Employee_Input:
    
    Company = input("Enter Name of Company :")
    Name = input("Enter Employee Name :")
    ID = input("Enter Employee ID :")
    Salary = int(input("Enter Salary of Employee :"))
    ta = int(input("Enter TA :"))
    da = int(input("Enter DA :"))
    hra = int(input("Enter HRA :"))
    pf = int(input("Enter PF :"))
    TA = Salary * ta / 100
    DA = Salary * da / 100
    HRA = Salary * hra / 100
    PF =  Salary * pf / 100

    Total = Salary + TA + DA + HRA 
        
class Employee_Output(Employee_Input):
    def showdata(self):
        print("\n")
        Employee_data.write("\n\t\t")
        Employee_data.write("-" * 50)
        Employee_data.write("\n\t\t")
        Employee_data.write("Salary Slip".center(50, "*"))
        Employee_data.write(f"\n\t\tCompany Name : {Employee_Input.Company}")
        Employee_data.write(f"\n\t\tEmployee Name : {Employee_Input.Name}")
        Employee_data.write(f"\n\t\tEmployee ID : {Employee_Input.ID}")
        Employee_data.write("\n\t\t")
        Employee_data.write("-" * 50)
        Employee_data.write(f"\n\t\tSalary : {Employee_Input.Salary}")
        Employee_data.write(f"\n\t\tTA : {Employee_Input.TA}")
        Employee_data.write(f"\n\t\tDA : {Employee_Input.DA}")
        Employee_data.write(f"\n\t\tHRA : {Employee_Input.HRA}")
        Employee_data.write(f"\n\t\tPF : {Employee_Input.PF}")
        Employee_data.write("\n\t\t")
        Employee_data.write("-"*50)
        Employee_data.write(f"\n\t\tTotal : {Employee_Input.Total}")
        Employee_data.write("\n")

obj = Employee_Output()
obj.showdata()

print("Employee Data Stored")
