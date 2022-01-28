# Login and register Page
import uuid

# REGISTRATION FORM
while True:

    print("=" * 50)

    Name = str(input("Enter Your Name : "))
    Ph_No = input("Enter Your Mobile Number : ")
    if len(Ph_No) < 10:
        print("<<<Invalid Mobile number>>>")
        break
    Email = input("Enter Your E-mail ID : ")
    if "@gmail.com" not in Email:
        print("<<<Invalid Email>>>")
        break
    Password = input("Enter Your Password : ")
    if len(Password) < 8:
        print("<<< Invalid Password >>>")
        break
    print("\n")
    print("Positions : Super Admin, Mid Admin ,Admin")
    Position = input("Enter Your Position : ")
    print("=" * 50)

    Dec = input("Do you want to fill your form again ? \n!! YES OR NO !! : ")
    if Dec == "NO" or Dec == "no":
        break
print("=" * 50)
print('Your Registration is Successful')
Id = uuid.uuid1()
print("Your Unique Id : ", Id)
print("=" * 50)

# LOGIN FORM

L_Name = Name
L_Password = Password
L_Id = Id

print("ENTER YOUR LOGIN DETAILS ")

while True:

    Name = input("Enter your Name/Email id/Id : ")
    Password = input("Enter your Password : ")
    if Name == L_Name or Email or L_Id:
        if Password == L_Password:
            print("YOU ARE LOGGED IN")

            while True:
                Department = input("Enter Your Department : ")

                print("-" * 50)
                print("Enter Student Name")
                print("-" * 50)

                Student_1 = (input("Enter student_1 Name : ")).upper()
                Student_2 = (input("Enter student_2 Name : ")).upper()
                Student_3 = (input("Enter student_3 Name : ")).upper()
                Student_4 = (input("Enter student_4 Name : ")).upper()
                Student_5 = (input("Enter student_5 Name : ")).upper()

                print("-" * 50)
                print("Enter Fees of Student")
                print("-" * 50)

                student_1_fee = input(f"Enter {Student_1}'s Fee  : ")
                student_2_fee = input(f"Enter {Student_2}'s Fee  : ")
                student_3_fee = input(f"Enter {Student_3}'s Fee  : ")
                student_4_fee = input(f"Enter {Student_4}'s Fee  : ")
                student_5_fee = input(f"Enter {Student_5}'s Fee  : ")
                print("%" * 50)

                if Department == Position:
                    print("Press 1 to show Student details")
                    print("Press 2 to show Admin details")
                    a = int(input("Enter Number : "))
                    print("%" * 50)

                    if a == 1:
                        print("=" * 50)
                        print("=" * 15, "NAME", "\t\tFEEs", "=" * 15)
                        print("_" * 50)
                        print("=" * 15, f"{Student_1}", f"----{student_1_fee}", "=" * 15)
                        print("-" * 50)
                        print("=" * 15, f"{Student_2}", f"----{student_2_fee}", "=" * 15)
                        print("-" * 50)
                        print("=" * 15, f"{Student_3}", f"----{student_3_fee}", "=" * 15)
                        print("-" * 50)
                        print("=" * 15, f"{Student_4}", f"----{student_4_fee}", "=" * 15)
                        print("-" * 50)
                        print("=" * 15, f"{Student_5}", f"----{student_5_fee}", "=" * 15)
                        print("-" * 50)
                        break

                    elif a == 2:
                        Password = Password
                        Encrypted_Password = ""
                        for i in Password:
                            aes_i = ord(i)
                            enc_i = aes_i + 5
                            pas_enc = chr(enc_i)
                            Encrypted_Password += pas_enc
                        print("=" * 50)
                        print("<" * 15, "ADMIN DETAIL", ">" * 15)
                        print("-" * 50)
                        print(" " * 15, f"{L_Name}", " " * 15)
                        print("-" * 50)
                        print(" " * 15, f"{Ph_No}", " " * 15)
                        print("-" * 50)
                        print(" " * 15, f"{Email}", " " * 15)
                        print("-" * 50)
                        print(" " * 15, f"{Id}", " " * 15)
                        print("-" * 50)
                        print(" " * 15, f"{(Position).upper()}", " " * 15)
                        print("-" * 50)
                        print(" " * 15, "*" * len(Password), " " * 15)
                        print("=" * 50)

                        a = (input("Do you want to show password : ")).upper()
                        if a == "YES" or a == "Y":
                            print(f"This is Encrypted Password : {Encrypted_Password} ")
                            print("\n")
                            print("To show the real password enter 'YES' : ")
                            answer = (input("Enter 'YES' or 'NO' : ")).upper()

                            if answer == "YES" or answer == "Y":
                                Decrypted_Password = ""
                                for i in Encrypted_Password:
                                    de_i = ord(i)
                                    dec_i = de_i - 5
                                    pass_dec = chr(dec_i)
                                    Decrypted_Password += pass_dec
                                    print(f"Your real password is : {Decrypted_Password} ")
                                    break
                        break
                else:
                    print("!!<< You are not in this Department >>!!")
                    break

        else:
            print("!!<< Wrong Password >>!!")
            break

    else:
        print("!!<< Invalid Username or Password >>!!")
        break
