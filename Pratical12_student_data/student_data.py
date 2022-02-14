# Student Result

student_data = open("Student_Database.txt", "a")

X=str(input('Collage Name :'))

a=str(input('Student Name :'))
b=int(input('Semester :'))
c=int(input('Er. No :'))
d=int(input('Roll. No :'))

s1=int(input('Subject-1 Marks outoff 100 :'))
s2=int(input('Subject-2 Marks outoff 100 :'))
s3=int(input('Subject-3 Marks outoff 100 :'))

print('\n')

# print('Collage Name\t', X)

# print('Student Name\t', 'Semester\t', 'Er. No\t\t', 'Roll. No')
# print(a,'\t\t\t', b,'\t\t', c,'\t', d,'\t')


# print('Subject-1\t', 'Subject-2\t', 'Subject-3')

# print(s1, '\t\t\t', s2, '\t\t', s3)

T=(s1+s2+s3)

# print('Total Marks outoff 300 =', T)

P=(T/300)*100

# print('Percent(%) = ', P)

student_data.write("\n")
student_data.write("\t\t")
student_data.write("-"*50)
student_data.write("\n\t\t")
student_data.write("Student Information".center(50, "*"))
student_data.write("\n\t\t")
student_data.write("-"*50)
# student_data.write("\n")
student_data.write(f"\n\t\tCollage Name : {X}")
student_data.write(f"\n\t\tStudent Name : {a}")
student_data.write(f"\n\t\tSemster : {b}")
student_data.write(f"\n\t\tER. No : {c}")
student_data.write(f"\n\t\tRoll No : {d}")
student_data.write("\n\t\t")
student_data.write("-"*50)
# student_data.write("\n")
student_data.write(f"\n\t\tSubject-1 Marks : {s1}")
student_data.write(f"\n\t\tSubject-2 Marks : {s2}")
student_data.write(f"\n\t\tSubject-3 Marks : {s3}")
student_data.write("\n\t\t")
student_data.write("-"*50)
# student_data.write("\n")
student_data.write(f"\n\t\tTotal Marks is {T} outoff 300")
student_data.write(f"\n\t\tPercent is {P}%")
student_data.write("\n\t\t")
student_data.write("-"*50)
student_data.write("\n")
student_data.close()
print("Student Database is created")