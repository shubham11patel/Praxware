# Print String

S = input("Enter your String :\n")

# Length of a String

print("The length of string is : ")
print(len(S))

# Slicing a String

Start = int(input(" Enter the starting point :"))
End = int(input(" Enter the ending point :"))

S_1 = slice(Start)
S_2 = slice(End)

print("\nYour string after slicing : \n", S[S_2])
print("\n")

# Removing left or right space from string

print("String after removing space from left and right :\n", S[S_2].strip())
SS_1 = S[S_2].strip()
print("\n")

# Base on output ask to make upper or lower case

New_S = (input("Do you Want your string in upper case ? \n!!Yes or No !!")).upper()
if New_S == "YES" or New_S == "Y":
    print("your string in upper case :\n", SS_1.upper())
else:
    print(SS_1)

print("\n")

New_S = (input("Do you Want your string in lower case ? \n!!Yes or No !!")).upper()
if New_S == "YES" or New_S == "Y":
    print("your string in lower case :\n", S[S_2].strip().lower())
else:
    print(SS_1)

print("\n")

# Split Function
Split = S[S_2].strip()
print("Your string after the splitting : ")
print(Split.split())
print(Split.split(","))
print("\n")

# Replacing Words

Replace = S[S_2].strip()
R_S1 = input("Enter word you want to replace : ")
R_S2 = input("Enter tne replacing word : ")
print(Replace.replace(R_S1, R_S2))
S_R = Replace.replace(R_S1, R_S2)
print("\n")

# Add String By user
while True:
    A_S = input("Do you want to Add string : ").upper()
    if A_S == "YES" or A_S == "Y":
        A_S2 = input("Enter the new String/Number : \n")
        # Concat
        F_S: str = S_R + "\t" + A_S2
        print("Your final string : ", F_S)
        break
    else:
        print(S_R)
        break

print("\n")

# Capitalize

print("Your string after using capitalize : \n", F_S.capitalize())
print("\n")

# Casefold (Same as Lower case)

print("Your string after using casefold : \n", F_S.casefold())
print("\n")

# Count the no. of times that word is use in string

S_C = input("Enter the word you want to count : \n")
print(F_S.count(S_C))
print("\n")

# End with

E_S = input("Enter the last charter or alphabet of string : \n")
print(F_S.endswith(E_S))
print("\n")

# Find (To find a word from the string)

FS = input("Enter the word you want to find from the string : \n")
print(F_S.find(FS))
print("\n")

# To see the input string is all number or not

print(F_S)
print(F_S.isalnum())
print("\n")

# To see the input string has any no. in it

print(F_S)
print(F_S.isalpha())
print("\n")

# Title

print("String after using title :\n", F_S.title())
print("\n")

# Center

print(F_S.center(15,'*'))
print("\n")


print("*" * 10, "TNX", "*" * 10)

