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

    SMALL_SIZE = 8
    START_COL = END_COL = "grey"
    MED_SIZE = 15
    LARGE_SIZE = 30
    SIZES = [SMALL_SIZE, MED_SIZE, LARGE_SIZE]
    TILE = "0"
    STILE = "S"
    ETILE = "E"
    DRAW_PROB = 0.5

    def __init__(self) -> None:

        self._grid: List[List[str]] = []
        self._start = (0,0)
        self._end = (0,0)


    def draw_obstacle(self, top_left: Tuple[int, int], ob_size):
        row: int = top_left[0]
        col: int = top_left[1]
        for rrow in range(row, row + ob_size):
            for ccol in range(col, col + ob_size):
                self._grid[rrow][ccol] = colored("#", "red")


    def generate_grid(self, size:int = 1) -> List[List[str]]:

        # Generate a 2D array filled with zeroes

        self._grid = [[GridCreator.TILE for col in range(size)] for row in range(size)]


        self.gen_start_end()
        self.generate_all_obstacles()

        return self._grid
    def _print_grid(self) -> None:

        for row in self._grid:
            print(*row)

    def check_obstacle(self, ob_size: int) -> Tuple[bool, int, int]:

        # Generates upper left corner position of obstacle
        row = random.randint(0,len(self._grid)-ob_size-1)
        col = random.randint(0,len(self._grid) - ob_size - 1)


        can = True
        # Checks if obstacle zone is free, (including one extra square)
        for rrow in range(row-1, row+ob_size+1):
            for ccol in range(col-1, col+ob_size+1):
                if self._grid[rrow][ccol] != GridCreator.TILE:
                    can = False

        return (can, row, col)

    def generate_all_obstacles(self) -> None:


        for ob_size in range(len(self._grid)//4, 0,-1):

            tries = 0
            suc = 0
            targ = (len(self._grid)//4)-ob_size
            while True:

                can, x,y = self.check_obstacle(ob_size)
                if can:
                    shouldDraw = random.random()

                    if shouldDraw < GridCreator.DRAW_PROB:
                        self.draw_obstacle((x, y), ob_size)
                    suc += 1
                if tries > 80 or suc == targ:
                    break
                tries += 1


    def gen_point(self, xlim=0, ylim=0) -> Tuple[int, int]:
        return random.randint(xlim, len(self._grid)-xlim-1), random.randint(ylim, len(self._grid)-ylim-1)


    def dist(self, p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

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

        self._grid[sy][sx] = colored(GridCreator.STILE, GridCreator.START_COL)
        self._grid[ey][ex] = colored(GridCreator.ETILE, GridCreator.END_COL)






"""
tg = GridCreator()

tg.generate_grid(25)
tg._print_grid()"""