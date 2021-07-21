import follow
import batman
import os

def print_header():
    os.system('cls')
    print("---------------------------------------------------------------------------------")
    print(".___                  __                     _____      .__  .__                 ")
    print("|   | ____    _______/  |______            _/ ____\____ |  | |  |   ______  _  __")
    print("|   |/    \  /  ___/\   __\__  \    ______ \   __\/  _ \|  | |  |  /  _ \ \/ \/ /")
    print("|   |   |  \ \___ \  |  |  / __ \_ /_____/  |  | (  <_> )  |_|  |_(  <_> )     / ")
    print("|___|___|  / ____  > |__| (____  /          |__|  \____/|____/____/\____/ \/\_/  ")
    print("         \/      \/            \/                                                ")
    print("---------------------------------------------------------------------------------")
    print("")

def print_menu():
    print_header()
    print("\t\t\t\t1. Follow all")
    print("\t\t\t\t2. Exit")
    print("")
    option = input("Please insert selection: ")
    return option

def print_follow():
    print_header()
    username = input("Please insert username: ")
    passw = input("Please insert password: ")
    origin_username = input("Please insert the origin username: ")
    return username, passw, origin_username


def select_option(option):
    if option.isdigit():
        if int(option) == 1:
            username, passw, origin_username = print_follow()
            follow.run(username, passw, origin_username)
        elif int(option) == 2:
            return False
        elif int(option) == 3:
            batman.get_random()
    return True

keep_going = True

while keep_going:
    option = print_menu()
    keep_going = select_option(option)
