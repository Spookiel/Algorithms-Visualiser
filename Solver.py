from abc import ABC
from termcolor import colored
from typing import Tuple
from collections import deque
from Creator import GridCreator
import time
from copy import deepcopy

class Solver(ABC):
    def __init__(self) -> None:
        pass


class MazeSolver():
    def __init__(self) -> None:
        pass

class GraphSolver():
    def __init__(self) -> None:
        pass
class GridSolver():
    def __init__(self) -> None:
        self._curGrid = [] #Stores current copy of the grid
        self._steps = []
        self.start: Tuple[int, int] = 0, 0
        self.end: Tuple[int, int] = 0, 0
        self.parents = {}

    def locateStart(self) -> Tuple[int, int]:
        # "s" in colored("s", "blue") -> True
        # "s" == colored("s", "blue") -> False
        for y in range(len(self._curGrid)):
            for x in range(len(self._curGrid)):
                if GridCreator.STILE in self._curGrid[y][x]:
                    return x,y
        print("START POINT NOT FOUND, USING TOP LEFT CORNER")
        return 0,0

    def locateEnd(self) -> Tuple[int, int]:
        # "e" in colored("e", "blue") -> True
        # "e" == colored("e", "blue") -> False
        for y in range(len(self._curGrid)):
            for x in range(len(self._curGrid)):
                if GridCreator.ETILE in self._curGrid[y][x]:
                    return x,y
        print("END POINT NOT DEFINED, USING BOTTOM RIGHT CORNER")
        return len(self._curGrid)-1, len(self._curGrid)-1

    def checkLim(self, node):
        # Checks if a node is on the grid or not
        return 0 <= node[0] < len(self._curGrid) and 0 <= node[1] < len(self._curGrid)

    def getVal(self, node):
        if self.checkLim(node):
            return self._curGrid[node[1]][node[0]]
    def bfs(self):
        # Generates a sequence of colored grids,
        # yellow is for items currently in the queue, green is for items that have already been seen
        # Function works with manhattan distance
        self.parents = {}  # Stores parent node for each node so a path to start can be re-traced
        seen = set()
        lastDist = 0
        self.start = self.locateStart()
        self.end = self.locateEnd()
        self._pathSteps = []
        queue = [(self.start, 0)]  # (Node, distance)
        seen.add(self.start)
        while queue:
            nextNode, dist = queue.pop(0)
            #print(dist, nextNode, lastDist)
            valAt = self.getVal(nextNode)

            if lastDist!=dist:
                # Record grid state and update last dist
                lastDist = int(dist) # Careful of copying errors

                copGrid = []
                for row in self._curGrid:
                    copGrid.append(row[:])
                self._steps.append(copGrid)
            # Colour green because have been searched
            if GridCreator.STILE not in valAt and GridCreator.ETILE not in valAt:
                # Not a start or end point so should colour green
                self._curGrid[nextNode[1]][nextNode[0]] = colored(GridCreator.TILE, "green")

            if GridCreator.ETILE in valAt:
                # Reached end so stop
                break


            # Go to adjacent nodes

            for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                nx, ny = nextNode[0]+dx, nextNode[1]+dy
                adjNode = (nx, ny)

                if self.checkLim(adjNode) and adjNode not in seen and "#" not in self.getVal(adjNode):
                    # New node is inside grid, and is not a barrier
                    seen.add(adjNode)
                    self.parents[adjNode] = nextNode


                    # Colour this node yellow on the grid
                    if GridCreator.ETILE not in self.getVal(adjNode):
                        self._curGrid[adjNode[1]][adjNode[0]] = colored(GridCreator.TILE, "blue")
                    #print("Adding", adjNode, "From", nextNode, "Dist", dist)
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
    def drawPath(self):

        for loc in self.path:
            self._curGrid[loc[1]][loc[0]] = colored(GridCreator.TILE, "grey")

            self._pathSteps.append(deepcopy(self._curGrid))

    def outputPath(self):

        for step in self._pathSteps:
            print("-"*40)
            time.sleep(0.6)
            for row in step:
                print(*row)


tc = GridCreator()
grid = tc.generate_grid(30)



ts = GridSolver()
ts._curGrid = grid



ts.bfs()
ts.tracePath()
ts.drawPath()
ts.outputSteps()
ts.outputPath()
