# Student Result
student_data = open("Student_Database.txt", "a")

class Student_Input:
    X=str(input('Collage Name :'))

    a=str(input('Student Name :'))
    b=int(input('Semester :'))
    c=int(input('Er. No :'))
    d=int(input('Roll. No :'))

    s1=int(input('Subject-1 Marks outoff 100 :'))
    s2=int(input('Subject-2 Marks outoff 100 :'))
    s3=int(input('Subject-3 Marks outoff 100 :'))

    T=(s1+s2+s3)

    P=(T/300)*100

class Student_output(Student_Input):
    
    def ShowStudentData(self):
 
        student_data.write("\n")
        student_data.write("\t\t")
        student_data.write("-"*50)
        student_data.write("\n\t\t")
        student_data.write("Student Information".center(50, "*"))
        student_data.write("\n\t\t")
        student_data.write("-"*50)
        
        # student_data.write("\n")
        student_data.write(f"\n\t\tCollage Name : {Student_Input.X}")
        student_data.write(f"\n\t\tStudent Name : {Student_Input.a}")
        student_data.write(f"\n\t\tSemster : {Student_Input.b}")
        student_data.write(f"\n\t\tER. No : {Student_Input.c}")
        student_data.write(f"\n\t\tRoll No : {Student_Input.d}")
        student_data.write("\n\t\t")
        student_data.write("-"*50)
        
        # student_data.write("\n")
        student_data.write(f"\n\t\tSubject-1 Marks : {Student_Input.s1}")
        student_data.write(f"\n\t\tSubject-2 Marks : {Student_Input.s2}")
        student_data.write(f"\n\t\tSubject-3 Marks : {Student_Input.s3}")
        student_data.write("\n\t\t")
        student_data.write("-"*50)
        
        # student_data.write("\n")
        student_data.write(f"\n\t\tTotal Marks is {Student_Input.T} outoff 300")
        student_data.write(f"\n\t\tPercent is {Student_Input.P}%")
        student_data.write("\n\t\t")
        student_data.write("-"*50)
        student_data.write("\n")

obj = Student_output()
obj.ShowStudentData()

print("Student Database is created")

