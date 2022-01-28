# NEWSPAPER DISTRIBUTOR SYSTEM

# Name of newspapers
Paper_1 = 'Divya Bhaskar'
Paper_2 = 'Sandesh'
Paper_3 = 'Economics'
Paper_4 = 'Times Of India'
Paper_5 = 'Sanj Samachar'
Paper_6 = 'Jansata'
print('\n')

# Name of delivery boys
Boy_1 = str(input('Name of Delivery Boy-1 :'))
Boy_2 = str(input('Name of Delivery Boy-2 :'))
print('\n')

# No. of newspapers
P_1 = int(input('No. of Divya Bhaskar paper :'))
P_2 = int(input('No. of Sandesh Paper       :'))
P_3 = int(input('No. of Economics Paper     :'))
P_4 = int(input('No. of Times Of India Paper:'))
P_5 = int(input('No. of Sanj Samachar Paper :'))
P_6 = int(input('No. Of Jansata Paper       :'))
print('\n')

# No. of newspaper given to Boy_1
Boy_1_Divya_Bhaskar  = int(input('No. Of Divya Bhaskar Papers given to Boy_1  :'))
Boy_1_Sandesh        = int(input('No. of Sandesh Paper given to Boy_1         :'))
Boy_1_Economics      = int(input('NO. of Economics Paper given to Boy_1       :'))
Boy_1_Times_Of_India = int(input('No. of Times of India Paper given to Boy_1  :'))
Boy_1_Sanj_Samachar  = int(input('No. of Sanj Samachar Paper given to Boy_1   :'))
Boy_1_Jansata        = int(input('No. of Jansata Paper given to Boy_1         :'))
print('\n')

# No. of newspaper given to Boy_2
Boy_2_Divya_Bhaskar  = int(input('No. Of Divya Bhaskar Papers given to Boy_2  :'))
Boy_2_Sandesh        = int(input('No. of Sandesh Paper given to Boy_2         :'))
Boy_2_Economics      = int(input('NO. of Economics Paper given to Boy_2       :'))
Boy_2_Times_Of_India = int(input('No. of Times of India Paper given to Boy_2  :'))
Boy_2_Sanj_Samachar  = int(input('No. of Sanj Samachar Paper given to Boy_2   :'))
Boy_2_Jansata        = int(input('No. of Jansata Paper given to Boy_2         :'))
print('\n')

# Total no. of newspaper Boy_1 have
Total_No_Paper_Boy_1 = int(Boy_1_Divya_Bhaskar + Boy_1_Sandesh + Boy_1_Economics + Boy_1_Times_Of_India + Boy_1_Sanj_Samachar + Boy_1_Jansata)

# Total no. of newspaper Boy_2 have
Total_No_Paper_Boy_2 = int(Boy_2_Divya_Bhaskar + Boy_2_Sandesh + Boy_2_Economics + Boy_2_Times_Of_India + Boy_2_Sanj_Samachar + Boy_2_Jansata)

print('\n')


# Commission Rate on per newspaper sale
Commission_Rate = int(input('Commission on per newspaper :'))
print('\n')

# No. of NEWSPAPER each BOY SOLD
Sold_by_Boy_1 = int(input('No. of Papers Boy-1 Sold :'))
Sold_by_Boy_2 = int(input('No. Of Papers Boy-2 Sold :'))
print('\n')

# No. of NEWSPAPER each BOY has left
Remaining_Paper_Boy_1 = int(Total_No_Paper_Boy_1 - Sold_by_Boy_1)
Remaining_Paper_Boy_2 = int(Total_No_Paper_Boy_2 - Sold_by_Boy_2)
print('\n')

# Total commission of each boy
Commission_of_Boy_1 = Sold_by_Boy_1 + Commission_Rate / 100
Commission_of_Boy_2 = Sold_by_Boy_2 + Commission_Rate / 100
print('\n')

# Total No. of NEWSPAPERS
Total_No_of_NEWSPAPERS = int(P_1+P_2+P_3+P_4+P_5+P_6)

# No. of NEWSPAPERS SOLD
Sold_Papers = int(Sold_by_Boy_1 + Sold_by_Boy_2)

# Total No. of NEWSPAPERS Remains
Remaining_papers = int(Total_No_of_NEWSPAPERS - Sold_Papers)

# Salary of each Boy
Salary_Boy_1 = int(input('Salary of Boy-1 :'))
Salary_Boy_2 = int(input('Salary of Boy-2 :'))

# Total Salary of each boy
Total_Salary_Of_Boy_1 = Salary_Boy_1 + Commission_of_Boy_1
Total_Salary_Of_Boy_2 = Salary_Boy_2 + Commission_of_Boy_2

print('\t========================================\n\t\t\t\tReport\n\t========================================')

print('\n')

print('\t========================================\n\t\t\t\tNo. of NEWSPAPER\n\t========================================')

print('\tNo. of Divya Bhaskar Paper       :', P_1)
print('\tNo. of Sandesh Paper             :', P_2)
print('\tNo. of Economics Paper           :', P_3)
print('\tNo. of Times Of India Paper      :', P_4)
print('\tNo. of Sanj Samachar Paper       :', P_5)
print('\tNo. of Jansata Paper             :', P_6)
print('\n')

print('\t========================================\n\t\t\t\tName Of Delivery Boys\n\t========================================')

print('\tName of Delivery Boy-1 :', Boy_1)
print('\tName Of Delivery Boy-2 :', Boy_2)
print('\n')

print('\t========================================\n\t\t\t\tTotal No. of NEWSPAPERS\n\t========================================')

print('\tTotal No. Of NEWSPAPERS :', Total_No_of_NEWSPAPERS)
print('\n')

print('\t========================================\n\t\t\t\t Total No. of NEWSPAPER each Boy Have\n\t========================================')

print('Total No. of NEWSPAPER with Boy_1 :', Total_No_Paper_Boy_1)
print('Total No. of NEWSPAPER with Boy_2 :', Total_No_Paper_Boy_2)
print('\n')

print('\t========================================\n\t\t\t\tNo. of NEWSPAPER Sold by BOYS\n\t========================================')

print('\tNo. Of NEWSPAPER Sold by BOY_1   :', Sold_by_Boy_1)
print('\tNo, Of NEWSPAPER Sold by BOY_2   :', Sold_by_Boy_2)
print('\n')

print('\t========================================\n\t\t\t\tTotal No. of NEWSPAPER SOLD\n\t========================================')

print('\tTotal No. of NEWSPAPER SOLD   :', Sold_Papers)
print('\n')

print('\t========================================\n\t\t\t\tNo. of NEWSPAPER REMAINS\n\t========================================')

print('\tNo. Of NEWSPAPER Remaining with BOY_1 :', Remaining_Paper_Boy_1)
print('\tNo. Of NEWSPAPER Remaining With BOY_2 :', Remaining_Paper_Boy_2)
print('\tNo. of NEWSPAPER REMAINS              :', Remaining_papers)

print('\n')

print('\t========================================\n\t\t\t\tSalary\n\t========================================')

print('\tSalary of BOY_1    :', Salary_Boy_1)
print('\tSalary Of BOY_2    :', Salary_Boy_2)
print('\n')

print('\t========================================\n\t\t\t\tCommission\n\t========================================')

print('\tCommission of BOY_1  :', Commission_of_Boy_1)
print('\tCommission of BOY_2  :', Commission_of_Boy_2)
print('\n')

print('\t========================================\n\t\t\t\tTotal Salary\n\t========================================')

print('\tTotal Salary Of BOY_1  :', Total_Salary_Of_Boy_1)
print('\tTotal Salary Of BOY_2  :', Total_Salary_Of_Boy_2)

print('\t========================================')



