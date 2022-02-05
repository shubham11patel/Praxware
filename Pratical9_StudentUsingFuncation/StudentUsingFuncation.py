def student(*S):
    print("=" * 50)
    print("YOUR RESULT".center(50, "*"))
    print("COLLEGUE    : ", S[0])
    print("NAME        : ", S[1])
    print("SEMESTER    : ", S[2])
    print("ENROLLMENT NUMBER  : ", S[3])
    print("ROLL NUMBER : ", S[4])
    print("=" * 50)
    print("SUBJECTS          MARKS ")
    print("=" * 50)
    print("Python          : ", S[5])
    print("Java            : ", S[6])
    print("C               : ", S[7])
    print("=" * 50)
    print("Total Marks is  : ", Total)
    print("Percentage is   : ", percentage)
    print("=" * 50)

print("\n")
clg = input("Enter your Collegue Name : ")
Name = input("Enter your Name : ")
Semester = input("Enter your Semester : ")
Er_number = int(input("Enter your Enrollment Number : "))
Roll_number = int(input("Enter your Roll Number : "))
Python = int(input("Enter Python Marks : "))
Java = int(input("Enter Java Marks : "))
C = int(input("Enter C Marks : "))
Total = Python + Java + C
percentage = (Total / 300) * 100
student(clg, Name, Semester, Er_number, Roll_number, Python, Java, C)



