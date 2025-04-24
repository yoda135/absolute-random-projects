import os
from datetime import datetime
import time

print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗       ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝       ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░       ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░       ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗       ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝       ░░░╚═╝░░░░╚════╝░

██╗░░░██╗░█████╗░██╗░░░░░██╗░█████╗░███╗░░██╗████████╗░█████╗░░██████╗
██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔════╝
╚██╗░██╔╝███████║██║░░░░░██║███████║██╔██╗██║░░░██║░░░██║░░██║╚█████╗░
░╚████╔╝░██╔══██║██║░░░░░██║██╔══██║██║╚████║░░░██║░░░██║░░██║░╚═══██╗
░░╚██╔╝░░██║░░██║███████╗██║██║░░██║██║░╚███║░░░██║░░░╚█████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═════╝░
""")

login_name = open('user/dataname.passwd')
login_pass = open('user/password.passwd')
l_n = login_name.read()
l_p = login_pass.read()

print("===================================")
now = datetime.now()
dt_string = now.strftime(" %d/%m/%Y, %H:%M")
print(" Welcome", l_n+"!")
print(" Date & Time =", dt_string)
print("===================================")
print(" 'P' Profile")
print(" 'L' Logout")
print(" 'Q' Shutdown")
print("===================================")

while True:
    user_option = input(">> ")
    if user_option == "p":
        os.startfile(r"C:\Users\scwal\PycharmProjects\ValiantOS\profile.py")
        break
    elif user_option == "q":
        print("Shutting Down...")
        print("Goodbye :)")
        time.sleep(1.5)
        break
    elif user_option == "l":
        os.startfile(r"C:\Users\scwal\PycharmProjects\ValiantOS\login.py")
        break
    elif user_option == "t":
        os.startfile(r"C:\Users\scwal\PycharmProjects\ValiantOS\texteditor.py")
        break
    elif user_option == "open":
        os.startfile(r"C:\Users\scwal\PycharmProjects\ValiantOS\texteditor.py")
        break
    else:
        print("Unknown Entry, Please try again.")
