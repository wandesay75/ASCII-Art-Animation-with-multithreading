import time
import os
from os import system, name

def clear():
    os.system( 'cls' )

def welcome():

    print("\n"*4)
    print("---------------+---------------")
    print("          ___ /^^[___              _")
    print("         /|^+----+   |#___________//")
    print("       ( -+ |____|    ______-----+/")
    print("        ==_________--'            ")
    print("          ~_|___|__")
    print("")
    time.sleep(.3)
    clear()

    print("\n"*5)
    print("   *-====== ---+---------------")
    print("          ___ /^^[___              _")
    print("         /|^+----+   |#___________//")
    print("       ( -+ |____|    ______-----+/")
    print("        ==_________--'            ")
    print("          ~_|___|__")
    print("")
    time.sleep(.3)
    clear()

    print("\n"*4)
    print("---------------+   --- *-======")
    print("          ___ /^^[___              _")
    print("         /|^+----+   |#___________//")
    print("       ( -+ |____|    ______-----+/")
    print("        ==_________--'            '\'")
    print("          ~_|___|__")
    print("")
    time.sleep(.3)
    clear()

    print("\n"*3)
    print("---------------+---------------")
    print("          ___ /^^[___              _")
    print("         /|^+----+   |#___________//")
    print("       ( -+ |____|    ______-----+/")
    print("        ==_________--'            ")
    print("          ~_|___|__")
    print("")
    time.sleep(.3)
    clear()

    print("\n"*2)
    print("   *-====== ---+---------------")
    print("          ___ /^^[___              _")
    print("         /|^+----+   |#___________//")
    print("       ( -+ |____|    ______-----+/")
    print("        ==_________--'            ")
    print("          ~_|___|__")
    print("")
    time.sleep(.3)
    clear()

    print("\n"*1)
    print("---------------+   --- *-======")
    print("          ___ /^^[___              _")
    print("         /|^+----+   |#___________//")
    print("       ( -+ |____|    ______-----+/")
    print("        ==_________--'            ")
    print("          ~_|___|__")
    print("")
    time.sleep(.3)
    clear()




while True:
    welcome()
    print('\033[wandesay]')