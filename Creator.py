from abc import ABC
from typing import List
import random
from termcolor import colored
from typing import Tuple


class Creator(ABC):
    def __init__(self) -> None:
        self._mazeCreator = MazeCreator()
        self._graphCreator = GraphCreator()
        self._gridCreator = GridCreator()


class MazeCreator():
    def __init__(self) -> None:
        pass

class GraphCreator():
    def __init__(self) -> None:
        pass

class GridCreator():

    MED_SIZE = 15
    OB_DENSITY = 5
    def __init__(self) -> None:

        self._grid: List[List[str]] = []
        self._start = (0,0)
        self._end = (0,0)

    def generate_grid(self, size:int = 1) -> None:

        # Generate a 2D array filled with zeroes

        self._grid = [["." for col in range(size)] for row in range(size)]


        self.gen_start_end()
        self.generate_all_obstacles()

    def _print_grid(self) -> None:

        for row in self._grid:
            print(*row)

    def place_obstacle(self, ob_size) -> bool:

        # Generates upper left corner position of obstacle
        row = random.randint(0,len(self._grid)-ob_size-1)
        col = random.randint(0,len(self._grid) - ob_size - 1)


        can = True
        # Checks if obstacle zone is free, (including one extra square)
        for rrow in range(row-1, row+ob_size+1):
            for ccol in range(col-1, col+ob_size+1):
                if self._grid[rrow][ccol]!=".":
                    can = False

        if can:
            for rrow in range(row, row + ob_size):
                for ccol in range(col, col + ob_size):
                    self._grid[rrow][ccol] = colored("#", "red")

        return can

    def generate_all_obstacles(self) -> None:


        for ob_size in range(len(self._grid)//4, 0,-1):

            tries = 0
            suc = 0
            targ = (len(self._grid)//4)-ob_size+GridCreator.OB_DENSITY
            while True:

                if self.place_obstacle(ob_size):
                    suc += 1
                if tries > 80 or suc == targ:
                    break
                tries += 1


    def gen_point(self, xlim=0, ylim=0) -> Tuple[int, int]:
        return random.randint(xlim, len(self._grid)-xlim-1), random.randint(ylim, len(self._grid)-ylim-1)


    def dist(self, p1, p2) -> int:
        return abs(p1[0]-p2[0])+abs(p2[0]-p2[1])

    def gen_start_end(self) -> None:

        # Ensure points are suitably separated
        while True:
            self._start, self._end = self.gen_point(), self.gen_point()

            if self.dist(self._start, self._end) > len(self._grid)//3:
                break

        #Generates and assigns start, end locations to the grid
        # Marks locations with green colour

        sy, sx = self._start
        ey, ex = self._end

        self._grid[sy][sx] = colored("s", "green")
        self._grid[ey][ex] = colored("e", "green")







tg = GridCreator()

tg.generate_grid(15)
tg._print_grid()