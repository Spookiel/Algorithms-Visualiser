
from abc import ABC
from Solver import Solver
from Creator import Creator, GridCreator
from typing import List
import utils
from Searches import BFS

class Simulator(ABC):
    def __init__(self) -> None:

        self._creator = Creator()
        self._solver = Solver()
        self._bfs = BFS() # Temporary to test

    def display_grid_generate_menu(self) -> None:
        """
        Displays the current menu for grid based operations

        :return: None
        """

        print("-"*20, "Grid generation menu", "-"*20)
        print("Enter arguments space separated")
        print("-"*40)
        print("First argument: Size of grid (Case insensitive)")
        print(f"s: Small - {GridCreator.SMALL_SIZE}x{GridCreator.SMALL_SIZE}",
              f"m: Medium - {GridCreator.MED_SIZE}x{GridCreator.MED_SIZE}",
              f"l: Large - {GridCreator.LARGE_SIZE}x{GridCreator.LARGE_SIZE}")
        print("Back: return to main menu")
        print("-"*40)

    def display_grid_solve_menu(self) -> None:
        print("-"*20, "Grid searching menu", "-"*20)
        print("Enter arguments space separated")
        print("-"*40)
        print("First argument: Type of search (Case insensitive)")
        print(f"b: BFS (Floodfill")




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
            back, args = utils.run_menu(self.display_grid_generate_menu)

            if back:
                return

            if self._test_grid_gen_args(args):

                conv_args: List = self._convert_grid_gen_args(args) # Convert args to list here
                size = conv_args[0] # Update when more args are added to grid generation

                self._creator._gridCreator.generate_grid(size)
                self._creator._gridCreator._print_grid()

                break # Go to next menu

            else:

                print("Invalid arguments, returning to main menu")
                return
        while True:
            back, args = utils.run_menu(self.display_grid_solve_menu)

            #if back:
            #    return

            if self._test_grid_solve_args(args):

                self._bfs.process_search(self._creator._gridCreator._grid)
                conv_args: List = self._convert_grid_solve_args(args)
            else:

                return

            return


    def _test_grid_gen_args(self, args):
        if len(args) > len(GridCreator.GRID_GEN_ARGS):
            return False

        for ind, val in enumerate(args):
            # Checks if the argument at a certain index is among the valid ones
            if val.lower() not in GridCreator.GRID_GEN_ARGS[ind]:
                return False

        return True

    def _test_grid_solve_args(self, args):
        if len(args) > len(GridCreator.GRID_SOLVE_ARGS):
            return False

        for ind, val in enumerate(args):
            # Checks if the argument at a certain index is among the valid ones
            if val.lower() not in GridCreator.GRID_SOLVE_ARGS[ind]:
                return False

        return True

    def _test_maze_args(self, args):
        raise NotImplementedError

    def _convert_grid_gen_args(self,args):
        size_lookup = {"s":0, "m":1, "l":2}

        converted: List = [arg.lower() for arg in args]
        print(converted)
        if len(converted)==0:
            converted.append(1) # Default arg for size of grid
        elif len(converted)==1:
            converted[0] = size_lookup[converted[0]]

        return converted

    def _convert_grid_solve_args(self, args):
        return 1

if __name__ == "__main__":
    pass