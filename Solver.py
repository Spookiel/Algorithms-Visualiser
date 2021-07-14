from abc import ABC, abstractmethod
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

    def display_menu(self):
        raise NotImplementedError

    def process_choice(self):
        raise NotImplementedError

class GraphSolver():
    def __init__(self) -> None:
        pass

    def display_menu(self):
        raise NotImplementedError

    def process_choice(self):
        raise NotImplementedError
class GridSolver():
    def __init__(self) -> None:
        self._curGrid = [] #Stores current copy of the grid
        self._steps = []
        self.start: Tuple[int, int] = 0, 0
        self.end: Tuple[int, int] = 0, 0
        self.parents = {}

    def display_menu(self):
        raise NotImplementedError

    def process_choice(self):
        raise NotImplementedError


tc = GridCreator()
grid = tc.generate_grid(30)
"""


ts = GridSolver()
ts._curGrid = grid



ts.bfs()
ts.tracePath()
ts.drawPath()
ts.outputSteps()
ts.outputPath()"""
