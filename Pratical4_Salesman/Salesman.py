# Salesman Application

from datetime import date

Name = str(input('Name of Salesman :'))
ID = int(input('ID of Salesman :'))
Route = 'Kathlal to Ahmedabad'
Joining_Date = '2020-12-01'
Current_Date = date.today()

Salary = int(input('Enter Salary :'))
Total_Sale = int(input('Total No. of Sale :'))
Commission_rate = int(input('Commission Rate :'))

Commission = (Total_Sale*Commission_rate/100)
Total_Salary = int(Salary+Commission)

print('\t===================================\n\t\t\t\tReport\t\n\t==================================')
print('\t\tName of Salesman            :', Name)
print('\t\tSalesman ID                 :', ID)
print('\t\tJoining Date                :', Joining_Date)
print('\t\tCurrent Date                :', Current_Date)
print('\t===================================\n\t\t\t\tSalary\t\n\t==================================')
print('\t\tSalary                        :', Salary)
print('\t===================================\n\t\t\t\tCommission\t\n\t==================================')
print('\t\tCommission                    :', Commission)
print('\t===================================\n\t\t\t\tTotal Salary\t\n\t==================================')
print('\t\tTotal Salary                  :', Total_Salary)
print('\t===================================')
