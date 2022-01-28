# Tuition Management App

# Trainer 1
T_1 = input("Enter the Name of trainer 1 : ")
Id_1 = "1"
print("ID of Trainer 1 is :", Id_1)
S_T_1 = input(f"Enter the subject of {T_1} : ")
No_of_lec1 = int(input(f"Enter the number of lec in one month by {T_1} : "))
No_of_student_1 = input(f"Enter the number of student teach by {T_1} : ")
Salary_1 = 10000
IS_1 = 5000
print("\n")

# Trainer 2
T_2 = input("Enter the Name of trainer 2 : ")
Id_2 = "2"
print("ID of trainer 2 is :", Id_2)
S_T_2 = input(f"Enter the subject of {T_2} : ")
No_of_lec2 = int(input(f"Enter the number of lec in one month by {T_2} : "))
No_of_student_2 = input(f"Enter the number of student teach by {T_2} : ")
Salary_2 = 20000
IS_2 = 10000
print("\n")

# Calculate TA DA HRA  and PF for each trainer

# For trainer 1
TA_1 = int(Salary_1 * 0.1)
DA_1 = int(Salary_1 * 0.07)
HRA_1 = int(Salary_1 * 0.2)
PF_1 = int(Salary_1 * 0.18)
T_S_1 = int(Salary_1 + TA_1 + DA_1 + HRA_1 - PF_1)

# For trainer 2
TA_2 = int(Salary_2 * 0.1)
DA_2 = int(Salary_2 * 0.07)
HRA_2 = int(Salary_2 * 0.2)
PF_2 = int(Salary_2 * 0.18)
T_S_2 = int(Salary_2 + TA_2 + DA_2 + HRA_2 - PF_2)
Total_Salary_2 = T_S_2 + IS_2

# Calucate and output of system
print("\n")
while True:
    Name = input("Enter your Name/Id of a trainer : ")

    if Name == T_1 or Name == Id_1:
        if No_of_lec1 >= 12:
            Total_Salary_1 = T_S_1 + IS_1
            print("\n")
            print("*" *50)
            print("DETAILS".center(25, '*'))
            print("Id            : ", Id_1)
            print("Name          : ", T_1)
            print("Subject       : ", S_T_1)
            print("Taken Lecture : ", No_of_lec1)
            print("Teach Student : ", No_of_student_1)
            print("\n")
            print("SALARY DETAILS".center(25, '*'))
            print("\n")
            print("TA  : ", TA_1)
            print("DA  : ", DA_1)
            print("HRA : ", HRA_1)
            print("PF  : ", PF_1)
            print("Salary       : ", T_S_1)
            print("Incentive    : ", IS_1)
            print("Total Salary : ", Total_Salary_1)
            print("*" * 50)
            print("\n")

        elif No_of_lec1 < 12 :
            Total_Salary_1 = T_S_1 - 2000

            print("*" * 50)
            print("DETAILS".center(25, '*'))
            print("Id            : ", Id_1)
            print("Name          : ", T_1)
            print("Subject       : ", S_T_1)
            print("Taken Lecture : ", No_of_lec1)
            print("Teach Student : ", No_of_student_1)
            print("\n")
            print("SALARY DETAILS".center(25, '*'))
            print("\n")
            print("TA  : ", TA_1)
            print("DA  : ", DA_1)
            print("HRA : ", HRA_1)
            print("PF  : ", PF_1)
            print("Salary       : ", T_S_1)
            print("Total Salary : ", Total_Salary_1)
            print("*" * 50)

        else:
            print("!!<<< Invalid Input >>>!!")
            break

    elif Name == T_2 or Name == Id_2:
        
        if No_of_lec2 >= 16:
            Total_Salary_2 = T_S_2 + IS_2
            print("\n")
            print("DETAILS".center(25, '*'))
            print("Id            : ", Id_2)
            print("Name          : ", T_2)
            print("Subject       : ", S_T_2)
            print("Taken Lecture : ", No_of_lec2)
            print("Teach Student : ", No_of_student_2)
            print("\n")
            print("SALARY DETAILS".center(25, '*'))
            print("\n")
            print("TA  : ", TA_2)
            print("DA  : ", DA_2)
            print("HRA : ", HRA_2)
            print("PF  : ", PF_2)
            print("Salary       : ", T_S_2)
            print("Incentive    : ", IS_2)
            print("Total Salary : ", Total_Salary_2)
            print("*" * 50)
            print("\n")

        elif No_of_lec1 < 16 :
            Total_Salary_1 = T_S_2 - 2000
            print("\n")
            print("*" * 50)
            print("DETAILS".center(25, '*'))
            print("Id            : ", Id_2)
            print("Name          : ", T_2)
            print("Subject       : ", S_T_2)
            print("Taken Lecture : ", No_of_lec2)
            print("Teach Student : ", No_of_student_2)
            print("\n")
            print("SALARY DETAILS".center(25, '*'))
            print("\n")
            print("TA  : ", TA_2)
            print("DA  : ", DA_2)
            print("HRA : ", HRA_2)
            print("PF  : ", PF_2)
            print("Salary       : ", T_S_2)
            print("Total Salary : ", Total_Salary_2)
            print("*" * 50)
            print("\n")

    else:
        print("!!<<< Invalid Input >>>!!")
        break

