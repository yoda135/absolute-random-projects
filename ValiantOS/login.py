import os

print("""
██╗░░░██╗░█████╗░██╗░░░░░██╗░█████╗░███╗░░██╗████████╗░█████╗░░██████╗
██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔════╝
╚██╗░██╔╝███████║██║░░░░░██║███████║██╔██╗██║░░░██║░░░██║░░██║╚█████╗░
░╚████╔╝░██╔══██║██║░░░░░██║██╔══██║██║╚████║░░░██║░░░██║░░██║░╚═══██╗
░░╚██╔╝░░██║░░██║███████╗██║██║░░██║██║░╚███║░░░██║░░░╚█████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═════╝░

██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
""")
print("")
print("===================================")
print("Welcome back to ValiantOS!")
print("===================================")

login_passwd = open('user/password.passwd')
login_name = open('user/dataname.passwd')
l_p = login_passwd.read()
l_n = login_name.read()
while True:
    usn = input("Username >> ")
    log = input("Password >> ")

    if usn == l_n:
        if log == l_p:
            os.startfile(r"C:\Users\scwal\PycharmProjects\ValiantOS\home.py")
            break
        else:
            print("Incorrect Username or Password, please try again")
    else:
        print("Incorrect Username or Password, please try again")


