from abc import ABC, abstractmethod
from Simulator import Simulator
from Renderer import Renderer
from Sorter import Sorter
import tkinter as tk
import random

import os
def clear_terminal():
    os.system('cls')

class UI(ABC):


    def __init__(self):
        self._simulator: Simulator = Simulator()


    @property
    def simulator(self):
        return self._simulator


    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError


class GUI(UI):

    def __init__(self) -> None:
        super().__init__()
        self._renderer: Renderer = Renderer()

    def run_menu2(self):

        menu2 = tk.Frame(self.root)

        tbutton = tk.Button(menu2, text="Change2", command=self.change_page)



        tbutton.pack(side=tk.TOP)

        menu2.pack()


    def run_menu1(self):
        frame = tk.Frame(self.root)

        startButton = tk.Button(frame, text="Change", command=self.change_page)
        quitButton = tk.Button(frame, text="QUIT", command=quit)



        startButton.pack(side=tk.TOP)
        quitButton.pack(side=tk.BOTTOM)
        frame.pack()

    def change_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.pagenum==0:
            self.run_menu1()
            self.pagenum = 1
        elif self.pagenum==1:
            self.run_menu2()
            self.pagenum = 0



    def run(self) -> None:

        self.pagenum = 0
        self.root = tk.Tk()
        self.root.geometry("500x200")

        self.run_menu1()


        self.root.mainloop()

    @property
    def renderer(self):
        return self._renderer


class Terminal(UI):
    MENULEN = 4
    SMALL_SORT = 8
    MED_SORT = 15
    LARGE_SORT = 25
    def __init__(self) -> None:
        super().__init__()

        self._sorter: Sorter = Sorter()


    def run(self) -> None:
        while True:
            self.display_menu()
            str_choice: str = input(f"Enter choice (1-{Terminal.MENULEN}): ")
            try:
                int_choice: int = int(str_choice)
            except ValueError:
                print("Invalid input for choice, please try again")
                continue #Back to start of loop

            if int_choice < 1 or int_choice > self.MENULEN:
                print("Choice is out of range, please try again")
                continue

            #Valid choice so process here

            if int_choice==1:
                self._sorter.process_sorting_choice()
            elif int_choice==2:
                self._simulator.process_grid_choice()
            elif int_choice==3:
                pass
            elif int_choice==4:
                exit(1)

    def display_menu(self):

        print("-"*20,"Main Menu", "-"*20)
        print("1. View sorting algorithm options")
        print("2. View grid algorithm options")
        print("3. View maze generation and searching options")
        print("4. Quit")
        print("-"*40)

if __name__ == "__main__":

    g = GUI()
    g.run()