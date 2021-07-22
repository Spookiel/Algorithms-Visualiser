import sys
from UI import GUI, Terminal
import os

def usage():
    print("run with t as second argument for terminal mode")
    print("run with g as second argument for GUI mode")
    print("-"*40+"\n")


tlines = 0
for file in os.listdir():
    if file.endswith(".py"):
        tlines += len(open(file).readlines())
print(f"Total lines in the project: {tlines}")
print("-"*40)

if __name__ == "__main__":
    usage()

    isTerminal: bool = True
    isBad: bool = False

    if len(sys.argv) == 1:

        print("Assumed running from Pycharm, would you like terminal or GUI?")
        inMode = input("Enter mode? (t|g): ")

        if inMode not in "tg":
            isBad = True

        elif inMode == "t":
            isTerminal = True

        elif inMode == "g":
            isTerminal = False

    else:
        if sys.argv[1] == "t":
            isTerminal = True

        elif sys.argv[1] == "g":
            isTerminal = False

        else:
            isBad = True

    if not isBad:

        if isTerminal:
            ui = Terminal()

        else:
            ui = GUI()

        ui.run()
    else:
        print("Bad arguments, please try again")

