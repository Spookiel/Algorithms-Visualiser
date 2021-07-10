from copy import deepcopy
from typing import Tuple,List
from Creator import GridCreator
from termcolor import colored
import time

class Search:
    def __init__(self):
        self._curGrid = []

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



    def checkLim(self,node: Tuple[int, int]) -> bool:
        # Checks if a node is on the grid or not
        return 0 <= node[0] < len(self._curGrid) and 0 <= node[1] < len(self._curGrid)

    def getVal(self,node: Tuple[int, int]) -> str:
        if self.checkLim(node):
            return self._curGrid[node[1]][node[0]]

class BFS(Search):

    def __init__(self):
        super().__init__()
        self._pathSteps = []
        self._steps = []



    def process_search(self, grid):
        self._curGrid = grid
        self._pathSteps = []
        self._steps = []

        self.bfs()
        self.outputSteps()
        self.process_path()
    def process_path(self):
        self.tracePath()
        self.storePath()
        self.outputPath()


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

            if last_dist != dist:
                # Record grid state and update last dist
                last_dist = int(dist) # Careful of copying errors

                copGrid = []
                for row in self._curGrid:
                    copGrid.append(row[:])
                self._steps.append(copGrid)

            # Colour green because have been searched
            if GridCreator.STILE not in val_at and GridCreator.ETILE not in val_at:
                # Not a start or end point so should colour green
                self._curGrid[next_node[1]][next_node[0]] = colored(GridCreator.TILE, "green")

            if GridCreator.ETILE in val_at:
                # Reached end so stop
                break


            # Go to adjacent nodes

            for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                nx, ny = next_node[0]+dx, next_node[1]+dy
                adjNode = (nx, ny)

                if self.checkLim(adjNode) and adjNode not in seen and "#" not in self.getVal(adjNode):
                    # New node is inside grid, and is not a barrier
                    seen.add(adjNode)
                    self.parents[adjNode] = next_node


                    # Colour this node yellow on the grid
                    if GridCreator.ETILE not in self.getVal(adjNode):
                        self._curGrid[adjNode[1]][adjNode[0]] = colored(GridCreator.TILE, "blue")
                    #print("Adding", adjNode, "From", next_node, "Dist", dist)
                    queue.append((adjNode, dist+1))


    def outputSteps(self):

        for step in self._steps:
            time.sleep(0.8)
            for row in step:
                print(*row)
            print("-"*40)


    def tracePath(self):

        self.path = [self.end]
        while self.path[-1] != self.start:
            self.path.append(self.parents[self.path[-1]])

        self.path = self.path[::-1]
        self.path.pop(0)
        self.path.pop(-1)
    def storePath(self):

        for loc in self.path:
            self._curGrid[loc[1]][loc[0]] = colored(GridCreator.TILE, "grey")

            self._pathSteps.append(deepcopy(self._curGrid))

    def outputPath(self):

        for step in self._pathSteps:
            print("-"*40)
            time.sleep(0.5)
            for row in step:
                print(*row)
tc = GridCreator()

grid = tc.generate_grid(20)
tb = BFS()

tb.process_search(grid)

