import matplotlib.pyplot as plt
import matplotlib
import random
from abc import ABC
from Creator import GridCreator
import numpy as np
from Searches import BFS

class Renderer(ABC):
    def __init__(self) -> None:
        pass


class SortingRenderer(Renderer):
    def __init__(self):
        
        super().__init__()


class SearchingRenderer(Renderer):
    def __init__(self):
        super().__init__()
        
        self._cell_to_col = {GridCreator.BARRIER_TILE:4, GridCreator.TILE: 0, GridCreator.ETILE:1, GridCreator.STILE: 1}
        # Start and end tiles are Grey
        # Searching are yellow
        # Searched are green
        # End points are blue
        # Obstacles are red
        GREY = '0.5'
        WHITE = '1'
        self.__col_list = [WHITE, GREY, "b", "g","r"]
        self.__frames = []
        self.__cur_grid = None
        self.__cmap = matplotlib.colors.ListedColormap(self.__col_list)
    
    
    @property
    def cur_grid(self):
        if self.__cur_grid is None:
            raise Exception("No grid found to operate on")
        return self.__cur_grid


    @cur_grid.setter
    def cur_grid(self, value):
        self.__cur_grid = value



    @property
    def frames(self):
        if not self.__frames:
            raise Exception("Not enough frames to animate")
        return self.__frames

    @frames.setter
    def frames(self, value):
        self.__frames = value


    def test_rand_gen(self, size: int = -1):

        if size == -1:
            size = len(self.__col_list)

        return np.array([[random.randint(0, len(self.__col_list)) for _ in range(size)] for _ in range(size)])

    def test_cmap(self, arr=None):

        if arr is None:
            arr = self.test_rand_gen(20)

        plt.pcolormesh(arr, cmap=self.__cmap, edgecolors="k", linewidth=0.01)
        plt.show()


    def test_update_fig(self, a, size):

        self.__im.set_array(self.test_rand_gen(size).flatten())

        return [self.__im]


    def test_2d_animation(self, size=10):

        fig = plt.figure()
        ax = plt.axes()

        data = self.test_rand_gen(size)

        self.__im = plt.pcolormesh(data, cmap=self.__cmap, edgecolors="k", linewidth=0.01)


        anim = matplotlib.animation.FuncAnimation(fig, self.test_update_fig, frames=10, interval=100, fargs = [size])

        plt.show()
    
    def gen_matplotlib_grid(self, grid, display: bool = False):
        # Should be called before any frames are generated for the text animation option
        # Eg there should be no colour on the grid
        mat_grid = [[] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid)):
                mat_grid[row].append(self._cell_to_col[self.extract_cell(grid[row][col])])

        if display:
            self.test_cmap(mat_grid)


    def extract_cell(self, string):
        SPEC_ORDER = GridCreator.TILES[:]
        SPEC_ORDER.remove(GridCreator.TILE)
        SPEC_ORDER.append(GridCreator.TILE)

        # Move 0 to end because it is a special character

        for tile in SPEC_ORDER:
            if tile in string:

                return tile



if __name__ == "__main__":
    tr = SearchingRenderer()

    tr.test_2d_animation(size=20)
