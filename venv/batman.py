import random
import time

def get(num):
    if num == 1:
        print("      _..--""````""--.._")
        print("    .'       |\/|       '.")
        print("   /    /`._ |  | _.'\    \ ")
        print("  ;    /              \    |")
        print("  |   /                \   |")
        print("  ;  / .-.          .-. \  ;")
        print("   \ |/   \.-.  .-./   \| /")
        print("    '._       \/       _.'")
        print("       ''--..____..--''")

    elif num == 2:
        print("          _____       _____")
        print("     ,-'``_.-'` \   / `'-._``'-.")
        print("   ,`   .'      |`-'|      `.   `.")
        print(" ,`    (    /\  |   |  /\    )    `.")
        print("/       `--'  `-'   `-'  `--'       \ ")
        print("|                                   |")
        print("\      .--.  ,--.   ,--.  ,--.      /")
        print(" `.   (    \/    \ /    \/    )   ,'")
        print("   `._ `--.___    V    ___.--' _,'")
        print("      `'----'`         `'----'`")

    elif num == 3:
        print("          _,     _    _     ,_")
        print("      .-'` /     \ '-' /     \ `'-.")
        print("     /    |      |     |      |    \ ")
        print("    ;      \_  _/       \_  _/      ;")
        print("   |         ``           ``         |")
        print("   |                                 |")
        print("    ;    .-.   .-.     .-.   .-.    ;")
        print("     \  (   '.'   \   /   '.'   )  /")
        print("      '-.;          V          ;.-'")
        print("          `                   `")

    elif num == 4:
        print("       _,    _   _    ,_")
        print("  .o888P     Y8o8Y     Y888o.")
        print(" d88888      88888      88888b")
        print("d888888b_  _d88888b_  _d888888b")
        print("8888888888888888888888888888888")
        print("8888888888888888888888888888888")
        print("YJGS8P\"Y888P\"Y888P\"Y888P\"Y8888P")
        print(" Y888   '8'   Y8P   '8'   888Y")
        print("  '8o          V          o8'")
        print("    `                     `")

    elif num == 5:
        print("_____________________                              _____________________")
        print("`-._:  .:'   `:::  .:\           |\__/|           /::  .:'   `:::  .:.-'")
        print("    \      :          \          |:   |          /         :       /    ")
        print("     \     ::    .     `-_______/ ::   \_______-'   .      ::   . /     ")
        print("      |  :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: :|      ")
        print("      |     ;::         ;::         ;::         ;::         ;::  |      ")
        print("      |  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:|      ")
        print("      /     :           :           :           :           :    \      ")
        print("     /______::_____     ::    .     ::    .     ::   _____._::____\     ")
        print("                   `----._:: ::'  :   :: ::'  _.----'                   ")
        print("                          `--.       ;::  .--'                          ")
        print("                              `-. .:'  .-'                              ")
        print("                                 \    /                                 ")
        print("                                  \  /                                  ")
        print("                                   \/                                   ")

def get_random():
    num = random.randint(1,5)
    get(num)
    time.sleep(1)
