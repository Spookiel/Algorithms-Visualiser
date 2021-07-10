from abc import ABC
from termcolor import colored
from typing import Tuple
from collections import deque
from Creator import GridCreator
import time


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


    def locateStart(self) -> Tuple[int, int]:
        # "s" in colored("s", "blue") -> True
        # "s" == colored("s", "blue") -> False
        for y in range(len(self._curGrid)):
            for x in range(len(self._curGrid)):
                if "s" in self._curGrid[y][x]:
                    return x,y
        print("START POINT NOT FOUND, USING TOP LEFT CORNER")
        return 0,0

    def locateEnd(self) -> Tuple[int, int]:
        # "e" in colored("e", "blue") -> True
        # "e" == colored("e", "blue") -> False
        for y in range(len(self._curGrid)):
            for x in range(len(self._curGrid)):
                if "e" in self._curGrid[y][x]:
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
        parents = {}  # Stores parent node for each node so a path to start can be re-traced
        seen = set()
        lastDist = 0
        self.start = self.locateStart()
        self.end = self.locateEnd()

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
            if "s" not in valAt and "e" not in valAt:
                # Not a start or end point so should colour green
                self._curGrid[nextNode[1]][nextNode[0]] = colored(".", "green")

            if "e" in valAt:
                # Reached end so stop
                break


            # Go to adjacent nodes

            for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                nx, ny = nextNode[0]+dx, nextNode[1]+dy
                adjNode = (nx, ny)

                if self.checkLim(adjNode) and adjNode not in seen and "#" not in self.getVal(adjNode):
                    # New node is inside grid, and is not a barrier
                    seen.add(adjNode)
                    parents[adjNode] = nextNode


                    # Colour this node yellow on the grid
                    if "e" not in self.getVal(adjNode):
                        self._curGrid[adjNode[1]][adjNode[0]] = colored(".", "blue")
                    #print("Adding", adjNode, "From", nextNode, "Dist", dist)
                    queue.append((adjNode, dist+1))


    def outputSteps(self):

        for step in self._steps:
            time.sleep(0.8)
            for row in step:
                print(*row)
            print("-"*40)
tc = GridCreator()
grid = tc.generate_grid(15)



ts = GridSolver()
ts._curGrid = grid



ts.bfs()
ts.outputSteps()