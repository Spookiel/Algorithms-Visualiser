import sys
from UI import GUI, Terminal





if __name__=="__main__":
    print("run with t as second argument for terminal mode")
    print("run with g as second argument for GUI mode")
    print("-"*40+"\n")
    sys_args = sys.argv

    isTerminal: bool = True


    if len(sys_args)==1:
        print("Assumed running from Pycharm, would you like terminal or GUI?")
        isTerminal = input("Enter mode? (t|g): ") == "t"
    else:
        if sys_args[1]=="t":
            isTerminal = True
        elif sys_args[1]=="g":
            isTerminal = False

    if isTerminal:
        ui = Terminal()
    else:
        ui = GUI()

    ui.run()