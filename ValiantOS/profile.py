import os
import time

print("""
██╗░░░██╗░█████╗░██╗░░░██╗██████╗       ░██████╗░██████╗░░█████╗░███████╗██╗██╗░░░░░███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║██╔══██╗      ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║██║░░░░░██╔════╝
░╚████╔╝░██║░░██║██║░░░██║██████╔╝      ██████╔╝██████╔╝██║░░██║█████╗░░██║██║░░░░░█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║██╔══██╗      ██╔═══╝░██╔══██╗██║░░██║██╔══╝░░██║██║░░░░░██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║      ██║░░░░░██║░░██║╚█████╔╝██║░░░░░██║███████╗███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝      ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚══════╝
""")
print("")
print("===================================")
login_name = open('user/dataname.passwd')
l_n = login_name.read()

print(" Your Username: " + l_n)
print("")
print(" Press 'B' to go back")
print(" Press 'E' to change your Username")
print(" Press 'P' to change your Password")
print(" Press 'D' to delete your user")
print("===================================")

while True:
    user_option = input(">> ")
    if user_option == "b":
        os.startfile(r"C:\Users\scwal\PycharmProjects\ValiantOS\home.py")
        break
    elif user_option == "q":
        print("Quitting...")
        break
    elif user_option == "e":
        print("Editing Username...")
        new_name = input("Enter New Name >> ")
        with open('user/dataname.passwd', 'w') as f:
            f.writelines(new_name)
        time.sleep(0.5)
        os.startfile(r"C:\Users\scwal\PycharmProjects\ValiantOS\profile.py")
        break
    elif user_option == "p":
        print("Editing Password...")
        new_pass = input("Enter New Password >> ")
        with open('user/password.passwd', 'w') as f:
            f.writelines(new_pass)
        time.sleep(0.5)
        os.startfile(r"C:\Users\scwal\PycharmProjects\ValiantOS\profile.py")
        break
    elif user_option == "d":
        conf = input("Are you sure you want to do this? This will delete all your data. (Y/N) >> ")

        if conf == "y":
            print("Deleting Data...")

            with open('info.data', 'w') as f:
                f.writelines("0")
            with open('password.passwd', 'w') as f:
                f.writelines("")
            with open('dataname.passwd', 'w') as f:
                f.writelines("")
            time.sleep(3)
            os.startfile('setup.py')
            break
        else:
            if conf == "n":
                print("Cancelled")
    else:
        print("Unknow Entry, Please try again.")
