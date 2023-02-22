import re
import pyperclip as pc

global Forgot_pass
global Help
global Pass

global uid, count
Users = {"1": "2"}
pass_list = {"Amazon": "playMode3122", "Axis": "BandiC00p800", "Twitter": "WeeTarded4ever"}
new_list = []

def password():
    global Pass, uid
    Users[uid] = Pass
    # print(Users)
    log_in()


def home1():
    while True:
        select = input("DO YOU WISH TO VIEW THE SAVED ACCOUNTS OR ADD A NEW ACCOUNT? (view/add/exit)")
        if select.lower() == "view":
            pass_manager()
        elif select.lower() == "exit":
            exit()
        elif select.lower() == "add":
            acc = input("ENTER THE ACCOUNT: ")
            new_list.append(acc)
            acc_pass = input("\nENTER THE PASSWORD: ")
            pass_list[acc] = acc_pass
            home1()

def pass_manager():
    global count
    cnt = []
    count = 1
    for x in pass_list.keys():
        print(count, ':', x)
        cnt.append(count)
        count += 1
    sel = int(input("ENTER YOUR CHOICE: "))
    if sel == 1:
        pc.copy(pass_list["Amazon"])
    elif sel == 2:
        pc.copy(pass_list["Axis"])
    elif sel == 3:
        pc.copy(pass_list["Twitter"])
    elif sel in cnt:
        pc.copy(pass_list[new_list[sel-4]])
    print("\nPASSWORD SUCCESSFULLY COPIED (USE CTR+V TO PASTE THE PASSWORD IN THE RESPECTIVE FIELD\n\n)")


# def home():
#
#
#     select = int(input("DO YOU WANT TO ADD NEW OR SELECT THE PASSWORD FOR THE FOLLOWING ACCOUNT: "))
#     if select == 1:
#         x = pc.copy(pass_list[2])
#         print("\nPASSWORD SUCCESSFULLY COPIED (USE CTR+V TO PASTE THE PASSWORD IN THE RESPECTIVE FIELD)")
#     elif select == 2:
#         pc.copy(pass_list["Axis"])
#         print("\nPASSWORD SUCCESSFULLY COPIED (USE CTR+V TO PASTE THE PASSWORD IN THE RESPECTIVE FIELD)")
#     elif select == 3:
#         pc.copy(pass_list["Twitter"])
#         print("\nPASSWORD SUCCESSFULLY COPIED (USE CTR+V TO PASTE THE PASSWORD IN THE RESPECTIVE FIELD)")
#     elif select == "add":
#
#         home()
#
#

def log_in():
    try_attempt = 3
    print("LOG IN".upper().center(170))
    while True:
        loguid = input("\nENTER YOUR USERNAME: ")
        logPass = input("ENTER YOUR PASSWORD: ")
        if loguid not in Users.keys() or logPass not in Users.values():
            print("\nWRONG USERNAME OR PASSWORD\n")
            try_attempt -= 1
            if try_attempt == 0:
                print("\nMAXIMUM ATTEMPT USED")
                sign_up()
                break
            print(try_attempt, "more attempts remaining\n")
        else:
            print("password manager".upper().center(170))
            print("welcome", loguid)
            home1()
            break


def sign_up():
    global uid
    print('\n')
    print("Welcome to Pass Manager".upper().center(170))
    x = input("DO YOU ALREADY HAVE AN ACCOUNT?\n")
    if x.lower() == "no":
        print("please enter your credentials")
        while True:
            uid = input("ENTER YOUR USERNAME: ")
            if uid not in Users:
                print("valid")
                break
            else:
                print(uid, " already exists, please try a different one")
        password_check()
        return uid
    elif x.upper() == 'yes':
        print("welcome back!")
        log_in()
    else:
        sign_up()


def password_check():
    global Pass
    while True:
        pw = input("ENTER A STRONG PASSWORD: ")
        if not 15 >= len(pw) >= 7:
            flag = -1
            break
        elif not re.search("[a-z]", pw, re.I):
            flag = -1
            break
        # elif not re.search("[A-Z]", pw):
        #     flag = -1
        #     break
        elif not re.search("[0-9]", pw):
            flag = -1
            break
        elif not re.search("[_@$!#%^&*]", pw):
            flag = -1
            break
        else:
            flag = 0
            print("Valid Password")
            Pass = input("RE-ENTER THE PASSWORD: ")
            if Pass == pw:
                password()
            else:
                print("THE PASSWORD DOESN'T MATCH! TRY AGAIN")
                password_check()
            break
    if flag == -1:
        print("Not a Valid Password"
              "\nTHE PASSWORD MUST CONTAIN: "
              "\n* PASSWORD LENGTH OF (7-15)"
              "\n* A LOWER CASE CHARACTER"
              "\n* AN UPPERCASE CHARACTER"
              "\n* A NUMBER"
              "\n* A SPECIAL CASE CHARACTER")
        password_check()
    return Pass


sign_up()
