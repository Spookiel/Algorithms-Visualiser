from copy import deepcopy
from typing import Tuple,List
from Creator import GridCreator
from termcolor import colored
import time
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.animation
import random
import heapq as hp
from copy import deepcopy # To copy the 2D arrays with no problems
from abc import abstractmethod


class Search:

    adj4: List[List[int]] = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    adj8: List[List[int]] = adj4 + [[1, 1], [-1, 1], [1, -1], [-1, -1]]

    def __init__(self):
        self._curGrid = []
        self._pathSteps = []
        self._steps = []
        self.__finalDist = 0
        self.__checked = 0
        self._frames = []
        self.parents = {}


    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end


    @property
    def all_frames(self):
        if len(self._frames) == 0:
            print(colored("Warning, no frames to draw", "red"))
            raise Exception("Not enough frames to animate")
        if len(self._pathSteps) == 0:
            print(colored("Warning, no path steps to draw", "red"))
            raise Exception("Not enough frames to animate")
        return self._frames + self._pathSteps

    @start.setter
    def start(self, grid) -> Tuple[int, int]:
        # "s" in colored("s", "blue") -> True
        # "s" == colored("s", "blue") -> False
        for y in range(len(grid)):
            for x in range(len(grid)):
                if GridCreator.STILE in grid[y][x]:
                    self.__start = x,y
                    return x, y
        print("START POINT NOT FOUND, USING TOP LEFT CORNER")
        return 0, 0

    @end.setter
    def end(self, grid) -> Tuple[int, int]:
        # "e" in colored("e", "blue") -> True
        # "e" == colored("e", "blue") -> False
        for y in range(len(grid)):
            for x in range(len(grid)):
                if GridCreator.ETILE in grid[y][x]:
                    self.__end = x,y
                    return x, y
        print("END POINT NOT DEFINED, USING BOTTOM RIGHT CORNER")
        return len(grid) - 1, len(grid) - 1





    def checkLim(self, node: Tuple[int, int]) -> bool:
        # Checks if a node is on the grid or not
        return 0 <= node[0] < len(self._curGrid) and 0 <= node[1] < len(self._curGrid)

    def getVal(self, node: Tuple[int, int]) -> str:
        if self.checkLim(node):
            return self._curGrid[node[1]][node[0]]



    def outputSteps(self):

        for step in self._steps:
            time.sleep(0.8)
            for row in step:
                print(*row)
            print("-"*40)





    def _tracePath(self):

        self.path = [self.end]
        while self.path[-1] != self.start:
            self.path.append(self.parents[self.path[-1]])

        self.path = self.path[::-1]
        self.path.pop(0)
        self.path.pop(-1)


    def _storePath(self):

        for loc in self.path:
            self._curGrid[loc[1]][loc[0]] = colored(GridCreator.TILE, "grey")

            self._pathSteps.append(deepcopy(self._curGrid))

    def _outputPath(self):

        for step in self._pathSteps:
            print("-"*40)
            time.sleep(0.5)
            for row in step:
                print(*row)

    def process_path(self, display_text_steps: bool = True) -> None:
        self._tracePath()
        self._storePath()
        if display_text_steps:
            self._outputPath()


    def process_search(self, grid: List[List], display_text_steps: bool = True) -> None:
        self._curGrid = grid
        self._pathSteps = []
        self._steps = []

        self.search()


        if display_text_steps:
            self.outputSteps()
        self.process_path(display_text_steps)

        self.outputSearchInfo()





    @abstractmethod
    def outputSearchInfo(self):
        raise NotImplementedError()


    def show_animation(self):

        if not self._frames:
            raise Exception("No frames to draw!")



        # Function to draw a matplotlib figure similar to that of the sorting algorithms


    def adj4_gen(self, px: int, py: int) -> Tuple[int, int]:

        for dx, dy in Search.adj4:
            nx: int = px+dx
            ny: int = py+dy

            assert len(self._curGrid) > 0
            if self.checkLim((nx, ny)):
                yield nx, ny

    def adj8_gen(self, px: int, py: int) -> Tuple[int, int]:

        for dx, dy in Search.adj8:
            nx: int = px+dx
            ny: int = py+dy
            assert len(self._curGrid) > 0
            if self.checkLim((nx, ny)):
                yield nx, ny

    @staticmethod
    def manhattan(p1, p2):
        return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])



class BFS(Search):

    def __init__(self):
        super().__init__()


    def outputSearchInfo(self):
        print("-"*5, "Search information", "-"*5)
        print(f"Distance: {self.__finalDist}")
        print(f"Tiles checked: {self.__checked}")
        print(f"Board size: {len(self._curGrid)}x{len(self._curGrid)}")


    def _colourMainTiles(self, next_node: Tuple[int, int], val_at: str):
        if GridCreator.STILE not in val_at and GridCreator.ETILE not in val_at:
            # Not a start or end point so should colour green
            self._curGrid[next_node[1]][next_node[0]] = colored(GridCreator.TILE, "green")


    def updateIfDistChange(self, dist: int, last_dist: int) -> int:

        if last_dist != dist:
            self._steps.append(deepcopy(self._curGrid))
            self._frames.append(deepcopy(self._curGrid))


        return int(dist) # Careful of copying errors

    def search(self):
        # Generates a sequence of colored grids,
        # yellow is for items currently in the queue, green is for items that have already been seen
        # Function works with manhattan distance
        self.parents: dict = {}  # Stores parent node for each node so a path to start can be re-traced
        seen: set = set()
        last_dist: int = 0

        self.start: Tuple[int, int] = self._curGrid # Goes through setter function
        self.end: Tuple[int, int] = self._curGrid # Goes through setter function


        self._frames.append(deepcopy(self._curGrid))

        self._pathSteps = []
        queue = [(self.start, 0)]  # (Node, distance)
        seen.add(self.start)



        while queue:

            next_node, dist = queue.pop(0)

            val_at = self.getVal(next_node)

            # Record grid state and update last dist

            last_dist = self.updateIfDistChange(dist, last_dist)


            # Colour green because have been searched
            self._colourMainTiles(next_node, val_at)

            if GridCreator.ETILE in val_at:

                # Reached end so stop
                self.__finalDist = dist
                break



            adj_node: Tuple[int, int]
            for adj_node in self.adj4_gen(next_node[0], next_node[1]):

                # Limits checked inside generator function above

                if adj_node not in seen and GridCreator.BARRIER_TILE not in self.getVal(adj_node):
                    # New node is inside grid, and is not a barrier
                    seen.add(adj_node)
                    self.parents[adj_node] = next_node


                    # Colour this node yellow on the grid
                    if GridCreator.ETILE not in self.getVal(adj_node):
                        self._curGrid[adj_node[1]][adj_node[0]] = colored(GridCreator.TILE, "blue")

                    queue.append((adj_node, dist+1))



        self.__checked = len(seen)







class AStar(Search):
    def __init__(self):
        super().__init__()

        self._pathSteps = []
        self._steps = []
        self.__finalDist = 0
        self.__checked = 0



    def _colourMainTiles(self, next_node: Tuple[int, int], val_at: str):
        if GridCreator.STILE not in val_at and GridCreator.ETILE not in val_at:
            # Not a start or end point so should colour green
            self._curGrid[next_node[1]][next_node[0]] = colored(GridCreator.TILE, "green")

    def search(self) -> None:


        self.end = self._curGrid # Goes through setter function
        self.start = self._curGrid # Goes through setter function


        queue = []
        hp.heapify(queue)

        self.parents: dict = {}  # Stores parent node for each node so a path to start can be re-traced
        seen: set = set()


        self._frames.append(deepcopy(self._curGrid))

        queue.append((self.heuristic(self.start), self.start, 0))

        while queue:
            _, next_node, dist = hp.heappop(queue)
            val_at = self.getVal(next_node)

            # Record grid state and update last dist

            self._frames.append(deepcopy(self._curGrid))
            self._steps.append(deepcopy(self._curGrid))


            # Colour green because have been searched
            self._colourMainTiles(next_node, val_at)

            if GridCreator.ETILE in val_at:

                # Reached end so stop
                self.__finalDist = dist
                break



            adj_node: Tuple[int, int]
            for adj_node in self.adj4_gen(next_node[0], next_node[1]):

                # Limits checked inside generator function above

                if adj_node not in seen and GridCreator.BARRIER_TILE not in self.getVal(adj_node):
                    # New node is inside grid, and is not a barrier
                    seen.add(adj_node)
                    self.parents[adj_node] = next_node


                    # Colour this node yellow on the grid
                    if GridCreator.ETILE not in self.getVal(adj_node):
                        self._curGrid[adj_node[1]][adj_node[0]] = colored(GridCreator.TILE, "blue")

                    hp.heappush(queue, (self.heuristic(adj_node), adj_node, dist+1))





    def heuristic(self, point):

        return Search.manhattan(point, self.end)



    def outputSteps(self):

        for step in self._steps:
            time.sleep(0.8)
            for row in step:
                print(*row)
            print("-"*40)


    def outputSearchInfo(self):
        pass
        #raise NotImplementedError



if __name__=="__main__":
    tc = GridCreator()

    grid = tc.generate_grid(1)
    tb = AStar()

    tb.process_search(grid, True)
    tb.outputSteps()
    tb.process_path()
