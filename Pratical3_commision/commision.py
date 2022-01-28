# Salesman Application

from datetime import date
print('Shop Name : ', 'RAM')

i = input('ID')
s = str(input('Salesman Name'))


print('\n')

print('Item 1 : Laptop')
L = int(input('No. of Laptop sale'))

print('Item 2 : Mouse')
M = int(input('No. of Mouse sale'))

CL = int(50000*L*0.05)
CM = int(500*M*0.05)


print('\n')
print('\n')

print('-------------------------------------------------------')
print('\t\t\t\tRAM\t\t\t\t')
print('-------------------------------------------------------')
print('\t\t\tSalesman ID         :', i)
print('\t\t\tSalesman Name       :', s)
print('\t\t\tJoining Date        :', '2020-12-01')
print('\t\t\tCurrent Date        :', date.today())
print('\t\t\tSalary              :', '10000')
print('----------------------\n\t\tCommission\n---------------------------------')
print('\t\t\tCommission On Laptop :', CL)
print('\t\t\tCommission On Mouse  :', CM)
print('\t\t\tTotal Commission     :', int(CL+CM))
print('\t\t\tTotal Salary        :', int(10000+CM+CL))
print('-------------------------------------------------------')

