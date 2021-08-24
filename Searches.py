from copy import deepcopy
from typing import Tuple,List
from Creator import GridCreator
from termcolor import colored
import time
import heapq as hp

class Search:

    adj4: List[List[int]] = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    adj8: List[List[int]] = adj4 + [[1, 1], [-1, 1], [1, -1], [-1, -1]]

    def __init__(self):
        self._curGrid = []
        self._pathSteps = []
        self._steps = []
        self.__finalDist = 0
        self.__checked = 0

    @staticmethod
    def locate_start(grid) -> Tuple[int, int]:
        # "s" in colored("s", "blue") -> True
        # "s" == colored("s", "blue") -> False
        for y in range(len(grid)):
            for x in range(len(grid)):
                if GridCreator.STILE in grid[y][x]:
                    return x, y
        print("START POINT NOT FOUND, USING TOP LEFT CORNER")
        return 0, 0

    @staticmethod
    def locate_end(grid) -> Tuple[int, int]:
        # "e" in colored("e", "blue") -> True
        # "e" == colored("e", "blue") -> False
        for y in range(len(grid)):
            for x in range(len(grid)):
                if GridCreator.ETILE in grid[y][x]:
                    return x, y
        print("END POINT NOT DEFINED, USING BOTTOM RIGHT CORNER")
        return len(grid) - 1, len(grid) - 1



    def checkLim(self, node: Tuple[int, int]) -> bool:
        # Checks if a node is on the grid or not
        return 0 <= node[0] < len(self._curGrid) and 0 <= node[1] < len(self._curGrid)

    def getVal(self,node: Tuple[int, int]) -> str:
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



    def show_animation(self):
        raise NotImplementedError
        # Function to draw a matplotlib figure similar to that of the sorting algorithms


    def adj4_gen(self, px: int, py: int) -> Tuple[int, int]:

        for dx, dy in Search.adj4:
            nx: int = px+dx
            ny: int = py+dy

            assert len(self._curGrid) > 0
            if self.checkLim((nx, ny)):
                yield (nx, ny)

class BFS(Search):

    def __init__(self):
        super().__init__()




    def process_search(self, grid: List[List]) -> None:
        self._curGrid = grid
        self._pathSteps = []
        self._steps = []

        self.bfs()
        self.outputSteps()
        self.__process_path()

        self.outputSearchInfo()


    def __process_path(self) -> None:
        self._tracePath()
        self._storePath()
        self._outputPath()



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
            cop_grid = []
            for row in self._curGrid:
                cop_grid.append(row[:])
            self._steps.append(cop_grid)

            return int(dist) # Careful of copying errors

    def bfs(self):
        # Generates a sequence of colored grids,
        # yellow is for items currently in the queue, green is for items that have already been seen
        # Function works with manhattan distance
        self.parents: dict = {}  # Stores parent node for each node so a path to start can be re-traced
        seen: set = set()
        last_dist: int = 0
        self.start: Tuple[int, int] = self.locate_start(self._curGrid)
        self.end: Tuple[int, int] = self.locate_end(self._curGrid)
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



    def process_search(self, grid):
        self._curGrid = grid
        self._pathSteps = []
        self._steps = []

        self.astar()
        self.outputSteps()
        self.__process_path()

        print("-"*5, "Search information", "-"*5)
        print(f"Distance: {self.__finalDist}")
        print(f"Tiles checked: {self.__checked}")
        print(f"Board size: {len(self._curGrid)}x{len(self._curGrid)}")


    def astar(self):
        raise NotImplementedError

    def outputSteps(self):

        for step in self._steps:
            time.sleep(0.8)
            for row in step:
                print(*row)
            print("-"*40)


    def __process_path(self):
        self.__tracePath()
        self.__storePath()
        self.__outputPath()

    def __tracePath(self):
        raise NotImplementedError

    def __storePath(self):
        raise NotImplementedError

    def __outputPath(self):
        raise NotImplementedError




tc = GridCreator()

grid = tc.generate_grid(0)
tb = BFS()

tb.process_search(grid)
