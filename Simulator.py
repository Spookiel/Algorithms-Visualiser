
from abc import ABC
from Solver import Solver
from Creator import Creator
from typing import List

class Simulator(ABC):
    def __init__(self) -> None:

        self._creator = Creator()
        self._solver = Solver()


    def display_grid_menu(self) -> None:
        """
        Displays the current menu for grid based operations

        :return: None
        """

    def display_maze_menu(self) -> None:
        """
        Displays the current menu for maze based operations

        :return: None
        """

    def process_maze_choice(self) -> None:
        """
        Gets user choice for maze operations and calls Creator and Solver to perform operation required

        :return: None
        """

    def process_grid_choice(self) -> None:
        """
        Gets user choice for grid operations and calls Creator / Solver to perform required operation

        :return: None
        """

        while True:

            self.display_grid_menu()

            try:
                args: List[str] = input("Enter arguments (space separated): ").split()
                if args[0].lower() == "back":
                    return
            except:
                print("Unknown error with input")
                try:
                    ans = input("would you like to return to main menu? (yY)")
                    if ans in "yY":
                        return
                except:
                    print("Error with input, returning to main menu")
                    return
                continue
            if self._test_grid_args(args): # Here

                conv_args: List = [] # Convert args to list here # Here
                s_type, size, speed = conv_args

                if s_type == "m":
                    pass
            else:

                print("Invalid arguments, returning to main menu")
                return



    def _test_grid_args(self, args):
        pass

    def _test_maze_args(self, args):
        pass