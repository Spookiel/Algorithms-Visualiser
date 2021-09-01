import matplotlib.pyplot as plt
import matplotlib
import random
from abc import ABC
from Creator import GridCreator
import numpy as np
from Searches import BFS
from termcolor import colored
import re

class Renderer(ABC):
    def __init__(self) -> None:
        pass


class SortingRenderer(Renderer):
    def __init__(self):
        
        super().__init__()


class SearchingRenderer(Renderer):
    GREY = '0.5'
    WHITE = '1'
    def __init__(self):
        super().__init__()
        
        self._cell_to_col = {GridCreator.BARRIER_TILE:4, GridCreator.TILE: 0, GridCreator.ETILE:1, GridCreator.STILE: 1}
        # Start and end tiles are Grey
        # Searching are yellow
        # Searched are green
        # End points are blue
        # Obstacles are red

        self.__col_list = [SearchingRenderer.WHITE, SearchingRenderer.GREY, "b", "g","r"]
        self.__frames = []
        self.__cur_grid = None
        self.__cmap = matplotlib.colors.ListedColormap(self.__col_list)
        self.__ansi_to_col = {31: 4, 32:3, 34:2, 37: 0, 30:1}
    
    
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


    def test_update_fig(self, frame):

        np_frame = np.array(frame)

        self.__im.set_array(np_frame.flatten())

        return [self.__im]


    def test_2d_animation(self, size=10):

        fig = plt.figure()
        ax = plt.axes()
        frame_gen = (self.gen_matplotlib_grid(scene) for ind,scene in enumerate(self.frames) if ind%1==0)
        data = next(frame_gen)


        plt.yticks([])
        plt.xticks([])
        self.__im = plt.pcolormesh(data, cmap=self.__cmap, edgecolors="k", linewidth=0.000001)


        anim = matplotlib.animation.FuncAnimation(fig, func=self.test_update_fig, frames=frame_gen, interval=200, repeat=False)

        plt.show()
    
    def gen_matplotlib_grid(self, grid, display: bool = False):
        # Should be called before any frames are generated for the text animation option
        # Eg there should be no colour on the grid
        mat_grid = [[] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid)):
                mat_grid[row].append(self.__ansi_to_col[self.extract_col(grid[row][col])])

        if display:
            self.test_cmap(mat_grid)

        return mat_grid


    def extract_cell(self, string):
        SPEC_ORDER = GridCreator.TILES[:]
        SPEC_ORDER.remove(GridCreator.TILE)
        SPEC_ORDER.append(GridCreator.TILE)

        # Move 0 to end because it is a special character

        for tile in SPEC_ORDER:
            if tile in string:

                return tile

    def extract_col(self, string):
        pat = r"\[([0-9]{2})" # To get the color of the string

        got = re.findall(pat, string)
        if len(got) == 0:
            # Return the white colour
            return 37
        return int(got[0])

if __name__ == "__main__":
    tr = SearchingRenderer()
    tb = BFS()
    tc = GridCreator()
    grid = tc.generate_grid(2)
    tb.process_search(grid, display_text_steps=False)
    tr.frames = tb._frames
    #tr.gen_matplotlib_grid(tb._frames[len(tb._frames)-1], display=True)

    tr.test_2d_animation()
